import discord
from discord import app_commands
from datetime import date

server_id = 1208861813861519390 

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False 

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: 
            await tree.sync(guild = discord.Object(id=server_id)) 
            self.synced = True
        print(f"Login successfully as {self.user}.")

aclient = client()
tree = app_commands.CommandTree(aclient)
today = date.today()

@tree.command(guild = discord.Object(id=server_id), name = 'build', description='Build your executable') 
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"""
    ESSE AQ VAI BUILDA O BAGUI""", 
    ephemeral = True) 

@tree.command(guild = discord.Object(id=server_id), name = 'status', description='Get application status') 
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"""
    > :white_check_mark:  **WORKING** *(UPDATED {today.strftime("%B %d, %Y")})*""", 
    ephemeral = True) 

@tree.command(guild = discord.Object(id=server_id), name = 'buy', description='Buy now') 
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"""
    > :moneybag: *$25/Month* 
    > ***PAYPAL*** -> https://paypal.com/linkdopaypal 
    > :envelope_with_arrow:  *AFTER PAYMENT DM ANY OWNER*""", 
    ephemeral = True) 

aclient.run('MTIwODk1MDIwNTQ5NjU2NTgxMA.Gsk-Fi.TmGdhc4Wvh2YzTHCuPqHK46TL-ytZxCRIS_JhY')

