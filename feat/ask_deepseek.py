import requests


def ask_deepseek(API_KEY: str, API_URL: str, prompt: str) -> str:
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        "model": "deepseek/deepseek-chat:free",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(API_URL, json = data, headers = headers)

    if response.status_code == 200:
        response = response.json()
        return response['choices'][0]['message']['content']
    else:
        return "Falha ao buscar dados da API. Código de status:", response.status_code