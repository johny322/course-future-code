from dotenv import load_dotenv
from os import getenv

load_dotenv()

BOT_TOKEN = getenv('TOKEN')
ADMINS = [int(admin_id) for admin_id in getenv('ADMIN_ID').split(',')]

PROVIDER_TOKEN = getenv('PROVIDER_TOKEN')
