'''
它告诉 Python：
当别人
import atlas_tutorial
的时候，
这个包里面有哪些东西可以直接使用。
'''
__version__="1.0.0"
from atlas_tutorial.base import BaseAgent
from atlas_tutorial.chat_agent import AtlasChatAgent
__all__=["BaseAgent","AtlasChatAgent","__version__"]
