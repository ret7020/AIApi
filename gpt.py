
import openai
from typing import List, Tuple
import os

def ask(history: List[dict], msg) -> Tuple[List[dict], str]:
    new_history = history.copy()
    new_history.append({
        "role": "user",
        "content": msg
    })
    completion = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo-16k',
        messages = new_history,
        temperature = 0.3
    )

    new_history.append({
        "role": "assistant",
        "content": completion['choices'][0]['message']['content']
    })
    return new_history, completion['choices'][0]['message']['content']


openai.api_key = os.getenv("OPENAI_TOKEN")
history = []
initial_prompt = '''Вместо ответа на вопрос о погоде, я заменяю его на !module_weather'''
history.append({
    "role": "assistant",
    "content": initial_prompt
})
while True:
    msg = input(">")
    history, ans = ask(history, msg)
    print(ans)

