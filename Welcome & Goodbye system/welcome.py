import discord


async def send_welcome_message(channel, member):
    guild = member.guild
    member_count = len(guild.members)
    embed = discord.Embed(
        title="Witaj!", 
        description=f"{member.mention} jestes {member_count}. osoba na tym serwerze!", 
        color=discord.Color(0x00008B) 
    )
    embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
    await channel.send(embed=embed)
