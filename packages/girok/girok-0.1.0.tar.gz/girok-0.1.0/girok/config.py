from functools import lru_cache
import typer
from pathlib import Path
import girok.utils.general as general_utils


class Config:
    def __init__(self):
        self.config = general_utils.read_json('girok/config.json')
        self.base_url = self.config['base_url']
        self.app_name = self.config['app_name']
        self.app_dir = typer.get_app_dir(self.app_name)
        self.config_path: Path = Path(self.app_dir) / "config.json"
        
        
@lru_cache()
def get_config():
    return Config()
        
        