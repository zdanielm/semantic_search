# Semantic Search project for "Geometric Data Analysis"

## Installation:
### 1. Install requirements:
```shell
pip install -r requirements.txt
```

### 2. Config
- create a `env` folder and inside it, a `config.yaml`

## Tested Models:
| Name | Link | Embedding Dimension | Elapsed Time For Embedding The Chunks of 1000 Texts |
|:----:|:----:|:-------------------:|:---------------------------------------------------:|
| ***MiniLM L6 v2*** | https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 | 384 | 0:17:00 |
| ***Snowflake Arctic Embed M*** | https://huggingface.co/Snowflake/snowflake-arctic-embed-m | 768 | 1:37:00 |
| Snowflake Arctic Embed S | https://huggingface.co/Snowflake/snowflake-arctic-embed-s | 384 | 0:35:00 |
| ModernBERT Embed Base | https://huggingface.co/nomic-ai/modernbert-embed-base | 768 | 2:36:00 |
