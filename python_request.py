import requests
from dotenv import dotenv_values

env_vars = dotenv_values(".env")

AZURE_OPENAI_KEY = env_vars["AZURE_OPENAI_KEY"]
AZURE_OPENAI_ENDPOINT = env_vars["AZURE_OPENAI_ENDPOINT"]
DEPLOYMENT_NAME = env_vars["DEPLOYMENT_NAME"]

url = f"{AZURE_OPENAI_ENDPOINT}"

headers = {"Content-Type": "application/json", "api-key": f"{AZURE_OPENAI_KEY}"}

data = {
    "messages": [
        {
            "role": "system",
            "content": "あなたは優秀なアシスタントです。ユーザーからの質問に丁寧な日本語で答えてください。",
        },
        {"role": "user", "content": "金太郎の物語について教えてください"},
    ]
}

response = requests.request("POST", url, headers=headers, json=data)
print(response.json()["choices"][0]["message"]["content"])
