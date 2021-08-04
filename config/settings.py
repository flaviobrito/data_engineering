from pathlib import Path
import os
DEBUG = False
base_path = Path(__file__).parent.parent
config_path = base_path / "config"
dotenv_path = config_path / '.env.dev'
data_path = base_path / "data" / "requests"
databse_local_dir = base_path / "db"
doc_path = base_path / "docs"
image_path = doc_path / "images"
DB_DRIVER = 'postgresql+psycopg2://'
from dotenv import load_dotenv
load_dotenv(dotenv_path)

DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')