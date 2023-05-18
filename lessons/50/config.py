from dotenv import load_dotenv
from os import getenv

load_dotenv()

BOT_TOKEN = getenv('TOKEN')
ADMINS = [int(admin_id) for admin_id in getenv('ADMIN_ID').split(',')]

Y_TOKEN = getenv('Y_TOKEN')
# 1111 1111 1111 1026, 12/22, CVC 000
