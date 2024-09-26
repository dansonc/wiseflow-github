# from openai import OpenAI

# client = OpenAI(api_key="sk-teveadihfbdlyxforitsoyjxuhcucglsjibxsnqgmhjtabnd",
#                 base_url="https://api.siliconflow.cn/v1")

# response = client.chat.completions.create(
#     model='alibaba/Qwen1.5-110B-Chat',
#     messages=[
#         {'role': 'user', 'content': '怎么赚大钱'}
#     ],
#     stream=True
# )

# for chunk in response:
#     print(chunk.choices[0].delta.content, end='')
    
from openai import OpenAI

client = OpenAI(api_key="sk-teveadihfbdlyxforitsoyjxuhcucglsjibxsnqgmhjtabnd",
                base_url="https://api.siliconflow.cn/v1")

while True:
    user_input = input("你: ")
    if user_input.lower() in ['exit', 'quit', 'q']:
        break

    response = client.chat.completions.create(
        model='Qwen/Qwen2-1.5B-Instruct',
        messages=[
            {'role': 'user', 'content': user_input}
        ],
        stream=True
    )

    print("AI: ", end='')
    for chunk in response:
        print(chunk.choices[0].delta.content, end='')
    print()  # 换行