__all__ = ['AbstractModel', 'context_model', 'MODELS', 'context', 'Undefined']

from dataclasses import dataclass, Field, field
from contextvars import ContextVar, Context, copy_context
from abc import ABC, abstractmethod
from functools import wraps
from typing import ClassVar, Union
from collections import ChainMap
from detabase.engine import DetaQuery

Undefined = object()

MODELS = ChainMap()
context = copy_context()


@dataclass
class AbstractModel(ABC):
	FIELD_NAMES: ClassVar[list[str]] = None
	FIELDS: ClassVar[dict[str, Field]] = None
	DESCRIPTORS: ClassVar[dict[str, 'BaseDescriptor']] = None
	DETA_QUERY: ClassVar[DetaQuery] = None
	TABLE: ClassVar[str] = None
	ITEM_NAME: ClassVar[str] = None
	VAR: ClassVar[ContextVar] = None
	CONTEXT: ClassVar[Context] = None
	DATA: ClassVar[dict[str, dict]] = None
	EXIST_PARAMS: ClassVar[Union[list[str], str]] = None
	SEARCH_PARAM: ClassVar[str] = None
	
	key: str = field(default=None)
	
	
	@abstractmethod
	def fields(cls):
		return NotImplemented
	
	@abstractmethod
	def descriptors(cls):
		return NotImplemented
	
	@abstractmethod
	def json(self):
		return NotImplemented


def context_model(cls: type[AbstractModel]):
	@wraps(cls)
	def wrapper():
		cls.VAR = ContextVar(f'{cls.__name__}Var', default=dict())
		cls.CONTEXT = context
		cls.FIELDS = cls.fields()
		cls.DESCRIPTORS = cls.descriptors()
		cls.FIELD_NAMES = cls.FIELDS.keys()
		return cls
	
	return wrapper()