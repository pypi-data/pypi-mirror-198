__all__ = ['BaseEnum', 'Month']

from enum import Enum
from typing import Union
from detafield.regex import Regex


class BaseEnum(Enum):
	
	def json(self):
		return self.name


class Month(BaseEnum):
	JAN = 'Janeiro', 1
	FEV = 'Fevereiro', 2
	MAR = 'Março', 3
	ABR = 'Abril', 4
	MAI = 'Maio', 5
	JUN = 'Junho', 6
	JUL = 'Julho', 7
	AGO = 'Agosto', 8
	SET = 'Setembro', 9
	OUT = 'Outubro', 10
	NOV = 'Novembro', 11
	DEZ = 'Dezembro', 12
	
	@classmethod
	def members(cls):
		return [*cls.__members__.values()]
	
	@classmethod
	def int_map(cls):
		return {int(member): member for member in cls.members()}
	
	@classmethod
	def name_map(cls):
		return {Regex.normalize_lower(str(member)): member for member in cls.members()}
	
	@classmethod
	def map(cls):
		return {**cls.int_map(), **cls.name_map(), **{str(int(member)): member for member in cls.members()},
		        **{member.name: member for member in cls.members()}}
	
	@classmethod
	def get(cls, key: Union[str, int]):
		if isinstance(key, int):
			return cls.map()[key]
		return cls.map()[Regex.normalize_lower(key)]
	
	def __str__(self):
		return self.value[0]
	
	def __int__(self):
		return self.value[1]

