import discord
from discord.ext import commands
from jokes import father
import random
from discord.ext.commands import has_permissions

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def clear(ctx, amount=2):
    amount += 1
    await ctx.channel.purge(limit=amount)

@client.command()
async def prefix(ctx):
    await ctx.send(f"Hello")

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def echo(ctx, arg):
    await ctx.send(arg)

@client.command()
@has_permissions(manage_roles=True)
async def announce(ctx, message):
    channel = client.get_channel(730196954432274452)
    await channel.send(message)

@client.command()
async def ping(ctx, member : discord.Member):
    hello = str(member.id)
    hello1 = "<@" + hello + ">"
    await ctx.send(f"PONG {hello1}")

@client.command()
@has_permissions(kick_members=True)
async def warn(ctx, member : discord.Member, *, reason=None):
    hello = str(member.id)
    hello1 = "<@" + hello + ">"
    sentence = "Warned " + hello1 + " for " + reason
    await ctx.send(sentence)

@client.command()
async def dadjoke(ctx):
    joke = random.choice(father)
    await ctx.send(joke)

@client.command()
async def report(ctx, member : discord.Member, *, reason=None, amount=1):
    hello = str(member.id)
    hello1 = "<@" + hello + ">"
    await ctx.channel.purge(limit=amount)
    report_message = "Successfully reported"
    await ctx.send(report_message)
    channel = client.get_channel(730228978987565076)
    username = str(ctx.author.id)
    username1 = "<@" + username + ">"
    await channel.send("Reported sent by " + username1 + " against " + hello1 + " for:\n" + "``" + reason + "``")

@client.command()
async def ticket(ctx, reason):
    username = ctx.message.author.name
    username1  = str(ctx.message.author.id)
    username2 = "<@" + username1 + ">"
    name = "tickets"
    category = discord.utils.get(ctx.guild.categories, name=name)
    guild = ctx.message.guild
    channel = await ctx.guild.create_text_channel(username, category=category)
    await channel.send("Ticket send by: " + username2 + "\n" + "``" + reason + "``")

@client.command()
async def newticket (ctx, reason):
    username1 = str(ctx.message.author.id)
    username2 = "<@" + username1 + ">"
    with open("tickets.csv", "a") as f:
        f.write(f"{username2},{reason}\n")
    await ctx.send("We have recieved your ticket!")

@client.command()
@has_permissions(kick_members=True)
async def tickets(ctx):
    searchfile = open("tickets.csv", "r")
    for line in searchfile:
        await ctx.send(line)
    searcfile.close()

@client.command()
@has_permissions(kick_members=True)
async def tdelete(ctx):
    file = open("tickets.csv", "r+")
    file.truncate(0)
    file.close()
    await ctx.send("Tickets have been deleted!")

client.run("")
