from dotenv import load_dotenv
from os import getenv

load_dotenv()

TOKEN = getenv('TOKEN')
ADMIN_ID = getenv('ADMIN_ID')

block_users = []
