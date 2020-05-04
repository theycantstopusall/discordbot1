import discord
from discord.ext import commands
import asyncio
import time
import discord.client

client = commands.Bot(command_prefix=".")

def words():
    with open("badwords.txt", "r") as f:
        f_contents = f.read(100)

channel = ["general"]
messages = joined = 0
badwords = words()
    

@client.event
async def on_ready():
    game = "Watching you"
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("With Marks Teamspeak permissions"))
    print('hello')
    print(f'{badwords}')

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason=reason)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason=reason)
    await ctx.send(f"""ban hammer is swinging {member.name} https://tenor.com/view/ban-banned-gif-8540509""")
@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"""unbanned {user.name}""")
            return

async def update_stats():
    await client.wait_until_ready()
    global messages, joined
    while not client.is_closed():
        try:

            messages = 0
            joined = 0

            with open("stats.txt", "a") as f:
                f.write(f"""Messages: {messages}, Members Joined {joined}, time: {time.time()}\n""")
            await  asyncio.sleep(5)
        except Exception as e:
            print(e)


@client.event
async def on_member_update(before, after):
    n = after.nick
    if n:
        if n.lower().count("Crysis Wolfie") > 0:
            last = before.nick
            if last:
                await after.edit(nick=last)
            else:
                await after.edit(nick="NO STOP THAT!")


@client.event
async def on_member_update(before, after):
    n = after.game
    if n:
        if n.lower.count(f"""{before.n}""") > 0:
            discord.message.channel.send()

@client.event
async def on_message(message, yes=None):
    # chat commands
    id = client.get_guild(705455096749752323)
    channels = ["general"]
    apply = ["i-want-to-apply"]
    global messages
    messages = + 1
    await client.process_commands(message)
    if message.content.find(".hello") != -1:
        await message.channel.send(f"""What's cooking {message.author.mention} looking good today :wink:""")
    elif message.content == "!users":
        await message.channel.send(f"""Number of members {id.member_count}""")
    if message.content.find("NHS") != -1:
        await message.channel.send("https://tenor.com/view/goodjob-clap-nicework-great-gif-7248435")
    if message.content.find("mark") != -1:
        await message.channel.purge(limit=1)
        await message.channel.send("https://tenor.com/view/facepalm-really-stressed-mad-angry-gif-16109475")
    if message.content.find("Mark") != -1:
        await message.channel.purge(limit=1)
        await message.channel.send("https://tenor.com/view/facepalm-really-stressed-mad-angry-gif-16109475")
    if message.content.find("cuba") != -1:
        await message.channel.send(
            "https://tenor.com/view/sr-burns-pero-aqui-todos-somos-amigos-chico-todos-somos-amigos-amigos-castro-gif-14927106")
    elif message.content == "!ip":
        await message.channel.send("testing")
    if message.content.find("!invite") != -1:
        await message.channel.send(f"here you go mate https://discord.gg/GSjyC5z {message.author.mention}")
    if str(message.channel) in apply:
        if message.content.find("!apply") != -1:
            await message.channel.send(f"""Hi {message.author.mention}, please read the rules. once done please message a @CoC member""")


@client.event
async def on_member_update(before, after):  # needs fixing
    n = before.status
    if n != before:
        await message.channel.send(f"""have fun on {after} """)


@client.command()
async def create_invite(ctx):
    link = await ctx.channel.create_invite(max_age=300)
    await ctx.send("Here is an instant invite to your server: " + link)


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {ctx.author.mention}')

@client.command()
async def addword(ctx, reason=None):
        await ctx.send(f"""Hey! {ctx.author.mention} badword added""")
        try:
            with open("badwords.txt", "a") as b:
                b.write(f"""{reason}\n""")
                b.close()
                return
        except Exception as b:
            print(b)

client.run('TOKEN')
