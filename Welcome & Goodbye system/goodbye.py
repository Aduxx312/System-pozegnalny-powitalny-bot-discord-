import discord

async def send_goodbye_message(channel, member):
    embed = discord.Embed(
        title="Pa!", 
        description=f" {member.mention} Mamy nadzieje ze do nas wrocisz!", 
        color=discord.Color(0x00008B)  
    )
    embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
    await channel.send(embed=embed)
