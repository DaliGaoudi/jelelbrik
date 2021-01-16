import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import os
import youtube_dl
import json


client = commands.Bot(command_prefix='>')

main2 = ["rwayak", "tnayekwahdek"]

url2 = ["https://youtu.be/3nPrRUV7L4o", "https://youtu.be/vUWn2Dh3o6c"]

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


queue = []


# def reopen():
#    savefile = open("backup.json", "r")
#    main2 = json.loads(savefile.read())

#   savefile0 = open("backup0.json", "r")
#  url = json.loads(savefile0.read())

def reopen():
    with open('output.txt', 'r') as f:
        main2 = f.read().split('\n')

    with open('output2.txt', 'r') as f2:
        url2 = f2.read().split('\n')


@client.command()
async def thakafni(ctx, video, url: str):
    main2.append(video)
    url2.append(url)

    with open('output.txt', 'w') as f:
        for item in main2:
            f.write(str(item)+'\n')

    with open('output2.txt', 'w') as f2:
        for item2 in url2:
            f2.write(str(item2)+'\n')
    reopen()

# @client.command()
# async def thakafni(ctx, video, url: str):
#    main2.append(video)
    # url2.append(url)
    #savefile = open("backup.json", "w")
   # savefile.write(json.dumps(main2))

  #  savefile0 = open("backup0.json", "w")
 #   savefile0.write(json.dumps(url2))
#    reopen()


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
async def ghani(ctx, url: str):
    queue.append(url)
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("old file tfassakh")
    except PermissionError:
        print("l file yetkra tnajamch tfassakh")
        await ctx.send("famma ghne")
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
        for i in queue:
            print("Downloading audio now\n")
            ydl.download([i])

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
    indexx = main2.index(vid)
    url = url2[indexx]
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
    voice.source.volume = 0.1

    nname = name.rsplit("-", 2)
    print("playing\n")

client.run('NzY5MzAyOTY3ODAzMTgzMTI0.X5NDOA.BlB4R8IEEmCgQNOWcy9ml1EN5Dk')
