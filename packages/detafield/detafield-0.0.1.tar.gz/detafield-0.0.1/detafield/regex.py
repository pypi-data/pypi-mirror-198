__all__ = ['Regex', 'Email', 'Phone', 'CPF']

import re
import datetime
from unidecode import unidecode
from typing import Union
from collections import UserString


class Regex(UserString):
	
	def __str__(self):
		return self.format()
	
	def format(self):
		return self.data
	
	@staticmethod
	def year_pattern():
		return re.compile(r'\b(19|20)\d{2}\b')
	
	@staticmethod
	def day_pattern():
		return re.compile(r'\b([0-2]\d|3[0-1])\b')
	
	@staticmethod
	def month_pattern():
		return re.compile(r'\b(0\d|1[0-2])\b')
	
	@staticmethod
	def get_date_string(value: str) -> str:
		values = re.split(r'[\./-]', value)
		print(values)
		years = list(
				filter(lambda x: x is not None, [Regex.group_or_none(Regex.year_pattern(), item) for item in values]))
		days = list(
				filter(lambda x: x is not None, [Regex.group_or_none(Regex.day_pattern(), item) for item in values]))
		months = list(
				filter(lambda x: x is not None, [Regex.group_or_none(Regex.month_pattern(), item) for item in values]))
		if len(months) == 2:
			if months[0] != months[1]:
				cleaned_months = [item for item in months if not item in days]
				if cleaned_months:
					months = cleaned_months
					days.remove(cleaned_months[0])
				else:
					days = [days[0]]
					months = [months[1]]
			else:
				days = [days[0]]
				months = [months[0]]
		elif len(months) == 1:
			if len(days) == 2:
				days.remove(months[0])
		return f'{years[0]}-{months[0]}-{days[0]}'
	
	@staticmethod
	def search_datetime_or_date(value: str) -> Union[datetime.datetime, datetime.date, str]:
		result = Regex.search_datetime(value)
		if isinstance(result, str):
			return Regex.search_date(result)
		return result
	
	@staticmethod
	def search_datetime(value: str) -> Union[datetime.datetime, str]:
		match = re.search(
				r'(19|20)(\d{2})-(01|02|03|04|05|06|07|08|09|10|11|12)-([0-3]\d)T([0-2]\d):([0-5]\d)(:[0-5]\d\.\d{6})?',
				value)
		if match:
			print(match)
			return datetime.datetime.fromisoformat(match.group())
		print(f'match not found for datetime: {value}')
		return value
	
	@staticmethod
	def search_int(value: str):
		if isinstance(value, str):
			return int(float(re.sub(r',', '.', value)).__round__(0))
		return value
	
	@staticmethod
	def search_float(value: str):
		if isinstance(value, str):
			return float(re.sub(r',', '.', value))
		return value
	
	@staticmethod
	def search_date(value: str) -> Union[datetime.date, str]:
		match = re.search(r'(19|20)(\d{2})-(01|02|03|04|05|06|07|08|09|10|11|12)-([0-3]\d)', value)
		if match:
			print(match)
			return datetime.date.fromisoformat(match.group())
		print(f'match not found for date: {value}')
		return value
	
	@staticmethod
	def group_or_value(pattern: re.Pattern, value: str):
		if isinstance(value, str):
			match = pattern.search(value)
			if match:
				return match.group()
		return value
	
	@staticmethod
	def group_or_none(pattern: re.Pattern, value: str):
		if isinstance(value, str):
			match = pattern.search(value)
			if match:
				return match.group()
		return None
	
	@staticmethod
	def get_year_string(value: str) -> str:
		return Regex.group_or_value(Regex.year_pattern(), value)
	
	@staticmethod
	def get_day_string(value: str) -> str:
		return Regex.group_or_value(Regex.day_pattern(), value)
	
	@staticmethod
	def get_month_string(value: str) -> str:
		return Regex.group_or_value(Regex.month_pattern(), value)
	
	@staticmethod
	def normalize(value: str) -> str:
		return unidecode(Regex.remove_extra_spaces(value))
	
	@staticmethod
	def normalize_lower(value: str) -> str:
		return Regex.normalize(value).lower()
	
	@staticmethod
	def findall_digits(value: str) -> list[str]:
		return re.findall(r'\d+[,.]\d+|\d+', value)
	
	@staticmethod
	def to_number(value: str):
		if isinstance(value, str):
			value = re.sub(r',', '.', value)
			if '.' in value:
				return float(value)
			return int(value)
		return value
	
	@staticmethod
	def extract_numbers(value: str) -> list[Union[int, float]]:
		return [Regex.to_number(item) for item in Regex.findall_digits(value)]
	
	@staticmethod
	def remove_extra_spaces(value: str) -> str:
		if isinstance(value, str):
			return re.sub(r'\s\s+', ' ', value).strip()
		return value
	
	@staticmethod
	def slug(value: str) -> str:
		return '_'.join([item.lower() for item in re.split(r'([A-Z][a-z]+)(?=[A-Z])', value) if item])
	
	@staticmethod
	def split_string_lines(value) -> list[str]:
		if isinstance(value, str):
			return [Regex.strip_string(item) for item in re.split(r'\r\n|\n', value) if item]
		return []
	
	@staticmethod
	def strip_string(value: str) -> str:
		return value.strip()
	
	@staticmethod
	def only_decimals(value: str) -> str:
		if isinstance(value, str):
			return ''.join([i for i in value if i.isdecimal()])
		return value


class Email(Regex):
	def __init__(self, data):
		super().__init__(self.remove_extra_spaces(data.lower()))
		assert '@' in self.data, self.validate_error_string
		assert len(self.data.split('@')) == 2, self.validate_error_string
		assert '.' in self.data.split('@')[-1], self.validate_error_string
	
	@property
	def validate_error_string(self):
		return f'A string "{self.data}" não corresponde a email válido.'


class CPF(Regex):
	def __init__(self, data):
		super().__init__(data)
		self.data = self.only_decimals(data)
		self.validate_error()
	
	def validate_error(self):
		if not len(self.data) == 11:
			raise ValueError(f'o valor {self.data} deve ter 11 digitos e apenas {len(self.data)} foram encontrados.')
	
	def format(self):
		return f'{self.data[:3]}.{self.data[3:6]}.{self.data[6:9]}-{self.data[9:]}'


class Phone(Regex):
	def __init__(self, data):
		super().__init__(data)
		result = ''.join([i for i in data if i.isdecimal()])
		assert (len(result) >= 9) and len(
				result) <= 13, f'o valor {data} deve ter entre 9 e 13 digitos e {len(result)} foram encontrados.'
		self.data = result
	
	def __str__(self):
		return self.format()
	
	def format(self):
		if len(self.data) == 9:
			return f'+55 (62) {self.data[:5]}-{self.data[5:]}'
		elif len(self.data) == 11:
			return f'+55 ({self.data[:2]}) {self.data[2:7]}-{self.data[7:]}'
		elif len(self.data) == 12:
			return f'+{self.data[:2]} ({self.data[2:4]}) {self.data[4:8]}-{self.data[8:]}'
		elif len(self.data) == 13:
			return f'+{self.data[:2]} ({self.data[2:4]}) {self.data[4:9]}-{self.data[9:]}'
		return self.data
