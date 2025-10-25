
from pathlib import Path
import json

VERSION = '0.0.2'
CREATOR = 'groknut'
URL = 'https://github.com/groknut/kerge'
SETTINGS_FILE = 'settings.json'

parent = Path(__file__).parent
settings_path = Path(SETTINGS_FILE)

def get_project_info():
	return {
		'version': VERSION,
		'creator': CREATOR,
		'url': URL
	}

def load_data():
    if settings_path.exists():
        with open(settings_path, mode='r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    return { 'baud': 15000000 }
    

def save(data):
    with open(settings_path, mode='w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
