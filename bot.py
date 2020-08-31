import discord
import random
import os
from discord.ext import commands

client = commands.Bot(command_prefix='/')
client.remove_command("help")

global Commands
Commands = False
global Shell
Shell = False

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="being silly, \"/\""))
    print("Siliness is about to begin (Bot ready)")

@client.command()
async def help(ctx, arg=""):
    if(arg == "Commands"):
        embed = discord.Embed(
            title = "Help Commands cog",
            description = "Commands cog can do this stuff.",
            colour = discord.Colour.green()
        )

        embed.add_field(name="/ping", value="responds with pong and bot's ping", inline=False)
        embed.add_field(name="/quote", value="sends one of the bot autors quotes", inline=False)
        embed.add_field(name="/clear", value="takes number of messages and deletes them plus the call.(does not check for admin yet)", inline=False)
        embed.add_field(name="/stats", value="shows how many times were commands called", inline=False)
        embed.add_field(name="/8ball", value="responds (might delete soon)", inline=False)
        embed.add_field(name="/calc", value="2 numbers +-*/ and °C to °F and reverse", inline=False)
        await ctx.send(embed=embed)
    elif(arg == "Shell"):
        embed = discord.Embed(
            title = "Help Shell cog",
            description = "Shell cog can do this stuff.",
            colour = discord.Colour.green()
        )

        embed.add_field(name="/k", value="/k ``command`` & /k cd ``folder``\nI would tell you to go ham, but plese don't", inline=False)

        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title = "Help",
            description = "Hewwo, I can do this stuff.",
            colour = discord.Colour.green()
        )

        embed.add_field(name="Built in:", value="**help** -this lovely message\n**load** -loads a cog\n**unload** -unloads cog\n**reload** -reloads cog", inline=True)
        embed.add_field(name="Commands cog:", value="**ping** -pong's\n**quote** -stuff I said\n**clear** -clears messages\n**stats** -commands stats\n**8ball** -gives reply\n**calc** -does math", inline=True)
        embed.add_field(name="Shell cog:", value="literrary Shell access the tho computer the bot is running on")
        await ctx.send(embed=embed)

@client.command()
async def load(ctx, cog="Commands"):
    global Commands
    global Shell
    if(ctx.message.author.id == 220622445927858178):
        client.load_extension(f"cogs.{cog}")
        print(f"# {cog} Cog loaded")
        if(cog == "Shell"):
            Shell = True
        elif(cog == "Commands"):
            Commands = True
        await ctx.send(f"{cog} Cog loaded")
    else:
        await ctx.send("My dev told me to not talk to stangers.")

@client.command()
async def unload(ctx, cog="Commands"):
    global Commands
    global Shell
    if(ctx.message.author.id == 220622445927858178):
        client.unload_extension(f"cogs.{cog}")
        if(cog == "Shell"):
            Shell = False
        elif(cog == "Commands"):
            Commands = False
        print(f"# {cog} Cog unloaded")
        await ctx.send(f"{cog} Cog unloaded")
    else:
        await ctx.send("My dev told me to not talk to stangers.")

@client.command()
async def reload(ctx, cog="Commands"):
    global Commands
    global Shell
    if(ctx.message.author.id == 220622445927858178):
        client.unload_extension(f"cogs.{cog}")
        client.load_extension(f"cogs.{cog}")
        if(cog == "Shell"):
            Shell = True
        elif(cog == "Commands"):
            Commands = True
        print(f"# {cog} Cog reloaded")
        await ctx.send(f"{cog} Cog reloaded")
    else:
        await ctx.send("My dev told me to not talk to stangers.")

@client.command()
async def cogs(ctx):
    global Commands
    global Shell
    await ctx.send(f"Commands = {Commands}\nShell = {Shell}")

for filename in os.listdir("./cogs"):
    if("Shell" in filename):
        pass
    else:
        if (filename.endswith(".py")):
            client.load_extension(f"cogs.{filename[:-3]}")
            if("Commands" in filename):
                Commands = True
            print(f"# {filename[:-3]} Cog loaded")

client.run('Magical key goes here')