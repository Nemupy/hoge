import disnake
from disnake.ext import commands

intents = disnake.Intents.all()

bot = commands.Bot(command_prefix="?!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    servers = len(bot.guilds)
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1
    await bot.change_presence(
        activity=disnake.Activity(
            name=f"help | {str(servers)}servers | {str(members)}users", type=3)
    )

@bot.command()
async def expand(ctx, message: disnake.Message):
    embed = disnake.Embed(color=0x00ff00)
    embed.set_author(name=message.author.name, icon_url=message.author.avatar.url)
    embed.description = message.content
    embed.add_field(name='Channel', value=message.channel.mention)
    embed.add_field(name='Created At', value=message.created_at.strftime('%Y-%m-%d %H:%M:%S'))
    embed.add_field(name='Link', value=f'[Jump to Message]({message.jump_url})')
    for attachment in message.attachments:
        embed.set_image(url=attachment.url)
    await ctx.send(embed=embed)

bot.load_extension("cogs.welcome")


bot.run('MTA5MjAzODkxNzQ4Nzg2MTgwMA.GRv2cc.ez9Wu0FCRFDw3GKFx_z09fwccZETAyJVTUMEgw')