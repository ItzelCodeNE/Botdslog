from dotenv import load_dotenv, dotenv_values
import discord
from discord.ext import commands
import os 
import time

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='$',intents=discord.Intents.all())
LOG_DIR = 'Servidores'

#@bot.event
#async def on_guild_join(guild):
R = "Servidores"
if not os.path.exists(R):
    os.mkdir(R)
else:
    print("La carpeta ya existe.")


def ReturnRoles(guild): 
    roles = guild.roles
    roles_list = [role.name for role in roles]
    return roles_list

def ReturnChannels(guild): 
    channels = guild.channels
    channels_list = [channel.name for channel in channels]
    return channels_list

def Returncategories(guild):
    categories = guild.categories
    print(categories)

@bot.event
async def on_ready():
    start_time = time.time()
   
    for guild in bot.guilds:
        ruta_guild = os.path.join(R, guild.name)
        os.makedirs(ruta_guild, exist_ok=True)
        for Cat in guild.categories:
            ruta_cat = os.path.join(ruta_guild, Cat.name)
            os.makedirs(ruta_cat, exist_ok=True)  
            for channel in Cat.channels:
                ruta_channel = os.path.join(ruta_cat, channel.name)               
                if not os.path.exists(ruta_channel): 
                    with open(ruta_channel + ".txt", 'w',encoding='utf-8') as A:
                        async for message in channel.history(limit=1000):
                            A.write(f'{message.created_at.strftime("%d/%m/%Y %H:%M")} | {message.author}: {message.content}\n')
    end_time = time.time()
    elapsed_time = end_time - start_time        
    print(f'Bot inciado en {elapsed_time:.2f} segundos')        
        
@bot.command(name='ReturnRolesCom') 
async def ReturnRolesCom(ctx):
    roles = ReturnRoles(ctx.guild)
    print(roles)

@bot.command(name='ReturnChannelsCom')
async def ReturnChannelsCom(ctx):
    channels = ReturnChannels(ctx.guild)
    print(channels)


@bot.command(name='ReturnCategoriesCom') 
async def ReturnCategoriesCom(ctx):
    Categories = Returncategories(ctx.guild)
    print(Categories)



    







    
    




bot.run(TOKEN)