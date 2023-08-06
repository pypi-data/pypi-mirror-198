__all__ = ['Env']

import os
from starlette.config import Config



class Env(Config):
	def __init__(self, env_prefix: str = ''):
		super().__init__(env_file=os.path.join(os.getcwd(), '.env'), environ=os.environ, env_prefix=env_prefix)
