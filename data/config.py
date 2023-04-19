import os
import sys
from pathlib import Path

if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.absolute()

else:
    ROOT_DIR = Path(__file__).parent.parent.absolute()

FILES_DIR = os.path.join(ROOT_DIR, 'files')

TEMP_DB = os.path.join(FILES_DIR, 'temp.db')

ERRORS_FILE = os.path.join(FILES_DIR, 'errors.log')

RESULTS_FILE = os.path.join(FILES_DIR, 'results.xlsx')
PROXIES_FILE = os.path.join(FILES_DIR, 'proxies.txt')
SETTINGS_FILE = os.path.join(FILES_DIR, 'settings.json')
