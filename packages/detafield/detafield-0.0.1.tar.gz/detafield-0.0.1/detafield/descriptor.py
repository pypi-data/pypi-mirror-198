import datetime
import os
import re
import json
import io
import calendar
from contextvars import ContextVar, copy_context, Context
from functools import wraps, cache, cached_property
from enum import Enum
from abc import ABC
from typing import Any, get_args, Union, Callable, NamedTuple, ClassVar, get_origin, Optional
from dataclasses import dataclass, field, fields, Field, asdict, astuple
from collections import UserString, ChainMap
from detabase import DetaBase
from detabase.engine import DetaQuery
from anyio import create_task_group
from unidecode import unidecode

Undefined = object()

MODELS = ChainMap()
context = copy_context()


### MODELS

@context_model
@dataclass
class Facility(Model):
	EXIST_PARAMS = 'name'
	name: str = TitleField('required')
	phone: Phone = RegexField('required')
	email: str = StringField()
	address: str = StringField('required')
	city: str = StringField('required')
	cep: str = StringField()
	description: str = StringField()
	search: str = AutoField()
	
	def __str__(self):
		return self.name


@context_model
@dataclass
class Person(Model):
	EXIST_PARAMS = ['code', 'cpf']
	SEARCH_PARAM = 'search_names'
	
	class Gender(BaseEnum):
		M = 'Masculino'
		F = 'Feminino'
	
	fname: str = TitleField('required')
	lname: str = TitleField('required')
	bdate: datetime.date = DateField('required')
	gender: Gender = EnumField('required')
	cpf: CPF = RegexField(default=None)
	transgender: bool = BooleanField(default=False)
	non_binary: bool = BooleanField(default=False)
	code: str = AutoField(default=None, method_name='get_code')
	search_names: str = AutoField(default=None, method_name='get_search')
	name: str = StringField(default=str)
	
	def get_search(self):
		return Regex.normalize_lower(Regex.remove_extra_spaces(f'{self.fullname} {self.name}'))
	
	def get_code(self):
		file = io.StringIO()
		file.write(self.gender.name)
		file.write(self.bdate.isoformat().replace("-", ""))
		file.write(Regex.normalize(self.fname[:2]).upper())
		file.write(Regex.normalize(self.lname.split()[-1][:2]).upper())
		return file.getvalue()
	
	def __str__(self):
		return self.fullname
	
	@property
	def age(self):
		return age(self.bdate)
	
	@property
	def fullname(self):
		return f'{self.fname} {self.lname}'


@context_model
@dataclass
class Patient(Model):
	EXIST_PARAMS = 'person_key'
	person_key: Person = KeyField('required')
	phone: Phone = RegexField()
	email: Email = RegexField()
	address: str = StringField()
	city: str = StringField()
	notes: str = StringField()
	search: str = AutoField()
	
	def __str__(self):
		return str(self.person)
	
	@property
	def age(self):
		return self.person.age


@context_model
@dataclass
class Doctor(Model):
	EXIST_PARAMS = 'person_key'
	person_key: Person = KeyField('required')
	facility_key: Facility = KeyField('required')
	register: str = StringField('required')
	university: str = StringField()
	graduation_field: str = StringField()
	graduation_year: int = IntegerField(min=1950, max=2025)
	specialties: list[str] = StringListField()
	health_insuances: list[str] = StringListField()
	picture: str = StringField()
	notes: str = StringField()
	search: str = AutoField()
	
	def __str__(self):
		return str(self.person)
	
	@property
	def age(self):
		return self.person.age


@context_model
@dataclass
class Therapist(Doctor):
	pass


@context_model
@dataclass
class Employee(Model):
	EXIST_PARAMS = 'persono_key'
	person_key: Person = KeyField('required')
	facility_key: Facility = KeyField('required')
	scope: str = StringField()  # todo: modificar para enum
	base_value: Union[float, int] = NumberField(default=None)
	salary_indexed: bool = BooleanField(default=False)
	days_month: int = IntegerField(min=0, max=31)
	phone: Phone = RegexField()
	email: Email = RegexField()
	address: str = StringField()
	city: str = StringField()
	assistant: bool = BooleanField(default=False)
	reception: bool = BooleanField(default=False)
	active: bool = BooleanField(default=True)
	housekeeping: bool = BooleanField(default=False)
	management: bool = BooleanField(default=False)
	external: bool = BooleanField(default=False)
	financial: bool = BooleanField(default=False)
	telephonist: bool = BooleanField(default=False)
	notes: str = StringField()
	search: str = AutoField()
	
	def __str__(self):
		return str(self.person)
	
	@property
	def age(self):
		return self.person.age


async def main():
	model = Doctor
	# await model.update_context()
	# print(x)
	# print(x.export())
	# print(x.dumps())
	# print(model.database_keys())
	for item in await model.items():
		print(item.person, item.age, item.search)
		print(item.json())
		print(json_dumps(item))


if __name__ == '__main__':
	import asyncio
	
	asyncio.run(main())



