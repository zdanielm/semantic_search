# Semantic Search project for "Geometric Data Analysis"

## Installation:
### 1. Install requirements:
Create a virtual environment:
```shell
python3 -m venv .venv
source .venv/bin/activate
```
```shell
pip install -r requirements.txt
```

### 2. Config
- create a `env` folder and inside it, a `config.yaml` and add the following fields (remove placeholders with specific values):
```yaml
database: text_db    # Specifies database name
host: localhost    # Specifies PostgreSQL database URL
port: 5432    # Specifies the port the database is accessible from
user: postgres    # Username
password: postgres    # Provided user's password
openai_api_key: APIKEY    # OpenAI API key (only needed for TruLens evaluation)
```

## Tested Models:
| Name | Link | Embedding Dimension | Elapsed Time For Embedding The Chunks of 1000 Texts |
|:----:|:----:|:-------------------:|:---------------------------------------------------:|
| ***MiniLM L6 v2*** | https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 | 384 | 0:17:00 |
| ***Snowflake Arctic Embed M*** | https://huggingface.co/Snowflake/snowflake-arctic-embed-m | 768 | 1:37:00 |
