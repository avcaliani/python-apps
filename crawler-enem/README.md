# 🕷️ Crawler Enem

![License](https://img.shields.io/github/license/avcaliani/crawler-enem?logo=apache&color=lightseagreen)
![#](https://img.shields.io/badge/python-^3.8.x-3776AB.svg?logo=python&logoColor=white)
![#](https://img.shields.io/badge/spark-3.3.0-E25A1C.svg?logo=apache-spark&logoColor=white)

## 🛫 Quick Start

Create your Python virtual environment...

```bash
# 👇 Setting PyEnv version
pyenv local 3.10.4

# 👇 Virtual Environment
python -m venv .venv \
  && source .venv/bin/activate \
  && pip install --upgrade pip

# 👇 Dependencies
poetry install
```

Extract files from Enem website.

```bash
docker-compose exec cluster /app/main.py \
  extract-files \
  --url "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem"
```

Save them into a Database.

```bash
docker-compose exec cluster spark-submit /app/main.py \
  export-data --from 2017 --to 2021
```
