from atlas_tutorial import AtlasChatAgent
def test_chat():
    agent = AtlasChatAgent()
    assert agent.chat("你好") == "你好呀！"