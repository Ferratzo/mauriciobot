import discord
from discord.ext import commands
import variables
import random as rnd
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
client = commands.Bot(command_prefix='m!')

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
@client.event
async def on_ready():
    print("El bot está listo")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="pickear mid y perder awp"))

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
@client.command()
async def say(ctx, *, arg):
    await ctx.send(arg)

@client.command()
async def fb(ctx):
    await ctx.send("¿Te jode que sea un fuckboy? Pues no es mi problema tiro mi cigarro y lo piso para apagarlo aunque nunca lo encendí. Estoy jodido, lo sé, tengo mierda en la cabeza y me gusta engañar a las chicas, enamorarlas, coger con ellas y luego bloquearlas de mis contactos, es lo que yo hago miro a otro lado con poco interés No podrás cambiarme aunque quieras, nena me paro frente tuyo y me muerdo el labio, así que....no te enamores de mí, porque te follaré y luego me iré, porque soy un fuckboy empiezo a caminar lejos de ti, por cierto... fumo y drogo, también ando en skate, no soy tu príncipe azul salgo caminando como todo un fuckboy")

#\\\\\\\\\\\\\\\\Echar gente\\\\\\\\\\\\\\\\\\\\\\\\\\
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):
    await member.kick()
    await ctx.send(f"{member} ha sido kickeado por malo")

#\\\\\\\\\\\\\\\\Primer embed\\\\\\\\\\\\\\\\\\\\\\\\\\
@client.command()
async def awp(ctx):
    r = rnd.randrange(1, 3)
    if r == 1:
        embedvar = discord.Embed(
            title="CISTERNAS PERDIÓ LA AWP EN MID",
            description="OH NOOOOOOOOOOOOOOO!!",
            color=0x00ff00
        )
        embedvar.set_image(
            url="https://media3.giphy.com/media/MFaIycChwBrAYViWdQ/200.gif"
        )
    #||||||||||||||||||||||||||
    elif r == 2:
        embedvar = discord.Embed(
            title="**CISTERNAS ABRIÓ MID CON AWP**",
            description="QUE PROPLAYER!",
            color=0x00ff00
        )
        embedvar.set_image(
            url="https://media1.giphy.com/media/jtj4HbLNbjCOfvPRnv/200w.gif?cid=82a1493bwvcze4iu74rcxevq8zwgmrza7etxlp5c50a5xpd2&rid=200w.gif"
        )
    await ctx.send(embed=embedvar)

#\\\\\\\\\\\\TOSCOSSSSS\\\\\\\\\\\\\\\\\

@client.command()
async def pasar(ctx):
    r = rnd.randrange(1, 4)
    if r == 1:
        embedvar = discord.Embed(
            title="**RENATO Y CISTERNAS TOSQUEARON A TODOS**",
            description="GG, LOS MATARON A LOS DOS, EN UN CUMPLE",
            color=0000000
        )
        embedvar.set_image(
            url="https://i.makeagif.com/media/9-29-2015/qF5Db0.gif"
        )
    elif r == 2:
        embedvar = discord.Embed(
            title="**PASÓ CISTERNAS SOLO :O**",
            description="Lo tasearon... :(",
            color=00000000
        )
        embedvar.set_image(
            url="https://thumbs.gfycat.com/LiquidFastHawk-max-1mb.gif"
        )
    elif r == 3:
        embedvar = discord.Embed(
            title="**PASÓ TODO EL TEAM**",
            description="INCRÍVEL",
            color=000000000
        )
        embedvar.set_image(
            url="https://steamuserimages-a.akamaihd.net/ugc/943936969959877708/8BDA726FDA64903869A3BD87AAA257934959B848/"
        )
    await ctx.send(embed=embedvar)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
@client.command()
async def random(ctx):
    embedvar = discord.Embed(
        Title="**IMAGEN RANDOM"
    )
    embedvar.set_image(
        url="https://imgur.com/random"
    )
    await ctx.send(embed=embedvar)

#\\\\\\\\\\\\\\\\\Latencia\\\\\\\\\\\\\\\\\\\\\\\\\\\\
@client.command(name="ping", description="Muestra la latencia")
async def ping(ctx):
    if client.latency * 1000 >= 70:
        await ctx.send(f"**VTR CULIAO! :face_with_symbols_over_mouth: :face_with_symbols_over_mouth: :face_with_symbols_over_mouth:  MIRAAAA TENGO {round(client.latency * 1000)}ms**")
    else:
        await ctx.send(f"**Piola, tengo solo {round(client.latency * 1000)}ms**")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Música

client.run(variables.token)