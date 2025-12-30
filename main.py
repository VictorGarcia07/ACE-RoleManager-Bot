import os
import discord
from discord.ext import commands
from flask import Flask, request
import json
import logging
import asyncio
import threading
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get('BOT_TOKEN')
WEBHOOK_SECRET = os.environ.get('WEBHOOK_SECRET')
GUILD_ID = int(os.environ.get('GUILD_ID', '0'))

PRODUCT_TO_ROLE = {
      '8087': 'Single-Course', '7648': 'Single-Course', '7640': 'Single-Course',
      '7635': 'Single-Course', '7630': 'Single-Course', '7625': 'Single-Course',
      '7620': 'Single-Course', '7615': 'Single-Course', '7610': 'Single-Course',
      '7602': 'Single-Course', '7599': 'Single-Course', '7595': 'Single-Course',
      '7588': 'Single-Course', '7583': 'Single-Course', '6424': 'Single-Course',
      'd471f5fb-0f48-4f9d-97f4-95638ef57dac': 'Miembro-Club-ACE',
}

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
bot = commands.Bot(command_prefix='!', intents=intents)

app = Flask(__name__)

@bot.event
async def on_ready():
      logger.info(f'✅ Bot: {bot.user}')

@app.route('/webhook', methods=['POST'])
def webhook():
      try:
                if request.headers.get('X-Webhook-Secret') != WEBHOOK_SECRET:
                              return {'error': 'Unauthorized'}, 401

                data = request.get_json()
                if data.get('event') == 'purchase_completed':
                              product_id = str(data.get('product_id'))
                              role_name = PRODUCT_TO_ROLE.get(product_id)
                              if role_name:
                                                asyncio.create_task(assign_role(data.get('user_email'), role_name))

                          return {'status': 'ok'}, 200
except Exception as e:
        logger.error(f'Error: {e}')
        return {'error': str(e)}, 500

async def assign_role(user_email, role_name):
      guild = bot.get_guild(GUILD_ID)
      if not guild:
                return
            role = discord.utils.get(guild.roles, name=role_name)
    if not role:
              return
          for member in guild.members:
                    if hasattr(member, 'email') and member.email == user_email:
                                  await member.add_roles(role)
                                  logger.info(f'✅ {role_name} assigned')
                                  return

            if __name__ == '__main__':
                  threading.Thread(target=lambda: app.run(host='0.0.0.0', port=5000), daemon=True).start()
                  bot.run(BOT_TOKEN)
