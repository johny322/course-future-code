from dotenv import load_dotenv
from os import getenv

load_dotenv()

BOT_TOKEN = getenv('TOKEN')
# ADMINS = [int(getenv('ADMIN_ID'))]
ADMINS = [int(admin_id) for admin_id in getenv('ADMIN_ID').split(',')]
channels = [-1001645078625]  # Список каналов
