import discord
import random
from discord.ext import commands
from kolreq import n

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client
        global p #ping
        p = 0
        global c #calk
        c = 0
        global b #8ball
        b = 0
        global q #quotes
        q = 0

    #Commands
    #=====PING=====#
    @commands.command(aliases=['p'])
    async def ping(self, ctx):
        global p
        p = p + 1
        print(f"ping {p}")
        await ctx.send(f"pong! {round(self.client.latency * 1000)}ms")

    #=====
    @commands.command(aliases=['q'])
    async def quote(self, ctx):
        global q
        q = q + 1
        print(f"quote {q}")
        responces = [
            'He make a silly sence, that makes no face.', 
            'If he was ever than he is forever', 
            'You need patience to go fast.', 
            'MOTHER DUCKIE',
            'Sucking up on all those dildos.',
            'Snapseed, more like Snapfeet.',
            'What is object doing when noone sees is it even issing?',
            'One day a little boy LEFT 4 STUDIES!',
            'Hey listen up here is the story about a little bass witch was droppedon the head,\nAnd now the bass it fucking stupid (bass drop)'
        ]
        await ctx.send(f"{random.choice(responces)}")

    #=====CLEAR=====#
    @commands.command()
    async def clear(self, ctx, amount=10):
        print(f"clear {c}")
        await ctx.channel.purge(limit=amount+1)

    #=====STATS=====#
    @commands.command()
    async def stats(self, ctx):
        embed = discord.Embed(
            title = "Status",
            description = f"Commands ran since last start:\n**ping:** {p}times\n**quote:** {q}times\n**8ball:** {b}times\n**calk:** {c}times",
            colour = discord.Colour.green()
        )
        await ctx.send(embed=embed)

    #=====8BALL=====#
    @commands.command(aliases=['8ball', '8Ball','b'])
    async def _8ball(self, ctx, *, question=""):
        global b
        b = b + 1
        print(f"8ball {b}")
        responces = ['lol.', 'why?', 'no', 'sure']
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responces)}")
        
    #=====CALC=====#
    @commands.command(aliases=['c', 'kalk'])
    async def calc(self, ctx, *, math):
        global c
        c = c + 1
        print(f"calc {c}")
        if("°F" in math):
            num = math[:-2]
            num = float(num)
            res = (5/9)*(num-32)
            res = str(n(res))+"°C"
        elif("°C" in math):
            num = math[:-2]
            num = float(num)
            res = (num*1.8)+32
            res = str(n(res))+"°F"
        elif("+" in math):
            num = math.split("+")
            num[0] = float(num[0])
            num[1] = float(num[1])
            res = num[0] + num[1]
        elif("-" in math):
            num = math.split("-")
            num[0] = float(num[0])
            num[1] = float(num[1])
            res = num[0] - num[1]
        elif("*" in math):
            num = math.split("*")
            num[0] = float(num[0])
            num[1] = float(num[1])
            res = num[0] * num[1]
        elif("/" in math):
            num = math.split("/")
            num[0] = float(num[0])
            num[1] = float(num[1])
            if(num[1] == 0):
                res = "Can't divide by 0"
            else:
                res = num[0] / num[1]
        await ctx.send(f"{n(res)}") 

def setup(client):
    client.add_cog(Commands(client))