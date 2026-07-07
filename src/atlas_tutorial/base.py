'''Base Agent
这个文件负责：定义所有 Agent 都应该具有哪些能力。
谁调用它：没有人直接使用。继承它。
它调用：调用子类实现的对话方法

'''
from abc import ABC,abstractmethod
from typing import List,Optional
from dataclasses import dataclass
@dataclass
class Message:
    role:str
    content:str
class BaseAgent(ABC):
    '''所有Atlas Agent的基类'''
    VERSION="1.0"
    def __init__(self,name:str="Atlas"):
        self.name=name
        self.memory:List[Message]=[]
    @abstractmethod
    def chat(self,user_input:str)->str:
        pass

    def add_message(self,role:str,content:str)->None:
        self.memory.append(Message(role=role,content=content))
    
    def run(self)->None:
        print(f"{self.name}启动")
        while True:
            user_input=input("你:").strip()
            if not user_input or user_input in ("exit","再见"):
                print(f"{self.name}:再见")
                break
            #调用子类实现的对话方法（因为这里是抽象方法）
            reply=self.chat(user_input)
            print(f"{self.name}:{reply}")
