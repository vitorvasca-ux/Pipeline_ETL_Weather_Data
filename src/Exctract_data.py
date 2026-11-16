
import requests
import json
from pathlib import Path

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

api_key = '86b853ea3379a166487f7c22c3cbc157'

url = f'https://api.openweathermap.org/data/2.5/weather?q=Sao Paulo,BR&units=metric&appid={api_key}'


def extract_weather_data(url: str) -> list:
    print("FUNÇÃO INICIADA")

    response = requests.get(url)

    print("STATUS:", response.status_code)
    print("RESPOSTA:", repr(response.text))

    data = response.json()

    if response.status_code != 200:
        logging.error("Erro na requisição")
        return []

    if not data:
        logging.warning("Nenhum dado retornado")
        return []

    project_dir = Path(__file__).resolve().parent.parent
    output_dir = project_dir / 'data'
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / 'weather_data.json'

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    logging.info(f"Arquivo salvo em {output_path}")

    return data


extract_weather_data(url)
