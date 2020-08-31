import discord
import random
from discord.ext import commands
from kolreq import n
import os

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Commands
    #=====SHELL=====#
    @commands.command()
    async def k(self, ctx, *, cmd):
        print(f"Shell_k: \"{cmd}\"")
        if(cmd[:2] == "cd"):
            os.chdir(cmd[3:])
            await ctx.send(f"```lua\n{cmd}\n```") 
        else:
            lol = os.popen(cmd).read()
            if(len(lol) > 1000):
                o = []
                while lol:
                    o.append(lol[:1000])
                    lol = lol[1000:]
                j=1   
                for i in o:
                    await ctx.send(f"Part {j}```lua\n{i}\n```") 
                    j=j+1
            else:
                if(lol == ""):
                    lol = "No output :3"
                await ctx.send(f"```lua\n{lol}\n```")  

def setup(client):
    client.add_cog(Commands(client))