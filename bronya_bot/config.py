import os
from  dotenv import load_dotenv

load_dotenv(".env.prod")
LOCALSTORE_DATA_DIR = os.getenv("LOCALSTORE_DATA_DIR")
