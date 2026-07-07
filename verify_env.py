"""验证python环境"""
import sys
def check_python():
	print(f"python版本:{sys.version}")
	assert sys.version_info >= (3, 11), "需要Python 3.11+"


def check_packages():
	"""检查关键包"""
	required=[
	"openai",
	"langchain",
        "chromadb",
        "tiktoken",
        "httpx",
    ]
      
	for pkg in required:
		try:
			__import__(pkg)
			print(f"✅ {pkg}")
		except ImportError:
			print(f"❌ {pkg} 未安装")

def check_env_vars():
    """检查环境变量"""
    from dotenv import load_dotenv
    load_dotenv()
    
    import os
    optional_vars = ["OPENAI_API_KEY", "ANTHROPIC_API_KEY", "LANGCHAIN_API_KEY"]
    
    for var in optional_vars:
        val = os.environ.get(var)
        if val:
            print(f"✅ {var}: {val[:8]}...")
        else:
            print(f"⚠️  {var}: 未设置")

if __name__ == "__main__":
    check_python()
    print()
    check_packages()
    print()
    check_env_vars()