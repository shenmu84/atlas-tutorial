import logging
import sys
from pathlib import Path

def setup_logging(level:str="INFO",log_file:str=None):
    #配置日志
    formatter=logging.Formatter(
       " %(asctime)s[%(levelname)s]%(name)s:%(message)s",
       datefmt="%Y-%m-%d %H:%M:%S"
    )
    #创建一个“控制台输出器”，日志会打印到屏幕（stdout）
    console=logging.StreamHandler(sys.stdout)
    console.setFormatter(formatter)
    #获取“根日志器”（全局日志系统的主入口）。
    root=logging.getLogger()
    root.setLevel(getattr(logging,level.upper()))
    #把控制台输出器挂到日志系统
    #让日志系统知道：以后产生的日志，要通过这个 console 输出
    root.addHandler(console)
    if log_file:
        Path(log_file).parent.mkdir(parents=True,exist_ok=True)
        file_handler=logging.FileHandler(log_file,encoding="utf-8")
        file_handler.setFormatter(formatter)

        root.addHandler(file_handler)
#创建“当前这个文件专属的日志记录器”
logger=logging.getLogger(__name__)

class AtlasAgent:
    VERSION="1.9"

    def __init__(self,name="Atlas"):
        self.name=name
        logger.info(f"Atlas{self.VERSION}初始化：name={name}")

    def chat(self,user_input:str)->str:
        logger.debug(f"chat")
        intent = self.classify(user_input)
        logger.info(f"intent={intent}, input={user_input!r}")
        
        reply = self.generate_reply(intent, user_input)
        
        logger.debug(f"reply={reply!r}")
        return reply
    
    def classify(self, text: str) -> str:
        if not text:
            logger.warning("空输入")
            return "empty"
        if "你好" in text:
            return "greeting"
        if "再见" in text:
            return "farewell"
        return "unknown"
    
    def generate_reply(self, intent, text):
        replies = {
            "greeting": "你好呀",
            "farewell": "再见",
            "empty": "请说话",
            "unknown": f"我听到了 {text}",
        }
        return replies.get(intent, "未知")
if __name__=="__main__":
        setup_logging(level="DEBUG",log_file="atlas.log")
        agent=AtlasAgent()
        agent.chat("你好")
        agent.chat("")
        agent.chat("Python")