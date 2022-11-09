import os
import yaml
import addict

_default_config = {
    'log': {
        'filename': 'evmautomation.log', 
        'level': 'WARNING'
        }
    }

class AttrDict(addict.Dict):
    def __missing__(self, name):
        if object.__getattribute__(self, '__frozen'):
            raise KeyError(name)
        
        return None

        
class Config:
    def __init__(self, config=None):
        self.config = AttrDict(_default_config)
        self.log_msg = ""
        if isinstance(config, str):
            if config and os.path.exists(config):
                with open(config) as fp:
                    self.config = AttrDict(yaml.safe_load(fp))
                    self.log_msg = f'Config: use file={config!r} containing the following main keys: {", ".join(self.config.keys())}'
            else:
                self.log_msg = f'Config: no file={config!r} => default config.'
        elif isinstance(config, dict):
            self.config = AttrDict(config)
            self.log_msg = f'Config: use dict containing the following main keys: {", ".join(self.config.keys())}'
        elif isinstance(config, Config):
            self.config = AttrDict(config.config)
            self.log_msg = f'Config: using Config containing the following main keys: {", ".join(self.config.keys())}'
        elif os.environ.get('EVM_AUTOMATION_CONFIG') and os.path.exists(os.environ.get('EVM_AUTOMATION_CONFIG')):
            config = os.environ.get('EVM_AUTOMATION_CONFIG')
            with open(config) as fp:
                self.config = AttrDict(yaml.safe_load(fp))
                self.log_msg = f'Config: use file={config!r} from EVM_AUTOMATION_CONFIG containing the following main keys: {", ".join(self.config.keys())}'
        else:
            self.log_msg = f'Config: Only accept str and dict but got {type(config)!r} => default config.'

    def __bool__(self):
        return self.config != {}

    def __getattr__(self, attr):
        return self.config[attr]

    def __getitem__(self, key):
        return self.config[key]

    def __contains__(self, item):
        return item in self.config

    def __repr__(self) -> str:
        return self.config.__repr__()