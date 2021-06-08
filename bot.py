from discord.ext import commands
import random
from riotwatcher import LolWatcher
file = open("RIOT_TOKEN.txt", "r")
CODE = file.read()
   

lol_watcher = LolWatcher(CODE)
MY_REGION = 'na1'

bot = commands.Bot(command_prefix='!')
@bot.command(name="idea")
async def idea(ctx) :
    await ctx.send("Ideas are hard")
    await ctx.send("Worry not, I think you should ...")
    topics = ['chat bot', 'cli', 'game','web bot','browser extention','api','web interface']
    areas = ['note taking', 'social life', 'physical fitness', 'mental health', 'pet care']
    language = ['java','C','C++','HTML','Python']

    rando = f'Create a new {random.choice(topics)} that helps with {random.choice(areas)} with {random.choice(language)} ! :slight_smile:'
    await ctx.send(rando)



@bot.command(name = "opgg")
async def opgg(ctx, name) :
    await ctx.send('https://na.op.gg/summoner/userName=' + name)

@bot.command(name = "champion")
async def champion(ctx) :
    str = "Aatrox Ahri Akali Alistar Amumu Anivia Annie Ashe Azir Blitzcrank Brand Braum Caitlyn Cassiopeia Cho'Gath Corki Darius Diana DrMundo Draven Elise Evelynn Ezreal Fiddlesticks Fiora Fizz Galio Gangplank Garen Gnar Gragas Graves Hecarim Heimerdinger Irelia Janna Jarvan IV Jax Jayce Jinx Kalista Karma Karthus Kassadin Katarina Kayle Kennen Kha'Zix Kog'Maw LeBlanc LeeSin Leona Lissandra Lucian Lulu Lux Malphite Malzahar Maokai MasterYi MissFortune Mordekaiser Morgana Nami Nasus Nautilus Nidalee Nocturne Nunu Olaf Orianna Pantheon Poppy Quinn Rammus Rek'Sai Renekton Rengar Riven Rumble Ryze Sejuani Shaco Shen Shyvana Singed Sion Sivir Skarner Sona Soraka Swain Syndra Talon Taric Teemo Thresh Tristana Trundle Tryndamere TwistedFate Twitch Udyr Urgot Varus Vayne Veigar Vel'Koz Vi Viktor Vladimir Volibear Warwick Wukong Xerath XinZhao Yasuo Yorick Zac Zed Ziggs Zilean Zyra"
    arr = str.split()
    idea = f'You should play {random.choice(arr)}'
    await ctx.send(idea)

@bot.command(name = "ranked")
async def ranked(ctx, id) :
    me = lol_watcher.summoner.by_name(MY_REGION, id)
    my_ranked_stats = lol_watcher.league.by_summoner(MY_REGION, me['id'])
    tier = my_ranked_stats[0]['tier']
    rank = my_ranked_stats[0]['rank']

    await ctx.send(tier + ' '+ rank)
@bot.command(name = "wr")
async def wr(ctx, id):
    me = lol_watcher.summoner.by_name(MY_REGION, id)
    my_ranked_stats = lol_watcher.league.by_summoner(MY_REGION, me['id'])
    win = int(my_ranked_stats[0]['wins'])
    loss = int(my_ranked_stats[0]['losses'])
    rate = int((win/(win + loss)) * 100)
    if rate > 50 :
        await ctx.send(str(rate) + "%  GGEZ")
    else:
        await ctx.send(str(rate) + "%  ff 15")


with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)
