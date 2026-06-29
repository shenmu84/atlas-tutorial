import argparse#导入命令行参数解析模块，用于处理用户运行程序时传入的参数
import sys
import atlas_tutorial  #从包中导入版本号（在__init__.py中定义）
from atlas_tutorial.chat_agent import AtlasChatAgent

'''
如果删除它,Agent 还能在 Python 中调用，但不能通过命令行启动
'''
def main()->int:
    __version__ = atlas_tutorial.__version__
    parser=argparse.ArgumentParser(
        prog="atlas",#程序名称，显示帮助时使用
        description="Atals AI Agent",
    )
    #添加基本参数
    #action="version"这是一个特殊动作，当用户输入--version时直接显示版本号并退出
    parser.add_argument("--version",action="version",version=__version__)
    parser.add_argument("--name",default="Atlas",help="Agent名字")
    #创建子命令
    #子命令的名称将保存在args.command中
    subparsers=parser.add_subparsers(dest="command")
    #添加chat子命令
    chat_p=subparsers.add_parser("chat",help="对话模式")
    
    #创建AtlasChatAgent实例，传入name参数（用户可通过--name指定）
    args=parser.parse_args()
    if args.command=="chat":
        agent=AtlasChatAgent(name=args.name)
        agent.run()
        return 0
    #如果用户没有提供任何子命令，显示帮助信息
    parser.print_help()
    return 1

#检查是否直接运行此文件（而不是被导入）
if __name__=="__main__":
    sys.exit(main())#调用main函数，并用其返回值作为程序退出码