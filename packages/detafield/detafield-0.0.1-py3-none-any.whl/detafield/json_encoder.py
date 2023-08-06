from __future__ import annotations

__all__ = ['json_parse', 'json_loads', 'json_dumps']
import json
from enum import Enum
import datetime
from typing import Any
from detafield.abstracet_model import AbstractModel
from detafield.regex import Regex

class JsonEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, datetime.datetime):
			return obj.isoformat()[:16]
		elif isinstance(obj, datetime.date):
			return obj.isoformat()
		elif isinstance(obj, Enum):
			return obj.name
		elif isinstance(obj, AbstractModel):
			return obj.json()
		elif isinstance(obj, bytes):
			return obj.decode(encoding='utf-8')
		elif isinstance(obj, dict):
			return json_parse(obj)
		elif isinstance(obj, Regex):
			return str(obj)
		return json.JSONEncoder.default(self, obj)
	
	
def json_loads(obj: str) -> Any:
	return json.loads(obj)


def json_dumps(obj: Any) -> str:
	return json.dumps(obj, cls=JsonEncoder, indent=2, ensure_ascii=False)


def json_parse(obj: Any) -> Any:
	return json_loads(json_dumps(obj))