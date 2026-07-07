"""Atlas调试示例"""

def classify_intent(text):
    breakpoint()  # 进入pdb
    if not text:
        return "empty"
    if "你好" in text:
        return "greeting"
    return "unknown"

def main():
    user_input = "你好"
    intent = classify_intent(user_input)
    print(f"意图: {intent}")

if __name__ == "__main__":
    main()