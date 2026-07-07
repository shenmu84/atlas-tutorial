'''chat agent'''
#导入类型提示工具
from typing import List
from atlas_tutorial.base import BaseAgent,Message
class AtlasChatAgent(BaseAgent):
    '''通用对话Agent'''
    #分析处理用户的输入，并对其做出回复，保存在消息界面中
    def classify_intent(self,text:str)->str:
        text=text.strip().lower()
        if not text:
            return "empty"
        for kw in ["你好", "hello", "hi"]:
            if kw in text:
                return "greeting"
        for kw in ["再见", "bye", "exit"]:
            if kw in text:
                return "farewell"
        if "?" in text or "？" in text:
            return "question"
        return "unknown"
    def chat(self, user_input: str) -> str:
        intent = self.classify_intent(user_input)
        replies = {
            "greeting": "你好呀！",
            "farewell": "下次见～",
            "question": "好问题",
            "empty": "请说话",
            "unknown": f"我听到了 '{user_input}'",
        }
        reply=replies.get(intent,"未知")
        self.add_message("user",user_input)
        self.add_message("assistant",reply)
        return reply
    