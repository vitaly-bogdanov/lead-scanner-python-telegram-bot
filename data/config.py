from environs import Env

env = Env()
env.read_env()
API_TOKEN = env.str("API_TOKEN")
API_ID = env.str("API_ID")
API_HASH = env.str("API_HASH")

IP = env.str("IP")
PGUSER = env.str("PGUSER")
PGPASSWORD = env.str("PGPASSWORD")
DB_HOST = IP
DATABASE = env.str("DATABASE")
POSTGRES_URL = f"postgresql://{PGUSER}:{PGPASSWORD}@{DB_HOST}/{DATABASE}"
CHAT_ID = -552814269

CHATS = []
KEYWORDS = []
