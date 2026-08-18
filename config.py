import json
import os

class ConfigLoader:
    def __init__(self, config_file='config.json', defaults=None):
        self.config_file = config_file
        self.defaults = defaults or {}
        self.config = self.load_config()

    def load_config(self):
        if not os.path.isfile(self.config_file):
            return self.defaults
        with open(self.config_file, 'r') as file:
            try:
                config_data = json.load(file)
            except json.JSONDecodeError:
                return self.defaults
        return {**self.defaults, **config_data}

    def get(self, key, default=None):
        return self.config.get(key, default)

if __name__ == '__main__':
    defaults = {
        'API_URL': 'https://api.example.com',
        'TIMEOUT': 30
    }
    config_loader = ConfigLoader(defaults=defaults)
    print(config_loader.get('API_URL'))
    print(config_loader.get('UNKNOWN_KEY', 'default_value'))