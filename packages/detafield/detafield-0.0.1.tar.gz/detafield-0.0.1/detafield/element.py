from dataclasses import dataclass, field
from typing import ClassVar, Optional, Deque, Union, Literal
from collections import deque, defaultdict
from abc import ABC, abstractmethod
from enum import Enum
import re

EMPTY: list[str] = ['input', 'img', 'meta', 'link', 'br', 'hr']
STRUCTURE: list[str] = ['html', 'head', 'body', 'title']
SEMANTIC: list[str] = ['header', 'footer', 'main', 'aside', 'nav']
FORM_FIELDS: list[str] = ['input', 'select', 'textarea']

TAGS: list[str] = [
		'a', 'address', 'area', 'abbr', 'article', 'aside', 'audio', 'body',
		'b', 'base', 'bdi', 'bdo', 'blockquote', 'br', 'button', 'canvas', 'caption', 'cite', 'code', 'col', 'colgroup',
		'data', 'datalist', 'dd', 'del', 'details', 'dfn', 'div', 'dialog', 'dl', 'dt', 'em', 'embed', 'fieldset',
		'figcaption', 'figure', 'footer', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'head', 'header', 'hr', 'html',
		'i', 'iframe', 'img', 'input', 'ins', 'kbd', 'label', 'legend', 'li', 'link', 'main', 'map', 'mark', 'meta',
		'meter', 'nav', 'nonscript', 'object', 'ol', 'optgroup', 'output', 'p', 'param', 'picture', 'pre', 'progress',
		'q', 'rp', 'rt', 'ruby', 's', 'samp', 'script', 'section', 'select', 'small', 'source', 'span', 'strong',
		'style', 'sub', 'summary', 'sup', 'svg', 'table', 'tbody', 'td', 'template', 'textarea', 'tfoot', 'th',
		'thead', 'time', 'title', 'tr', 'track', 'u', 'ul', 'var', 'video', 'wbr'
]

INPUT_TYPES: list[str] = [
		'button', 'checkbox', 'color', 'date', 'datetime-local', 'email', 'file', 'hidden', 'image', 'month',
		'number', 'password', 'radio', 'range', 'reset', 'search', 'submit', 'tel', 'text', 'time', 'url', 'week'
]

EXCLUDE_KWARGS: list[str] = ['label', 'floating', 'group', 'fieldset', 'order', 'default']


class HTMLTag(Enum):
	_ignore_ = 'HTMLTag i'
	HTMLTag = vars()
	for i in TAGS:
		HTMLTag[f'{i}'.upper()] = i


class InputType(Enum):
	_ignore_ = 'InputType i'
	InputType = vars()
	for i in INPUT_TYPES:
		InputType[f'{i}'.upper().replace("-", "_")] = i
	
	def input_bootstrap(self):
		if self.value == 'checkbox':
			return 'form-check-input'
		elif self.value == 'color':
			return 'form-control form-control-color'
		elif self.value == 'range':
			return 'form-range'
		return 'form-control'
	
	def label_bootstrap(self):
		if self.value == 'checkbox':
			return f'form-check-label'
		return 'form-label'


class Element(ABC):
	
	def __init__(self, tag, *args, **kwargs):
		self.enum_tag = HTMLTag(tag)
		self.args = args
		self.kwargs = kwargs
		self.text = self.kwargs.pop('text', None)
		self.children = self.make_deque(self.kwargs.pop('children', None))
		self.style = self.make_deque(self.kwargs.pop('style', None))
		self.after = self.make_deque(self.kwargs.pop('after', None))
		self.before = self.make_deque(self.kwargs.pop('before', None))
		self.parent = None
	
	@classmethod
	def make_deque(cls, value):
		if value is None:
			return deque([])
		elif isinstance(value, list):
			return deque(value)
		else:
			return deque([value])
	
	def __str__(self):
		return re.sub(r'\s>', '>', re.sub(r'\s\s+', ' ', self.render))
	
	@property
	def tag(self):
		if self.enum_tag:
			return self.enum_tag.value
		return type(self).__name__.lower()
	
	@property
	def id(self):
		return self.kwargs.get('id', None)
	
	@property
	def value(self):
		return self.kwargs.get('value', None)
	
	@property
	def default(self):
		return self.kwargs.get('default', None)
	
	@property
	def input_type(self):
		if self.is_input:
			return InputType(self.kwargs.get('type', 'text'))
		return None
	
	@property
	def klass(self):
		return self.kwargs.get('klass', None)
	
	@property
	def is_required(self):
		return 'required' in self.args
	
	@property
	def is_readonly(self):
		return 'readonly' in self.args
	
	@property
	def is_disabled(self):
		return 'disabled' in self.args
	
	@property
	def is_select(self):
		return self.tag == 'select'
	
	@property
	def is_textarea(self):
		return self.tag == 'textarea'
	
	@property
	def is_input(self):
		return self.tag == 'input'
	
	@property
	def is_form(self):
		return self.tag == 'form'
	
	@property
	def is_form_element(self):
		if self.is_input or self.is_select or self.is_textarea:
			return True
		return False
	
	def add_style(self, value: str):
		self.style.append(value)
	
	def add_kwargs(self, **kwargs):
		self.kwargs.update(kwargs)
	
	def add_args(self, value: str):
		self.args.append(value)
	
	def append(self, element: Union['Element', str]):
		self.children.append(element)
	
	def prepend(self, element: Union['Element', str]):
		self.children.appendleft(element)
	
	def append_after(self, element: Union['Element', str]):
		self.after.append(element)
	
	def prepend_after(self, element: Union['Element', str]):
		self.after.appendleft(element)
	
	def append_before(self, element: Union['Element', str]):
		self.before.append(element)
	
	def prepend_before(self, element: Union['Element', str]):
		self.before.appendleft(element)
	
	def make_parent(self, *args, **kwargs):
		kwargs['children'] = [self]
		self.parent = Element(*args, **kwargs)
	
	@property
	def render_style(self):
		if self.style:
			return 'style="{}"'.format('; '.join(self.style))
		return ''
	
	@property
	def render_args(self):
		return ' '.join(self.args)
	
	@property
	def render_kwargs(self):
		return ' '.join([
				f'{key.replace("_", "-")}="{val}"'
				for key, val in self.kwargs.items()
				if not key in EXCLUDE_KWARGS if val is not None
		]).replace('klass', ' class').replace('for-id', 'for')
	
	@property
	def render_children(self):
		if not self.text:
			return ''.join([str(item) for item in self.children])
		return '{}{}'.format(self.text, ''.join([str(item) for item in self.children]))
	
	@property
	def render_after(self):
		return ''.join([str(item) for item in self.after])
	
	@property
	def render_before(self):
		return ''.join([str(item) for item in self.before])
	
	@property
	def config(self):
		return '{} {} {}'.format(self.render_kwargs, self.render_args, self.render_style)
	
	@property
	def render(self):
		if self.tag in EMPTY:
			return f'{self.render_before}<{self.tag} {self.config}>{self.render_after}'
		return f'{self.render_before}<{self.tag} {self.config}>{self.render_children}</{self.tag}>{self.render_after}'


class HTML(ABC):
	
	def __str__(self):
		return str(self.element)
	
	@property
	@abstractmethod
	def element(self):
		return NotImplemented


class Ul(HTML):
	items: list[Element, str] = field(default_factory=list)
	
	@property
	def element(self):
		return Element(
				'ul',
				klass='list-group',
				children=[Element('li', klass='list-group-item', text=str(item)) for item in self.items]
		)


@dataclass
class FormField(HTML):
	form_element: Element
	
	def __post_init__(self):
		self.set_name()
		if not self.form_element.klass:
			self.form_element.add_kwargs(klass=self.form_element_class)
	
	@property
	def input_type(self):
		return self.form_element.input_type
	
	def set_name(self):
		self.form_element.add_kwargs(name=self.form_element.id)
	
	@property
	def label(self):
		return self.form_element.kwargs.get('label', self.form_element.kwargs.get('id'))
	
	@property
	def is_floating(self):
		return self.form_element.kwargs.pop('floating', True)
	
	@property
	def form_element_class(self):
		if self.form_element.is_select:
			return 'form-select'
		elif self.form_element.is_textarea:
			return 'form-control'
		elif self.input_type:
			return self.input_type.input_bootstrap()
	
	def setup_input(self):
		self.form_element.add_kwargs(klass=self.input_type.input_bootstrap())
	
	def setup_select(self):
		self.form_element.add_kwargs(klass='form-select')
	
	@property
	def element(self):
		if self.input_type:
			if self.input_type.value == 'checkbox':
				if self.form_element.default:
					self.form_element.add_kwargs(value='on')
				return Element('div', klass='form-check', children=[self.form_element, self.label_element])
			if self.input_type.value == 'range':
				self.form_element.append_before(self.label_element)
				return self.form_element
		if self.is_floating:
			self.form_element.add_kwargs(placeholder=self.label)
			return Element('div', klass='form-floating mb-3', children=[self.form_element, self.label_element])
		return Element('div', klass='mb-3', children=[self.form_element, self.label_element])
	
	@property
	def label_element(self):
		return Element(
				'label',
				for_id=self.form_element.kwargs.get('id', self.form_element.kwargs.get('name', None)),
				text=self.form_element.kwargs.pop('label', self.form_element.kwargs.get('id')),
				klass=self.input_type.label_bootstrap()
		)


@dataclass
class Form(HTML):
	id: str = None
	action: str = None
	method: Literal['get', 'post'] = 'get'
	form_elements: list[Element] = field(default_factory=list)
	fieldset_list: list[Element] = field(default_factory=list, init=False)
	grouped_list: list[Element] = field(default_factory=list, init=False)
	general_list: list[Element] = field(default_factory=list, init=False)
	
	def __post_init__(self):
		self.set_fieldsets()
		self.set_groups()
	
	def set_fieldsets(self):
		groups = [(item.kwargs.get('fieldset', ''), item) for item in self.form_elements]
		d = defaultdict(list)
		for k, v in groups:
			if k:
				d[k].append(v)
			else:
				self.general_list.append(v)
		self.fieldset_list = [self.make_fieldset(*item) for item in sorted(d.items())]
	
	@staticmethod
	def make_fieldset(name: str, items: list[Element]):
		return Element('fieldset', children=[Element('legend', text=name), *[FormField(item) for item in items]])
	
	def make_group(self, group: int, items: list[Element]):
		return Element(
				'div',
				klass='input-group',
				id='{}-input-group-{}'.format(self.id, str(group)),
				children=[FormField(item) for item in items]
		)
	
	def set_groups(self):
		groups = [(item.kwargs.get('group', None), item) for item in self.general_list]
		d = defaultdict(list)
		for k, v in groups:
			if k:
				d[k].append(v)
				self.general_list.remove(v)
		self.grouped_list = [self.make_group(*item) for item in sorted(d.items())]
	
	@property
	def element(self):
		return Element(
				'form',
				id=self.id,
				action=self.action,
				method=self.method,
				children=[
						*[FormField(item) for item in self.general_list],
						*self.fieldset_list,
						*self.grouped_list
				]
		)


@dataclass
class Document(HTML):
	BOOTSTRAP_STYLE: ClassVar[str] = '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.' \
	                                 'bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h' \
	                                 '455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>'
	BOOTSTRAP_SCRIPT: ClassVar[str] = '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.' \
	                                  'min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80z' \
	                                  'W1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">'
	
	title: str
	body: list[Union[Element, str]] = field(default_factory=list)
	head: list[Union[Element, str]] = field(default_factory=list)
	
	@property
	def head_tags(self):
		return [
				Element('title', text=self.title),
				Element('meta', charset='utf-8'),
				Element('meta', name='viewport', content="width=device-width, initial-scale=1"),
				self.BOOTSTRAP_STYLE,
				*self.head
		]
	
	@property
	def element(self):
		self.body.append(self.BOOTSTRAP_SCRIPT)
		return Element(
				'html',
				lang='pt-BR',
				before='<!DOCTYPE html>',
				children=[
						Element('head', children=self.head_tags),
						Element('body', children=self.body)
				]
		)


if __name__ == '__main__':
	f = Form('new-patient', '/patient/new', form_elements=[
			Element('input', id='bdate', type='date', label='nascimento', group=1),
			Element('input', 'required', id='fname', type='text', label='primeiro nome', fieldset='Nome',
			        value='daniel'),
			Element('input', 'required', id='sname', type='text', label='segundo nome', fieldset='Nome'),
			Element('input', 'required', id='size', type='range', label='tamanho', group=3),
			Element('input', 'required', id='weight', type='range', label='peso', group=2),
	
	])
	x = Document('pagina inicial',
	             [
			             Element('h3', text='Novo Paciente'),
			             f.element],
	             )
