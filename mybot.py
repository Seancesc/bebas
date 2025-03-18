import discord
from discord.ext import commands
from mycode import gen_pass
import random, os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def generate_password(ctx):
    await ctx.send('ini password untukmu:')
    await ctx.send(gen_pass(12))

@bot.command()
async def pangkatkan(ctx):
    await ctx.send('coba kirim angka yang ingin dipangkatkan')
    angka = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    angka = int(angka.content)

    await ctx.send('berikut pangkat dua dari {angka}')
    await ctx.send(angka**2)

@bot.command()
async def help_me(ctx):
    list_command = {
        '$hello : untuk menyapa bot',
        '$generate_password : untuk membantu kamu membuat password',
        '$pangkatkan : untuk angka dipangkatkan 2',
        '$heh : untuk ketawa',
        '$on_ready : untuk lihat bot'
    }

    for i in list_command.keys:
        await ctx.send(f'{i} : {list_command[i]}')

@bot.command()
async def send_meme(ctx):
    folder = os.listdir('gambar_meme')
    img = random.choice(folder)
    direktori = f'gambar_meme/{img}'
    with open(direktori, 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def animals(ctx):
    folder = os.listdir('gambar_animals')
    img = random.choice(folder)
    direktori = f'gambar_animals/{img}'
    with open(direktori, 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

organik = ["daun","sayur","kulit pisang ambon"]
anorganik = ['plastik', 'besi', 'kabel']

@bot.command()
async def pilih(ctx):
    await ctx.send('Masukan sampah')
    msg = await bot.wait_for("message")
    if msg.content in organik:
        await ctx.send("Masukan dalam organik")
    elif msg.content in anorganik:
        await ctx.send("Masukan dalam anorganik")

bot.run("MASUKAN TOKEN")
