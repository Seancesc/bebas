import discord
from discord.ext import commands
from mycode import gen_pass

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
async def help(ctx):
    list_command = {
        '$hello : untuk menyapa bot',
        '$generate_password : untuk membantu kamu membuat password',
        '$pangkatkan : untuk angka dipangkatkan 2',
        '$heh : untuk ketawa',
        '$on_ready : untuk lihat bot'
    }

    for i in list_command.keys:
        await ctx.send(f'{i} : {list_command[i]}')


bot.run("Masukan TOKEN")
