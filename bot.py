import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import os
import youtube_dl

client = commands.Bot(command_prefix='>')

urls = {
    "rwayak": "https://youtu.be/3nPrRUV7L4o",
    "tnayekwahdek": "https://youtu.be/vUWn2Dh3o6c",
    "ebeedzebi": "https://youtu.be/LuVb5mFL-3s",
    "tetmanyek": "https://youtu.be/2TpSjkgfoJI"
}

OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll',
             'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
        try:
            opus.load_opus(opus_lib)
            return
        except OSError:
            pass

        raise RuntimeError('Could not load an opus lib. Tried %s' %
                           (', '.join(opus_libs)))


# @client.event
# async def on_message(message):
#    voicechannel = message.author.voice.channel
#    if not voicechannel == None and message.author.id == 356558972607791115:
#        await message.channel.send("OOO ti haw Deli lahne tlaa ya zebi houwa mahsoub rabi rao khlakni ya zab")


@client.event
async def on_ready():
    print('bot is ready')


@client.event
async def on_member_join(member):
    print(f'(member) joina w walla kahboun')


@client.event
async def on_member_remove(member):
    print(f'(member)khraj yaatih aasba')


@client.command()
async def aasba(ctx, target: discord.Member):
    await ctx.send("yaatek aasba ya " + target.mention + "!")


@client.command(aliases=["assbaenh ", "aasbaa"])
async def aasbaenh(ctx, target: discord.Member):
    await ctx.send('yaatek aasba ala sormek ya!' + target.mention)


@client.command()
async def nhebnalaab(ctx):
    await ctx.send('@everyone ya malhet chkn yalaab')


@client.command()
async def nawarna(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send("haw jit!")


@client.command()
async def okhrejnayek(ctx):
    await ctx.voice_client.disconnect()
    await ctx.send("maadch kdar f hel bled")


@client.command()
async def jomlaop(ctx, place):
    await ctx.send("O wras rabek manji " + place+" o kadrek namsah bih sorm omek li tneket meno mn shtar rjel touns")


@client.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx, url: str):

    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("ERROR: Music playing")
        return

    await ctx.send("nsakhen f darbouka haw jek")

    voice = get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"),
               after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit("-", 2)
    print("playing\n")


@client.command(pass_context=True)
async def bsout(ctx, vid):
    url = urls[vid]
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("ERROR: Music playing")
        return

    voice = get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"),
               after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit("-", 2)
    print("playing\n")

client.run('NzY5MzAyOTY3ODAzMTgzMTI0.X5NDOA.BlB4R8IEEmCgQNOWcy9ml1EN5Dk')
