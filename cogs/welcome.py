import disnake
from disnake.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        guild_name = member.guild.name
        member_count = guild.member_count
        embed = disnake.Embed(
            title=f"ようこそ！{guild_name}へ！",
            description=f"{member.mention}さんが入室しました。 \nあなたは{str(member_count)}人目のユーザーです。",
            color=0x3498DB,
        )
        embed.set_thumbnail(url=member.avatar.url)
        await member.guild.system_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        embed = disnake.Embed(
            title="また来てね！",
            description=f"{member.mention}さんが退室しました。", 
            color=0x3498DB
        )
        embed.set_thumbnail(url=member.avatar.url)
        await member.guild.system_channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Welcome(bot))