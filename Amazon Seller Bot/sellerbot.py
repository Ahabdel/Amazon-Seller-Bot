import discord
from discord.ext import commands
import sqlite3



# Intents for the Discord bot

intents = discord.Intents.default()
intents.messages = True  # Allows the bot to read messages
intents.guilds = True
intents.message_content = True  # Important for reading message content



# Initialize the bot with the '/' command prefix

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Function to create a database and initialize the table

def create_database():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS sellers
                 (seller_id TEXT PRIMARY KEY, channel_id TEXT, seller_name TEXT)''')
    conn.commit()
    conn.close()





# Function to add a seller to the database



def add_seller_to_db(seller_id, channel_id, seller_name):
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute('INSERT OR REPLACE INTO sellers (seller_id, channel_id, seller_name) VALUES (?, ?, ?)',
              (seller_id, channel_id, seller_name))
    conn.commit()
    conn.close()



# Function to get sellers from the database



def get_sellers():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute('SELECT * FROM sellers')
    sellers = c.fetchall()
    conn.close()
    return sellers




# Event when the bot is ready


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    create_database()  # Create the database when the bot is ready




# Hello command


@bot.command()
async def hello(ctx):
    await ctx.send('Hello there!')




# Command to add a seller


@bot.command()
async def add_seller(ctx, seller_id, seller_name):
    channel_id = str(ctx.channel.id)
    add_seller_to_db(seller_id, channel_id, seller_name)
    await ctx.send(f"Seller '{seller_name}' with ID {seller_id} added to channel {channel_id}")




# Run the bot with your token

bot_token = '' 
bot.run('')
