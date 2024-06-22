import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # Enable the members intent

# Bot token
TOKEN = 'MTI1NDA0OTc4NTU2OTA4MzU3Mw.GioR7k.AOIaxes6gDFw68Ik6BIYAThqK19sveLxy_UpOA'

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    print(f'{member.name} has joined the server.')
    guild = member.guild
    admin_role_name = "Admin"  # Admin role name

    # Find the admin role
    admin_role = discord.utils.get(guild.roles, name=admin_role_name)
    if not admin_role:
        print(f'Role "{admin_role_name}" not found in guild "{guild.name}".')
        return

    # Create a new text channel with the member's name
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        member: discord.PermissionOverwrite(read_messages=True),
        admin_role: discord.PermissionOverwrite(read_messages=True)
    }

    # Format channel name with 🎫 and Discord username
    channel_name = f'🎫┃{member.display_name}'
    try:
        channel = await guild.create_text_channel(channel_name, overwrites=overwrites)
        print(f'Created channel {channel_name} for {member.display_name}')

        # Send welcome message with embedded content
        welcome_message = (
            f"Welcome {member.mention}, {admin_role.mention} will be with you shortly. "
            "In the meantime please read all the information below."
        )
        embed = discord.Embed(
            title="TikTok Organic Mastery",
            description=(
                "Thank you for your interest in TikTok Organic Mastery.\n\n"
                "Here, you will learn exactly how to build a profitable TikTok organic marketing strategy.\n\n"
                "TikTok Organic Mastery is led by Jan and Aniela, experts in TikTok marketing. "
                "They guide you through videos, live sessions, expert guest talks, and exclusive events on mastering TikTok organically.\n\n"
                "If you have any questions or would like to get started, let us know below by responding in this ticket!"
            ),
            color=discord.Color.green()  # You can change the color here
        )
        embed.set_footer(text="This message is automated.")
        await channel.send(welcome_message, embed=embed)

    except Exception as e:
        print(f'Failed to create channel: {e}')

@bot.event
async def on_member_remove(member):
    print(f'{member.name} has left the server.')
    guild = member.guild

    # Find the channel associated with the member
    channel_name = f'🎫┃{member.display_name}'
    channel = discord.utils.get(guild.channels, name=channel_name)

    if channel:
        await channel.delete()
        print(f'Deleted channel {channel_name}')

# Run the bot
bot.run(TOKEN)
