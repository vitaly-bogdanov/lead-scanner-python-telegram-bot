import os

API_TOKEN = os.environ.get("API_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

IP = os.environ.get("IP")
PGUSER = os.environ.get("PGUSER")
PGPASSWORD = os.environ.get("PGPASSWORD")
DB_HOST = IP
DATABASE = os.environ.get("DATABASE")
POSTGRES_URL = f"postgresql://{PGUSER}:{PGPASSWORD}@{DB_HOST}/{DATABASE}"
CHAT_ID = -1001573784593

CHATS = []
KEYWORDS = []
