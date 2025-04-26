# 文件: 主程序.py

import json
import random

def 加载配置(路径):
    with open(路径, 'r', encoding='utf-8') as 文件:
        return json.load(文件)

def 简易推理(输入文本, 配置):
    关键词 = 配置.get("关键词", [])
    响应 = 配置.get("响应", "未找到响应。")
    
    if any(词 in 输入文本 for 词 in 关键词):
        return random.choice(响应)
    else:
        return "抱歉，我不理解你的请求。"

if __name__ == "__main__":
    配置 = 加载配置('config.json')
    
    while True:
        用户输入 = input("请输入您的问题（输入'退出'结束）：")
        if 用户输入.strip() == "退出":
            print("感谢您的使用！")
            break
        答复 = 简易推理(用户输入, 配置)
        print(f"答复: {答复}")
