__all__ = [
		'Model',
		'BaseDescriptor',
		'Validator',
		'TitleField',
		'FloatField',
		'KeyField',
		'KeyListField',
		'IntegerField',
		'NumberField',
		'EnumField',
		'RegexField',
		'RangeField',
		'StringField',
		'StringListField',
		'AutoField',
		'DateField',
		'DatetimeField',
		'BooleanField'
]

from functools import wraps, cache, cached_property
from abc import ABC
from typing import get_args, Union, Callable, ClassVar, get_origin, Any
from dataclasses import dataclass, field, fields, Field, asdict, astuple
from collections import ChainMap
from detabase import DetaBase
from detabase.engine import DetaQuery
from anyio import create_task_group
from detafield.abstracet_model import *
from detafield.json_encoder import *
from detafield.regex import *



@dataclass
class Model(AbstractModel):
	
	def __post_init__(self):
		for item in self.descriptors().values():
			if isinstance(item, AutoField):
				setattr(self, item.private_name, getattr(self, item.method_name or f'get_{item.public_name}')())
	
	@classmethod
	def search_param(cls):
		return cls.SEARCH_PARAM or 'search'
	
	@classmethod
	def database_keys(cls):
		result = []
		gen = (item for item in cls.DATA.values())
		try:
			while True:
				result.extend(next(gen).keys())
		except StopIteration:
			return set(result)
	
	def get_search(self):
		return Regex.normalize_lower(str(self))
	
	def __lt__(self, other):
		return Regex.normalize_lower(str(self)) < Regex.normalize_lower(str(other))
	
	def asdict(self, exclude: set[str] = None):
		exclude_keys = exclude or set()
		return {key: val for key, val in asdict(self).items() if key not in exclude_keys}
	
	def json(self, exclude: set[str] = None):
		return json_parse(self.asdict(exclude))
	
	def export(self):
		return json_parse(asdict(self))
	
	def dumps(self, exclude: set[str] = None) -> str:
		return json_dumps(self.asdict(exclude))
	
	@staticmethod
	def loads(string: str) -> Any:
		return json_loads(string)
	
	@classmethod
	def cleaned_data(cls, data: dict[str, Any]):
		return {key: val for key, val in data.items() if key in cls.FIELD_NAMES}
	
	@classmethod
	async def fetch_all(cls, query: DetaQuery = None):
		return await DetaBase(cls.table()).fetch_all(query or cls.DETA_QUERY)
	
	@classmethod
	async def fetch(cls, query: DetaQuery = None):
		return await DetaBase(cls.table()).fetch(query or cls.DETA_QUERY)
	
	@classmethod
	async def get(cls, key: str):
		return await DetaBase(cls.table()).get(key)
	
	@classmethod
	async def get_first(cls, query: DetaQuery = None):
		return await DetaBase(cls.table()).get_first(query or cls.DETA_QUERY)
	
	def make_query_dict(self, keys: list[str]):
		result = dict()
		for item in keys:
			value = getattr(self, item, None)
			if value:
				if isinstance(value, str):
					result[f'{item}?contains'] = json_parse(value)
				else:
					result[item] = json_parse(value)
		return result
	
	@classmethod
	def make_instance(cls, data: dict):
		return cls(**cls.cleaned_data(data))
	
	async def exist(self):
		if self.EXIST_PARAMS:
			if isinstance(self.EXIST_PARAMS, list):
				query = list()
				for item in self.EXIST_PARAMS:
					query.append(self.make_query_dict(item.split()))
			else:
				query = self.make_query_dict(self.EXIST_PARAMS.split())
		else:
			query = {key: val for key, val in self.json().items() if val}
		result = await self.fetch_all(query)
		if result:
			return result[0]
		return None
	
	async def save(self):
		await self.get_model_data()
		exist = await self.exist()
		if exist:
			instance = self.make_instance(exist)
			print(f'{instance} já existe no banco de dados com a chave {getattr(instance, "key")}.')
			return instance
		saved = await DetaBase(self.table()).insert(data=self.json())
		if saved:
			instance = self.make_instance(saved)
			print(f'{instance} foi criado no banco de dados com a chave {getattr(instance, "key")}.')
			return instance
		raise Exception('Os dados não puderam ser salvos.')
	
	async def update(self):
		return await DetaBase(self.table()).put(data=self.json())
	
	@classmethod
	async def items(cls) -> list['cls']:
		await cls.update_context()
		return sorted([cls.make_instance(item) for item in cls.DATA.values()])
	
	@classmethod
	async def delete_object(cls, key: str):
		return await DetaBase(cls.table()).delete(key)
	
	async def delete_self(self):
		return await self.delete_object(getattr(self, 'key'))
	
	@classmethod
	def key_models(cls):
		return [item.model for item in cls.key_descriptors().values()]
	
	@classmethod
	def base_key_models(cls):
		result = []
		for item in [cl for cl in cls.__bases__ if isinstance(cl, Model)]:
			result.extend(item.key_models())
		return set(result)
	
	@classmethod
	def dependant_models(cls):
		result = [cls]
		for item in [*cls.key_models(), *cls.base_key_models()]:
			result.extend([*item.dependant_models()])
		return set(result)
	
	@classmethod
	async def update_context(cls):
		models = cls.dependant_models()
		async with create_task_group() as tasks:
			for model in models:
				tasks.start_soon(model.get_model_data, model.DETA_QUERY)
	
	@classmethod
	async def get_model_data(cls, query: DetaQuery = None):
		
		async def set_data(model_query=query):
			cleaned_query = None
			if model_query:
				cleaned_query = {key: val for key, val in model_query.items() if
				                 key.rstrip('?contains') in cls.FIELD_NAMES}
			cls.DATA = {item['key']: item for item in await cls.fetch_all(cleaned_query or cls.DETA_QUERY)}
		
		def set_context():
			cls.var().set(cls.DATA)
		
		await set_data()
		context.run(set_context)
	
	@classmethod
	@cache
	def fields(cls):
		return {item.name: item for item in fields(cls)}
	
	@classmethod
	@cache
	def field(cls, name: str):
		return cls.fields()[name]
	
	@classmethod
	@cache
	def descriptors(cls):
		return {name: val for name, val in vars(cls).items() if isinstance(val, BaseDescriptor)}
	
	@classmethod
	@cache
	def key_descriptors(cls):
		return {name: val for name, val in cls.descriptors().items() if isinstance(val, KeyField)}
	
	@classmethod
	@cache
	def descriptor(cls, name: str):
		return cls.descriptors()[name]
	
	@classmethod
	@cache
	def table(cls):
		return cls.TABLE or cls.__name__
	
	@classmethod
	@cache
	def var(cls):
		return cls.VAR
	
	@classmethod
	@cache
	def item_name(cls):
		return cls.ITEM_NAME or Regex.slug(cls.__name__)
	
	@classmethod
	@cache
	def key_name(cls):
		return f'{cls.item_name()}_key'
	
	@classmethod
	@cache
	def item_list_name(cls):
		return f'{cls.item_name()}_list'
	
	@classmethod
	@cache
	def key_list_name(cls):
		return f'{cls.item_name()}_key_list'


### BASE DESCRIPTORS

class BaseDescriptor(ABC):
	def __init__(self, *args, **kwargs):
		self.args = args
		self.default = kwargs.pop('default', None)
		self.factory = kwargs.pop('factory', None)
		self.label = kwargs.pop('label', None)
		self.parser = kwargs.pop('parser', lambda x: x)
		self.predicate = kwargs.pop('predicate', lambda x: True)
		self.pattern = kwargs.pop('pattern', None)
		self.form_edit = kwargs.pop('form_edit', 'new update')
		for k in kwargs:
			setattr(self, k, kwargs[k])
	
	def __set_name__(self, owner, name):
		self.public_name = name
		self.private_name = f'_{name}'
		self.owner: Model = owner
	
	def __get__(self, instance, owner):
		if instance is None:
			if isinstance(self.default, Callable):
				return self.default()
			return self.default
		return getattr(instance, self.private_name)
	
	def __set__(self, instance, value):
		value = self.try_parse(value)
		self.validate(value)
		setattr(instance, self.private_name, value)
	
	def try_parse(self, value: Any):
		try:
			value = self.parser_engine(value)
		finally:
			if self.no_value(value):
				if self.factory:
					value = self.factory()
			return value
	
	def parser_engine(self, value):
		return self.parser(value)
	
	def validate_none(self):
		if self.required is True:
			raise ValueError(f'{self.attribute_name} não pode ser nulo.')
	
	def validate(self, value):
		if self.no_value(value):
			self.validate_none()
	
	@property
	def required(self):
		return 'required' in self.args
	
	@property
	def owner_name(self):
		return self.owner.__name__
	
	@property
	def attribute_name(self):
		return '{}.{}'.format(self.owner_name, self.public_name)
	
	@property
	def field(self):
		return self.owner.field(self.public_name)
	
	@property
	def type_hint(self):
		return self.field.type
	
	@property
	def type_origin(self):
		return get_origin(self.type_hint)
	
	@property
	def type_args(self):
		return [tp for tp in get_args(self.type_hint) if tp is not None]
	
	@property
	def is_union(self):
		return self.type_origin is Union
	
	@cached_property
	def is_sequence(self):
		return self.type_origin in [list, set]
	
	@cached_property
	def is_map(self):
		return self.type_origin in [dict, ChainMap]
	
	@cached_property
	def is_container(self):
		return self.is_map or self.is_sequence
	
	@cached_property
	def container(self):
		if self.is_container:
			return self.type_origin
		return None
	
	@staticmethod
	def value_is_none(value):
		return value is None
	
	@staticmethod
	def value_is_blank_line(value):
		return value == ''
	
	@staticmethod
	def value_is_undefined(value):
		return value == Undefined
	
	def no_value(self, value):
		return self.value_is_none(value) or self.value_is_blank_line(value) or self.value_is_undefined(value)


class Validator(BaseDescriptor):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	
	def validate_extra(self, value):
		pass
	
	def validate_union_type(self, value):
		self.args_validation(value, self.type_args)
	
	def validate_simple_type(self, value):
		self.isinstance_validation(value, self.type_hint)
	
	def validate_container_type(self, value):
		self.isinstance_validation(value, self.container)
		if self.is_map:
			for val in value.values():
				self.args_validation(val, self.type_args)
		elif self.is_sequence:
			for val in value:
				self.args_validation(val, self.type_args)
	
	def isinstance_validation(self, value: Any, base_type: type):
		if not isinstance(value, base_type):
			raise ValueError(
					f'{self.attribute_name} exige um tipo {base_type} e o encontrado para {value} é {type(value)}.')
	
	def args_validation(self, value: Any, args: list[type]):
		if not type(value) in args:
			raise ValueError(
					f'{self.attribute_name}: o tipo de {value} ({type(value)} não confere com o esperado ({args}).')
	
	def full_validation(self, value):
		if self.no_value(value):
			self.validate_none()
		else:
			if self.is_container:
				self.validate_container_type(value)
			elif self.is_union:
				self.validate_union_type(value)
			else:
				self.validate_simple_type(value)
			self.predicate_validation(value)
			self.validate_extra(value)
	
	def predicate_validation(self, value):
		if not self.predicate(value):
			raise ValueError(f'{self.attribute_name}: o valor "{value}" não pode ser validado.')
	
	def validate(self, value):
		self.full_validation(value)


### DESCRIPTORS

class TitleField(Validator):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	
	def parser_engine(self, value):
		return Regex.remove_extra_spaces(value).title()


class DatetimeField(Validator):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	
	def parser_engine(self, value):
		return Regex.search_datetime(value)


class DateField(Validator):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	
	def parser_engine(self, value):
		return Regex.search_date(value)


class StringField(Validator):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	
	def parser_engine(self, value):
		return '' if value is None else str(value)


class NumberField(Validator):
	def __init__(self, *args, **kwargs):
		self.min = kwargs.pop('min', Undefined)
		self.max = kwargs.pop('max', Undefined)
		self.step = kwargs.pop('step', 0.01)
		super().__init__(*args, **kwargs)
	
	def validate_extra(self, value):
		if self.min is not Undefined:
			if self.min > value:
				raise ValueError(f'{self.attribute_name} ({value}) não pode ser menor que {self.min}.')
		if self.max is not Undefined:
			if self.max < value:
				raise ValueError(f'{self.attribute_name} ({value}) não pode ser maior que {self.max}.')
	
	def parser_engine(self, value):
		return Regex.to_number(value)


class IntegerField(NumberField):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.step = 1
	
	def parser_engine(self, value):
		return Regex.search_int(value)

class FloatField(NumberField):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	
	def parser_engine(self, value):
		return Regex.search_float(value)


class EnumField(Validator):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	
	def parser_engine(self, value):
		if isinstance(value, str):
			return self.type_hint[value]
		return value


class RegexField(Validator):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	
	def parser_engine(self, value):
		if isinstance(value, str):
			return self.type_hint(value)
		return value if value is not None else ''


class BooleanField(Validator):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	
	def parser_engine(self, value):
		if isinstance(value, str):
			if value == 'off':
				return False
			elif value == 'on':
				return True
		return value


class RangeField(IntegerField):
	pass


class StringListField(Validator):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	
	def __set__(self, instance, value):
		value = self.parser_engine(value)
		self.validate(value)
		setattr(instance, self.private_name, value)
	
	def parser_engine(self, value):
		return Regex.split_string_lines(value)
	
	def full_validation(self, value):
		if not isinstance(value, list):
			raise ValueError(f'{self.attribute_name}: o valor não é uma lista.')
		for i in value:
			if not isinstance(i, str):
				raise ValueError(
						f'{self.attribute_name}: o item da lista ({i} => {type(i)}) não corresponde a uma string.')


class AutoField(Validator):
	def __init__(self, *args, **kwargs):
		self.method_name = kwargs.pop('method_name', None)
		super().__init__(*args, **kwargs)
		self.form_edit = ''
		self.default = None
	
	def validate(self, value):
		pass


### KEY DESCRIPTORS

class KeyField(BaseDescriptor):
	def __set__(self, instance, value):
		setattr(instance, self.private_name, value)
		setattr(instance, self.item_name, self.model_instance(value))
	
	@property
	def model(self):
		return self.type_hint
	
	@property
	def model_name(self):
		return self.model.__name__
	
	@property
	def item_name(self):
		return self.model.item_name()
	
	def model_instance(self, key):
		if key:
			return self.model(**self.model.cleaned_data(context.get(self.model.var())[key]))
		return None


class KeyListField(KeyField):
	def __set__(self, instance, value):
		setattr(instance, self.private_name, value)
		setattr(self.owner, self.item_list_name, self.model_instance_list(value))
	
	@property
	def model(self):
		return get_args(self.type_hint)[0]
	
	@property
	def model_name(self):
		return self.model.__name__
	
	@property
	def item_list_name(self):
		return self.model.item_list_name()
	
	def model_instance_list(self, value):
		if value:
			return [self.model_instance(key) for key in value]
		return list()
