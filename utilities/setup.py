import yaml

def load_config():
    with open('./env/config.yaml', 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config
