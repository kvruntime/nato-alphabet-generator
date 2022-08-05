from dotenv import load_dotenv, find_dotenv
import os
from pathlib import Path
load_dotenv(find_dotenv())


NATO_RESSOURCE = Path(str(os.getenv("NATO_RESSOURCE"))).resolve()
