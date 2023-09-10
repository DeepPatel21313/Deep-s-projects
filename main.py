import discord
import random
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
played = []

answered = False
gamble_amount = [20000]
rand = random.randint(0,3)
rand1 = 0
trivia_list = []
counter=0
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    global gamble_amount, asked, answered, rand1, counter
    if message.author == client.user:
        return

    if message.content.startswith('hello') or message.content.startswith('Hello') or message.content.startswith(
            'Hi') or message.content.startswith('hi'):
        await message.channel.send('Hello')
    if message.content.startswith('wassup'):
        await message.channel.send('wassup homie')
    if message.content.startswith("image") or message.content.startswith("pfp") or message.content.startswith(
            "profile picture"):
        await message.channel.send(file=discord.File("eren.jpeg"))

    if message.content.startswith("hyaena") or message.content.startswith("music") or message.content.startswith("reset"):
        await message.channel.send(file=discord.File("Travis-Scott-HYAENA.mp3"))
        played.append("1")
    if message.content.startswith("next") and played.__contains__("1"):
        await message.channel.send(file=discord.File("Travis-Scott-FE-N.mp3"))
        played.remove("1")
        played.append("2")
        return
    if message.content.startswith("next") and played.__contains__("2"):
        await message.channel.send(file=discord.File("Travis-Scott-LOOOVE.mp3"))
        played.remove("2")
        played.append("3")
        return
    if message.content.startswith("next") and played.__contains__("3"):
        await message.channel.send(file=discord.File("Travis-Scott-MELTDOWN.mp3"))
        played.remove("3")
        played.append("4")
        return
    if message.content.startswith("next") and played.__contains__("4"):
        await message.channel.send(file=discord.File("Travis-Scott-TELEKINESIS.mp3"))
        played.remove("4")
        played.append("5")
        return
    if message.content.startswith("next") and played.__contains__("5"):
        await message.channel.send(file=discord.File("Travis-Scott-TIL-FURTHER-NOTICE.mp3"))
        played.remove("5")
        played.append("6")
        return
    if message.content.startswith("next") and played.__contains__("6"):
        await message.channel.send(file=discord.File("Travis-Scott-TOPIA-TWINS.mp3"))
        played.remove("6")
        played.append("7")
    if message.content.startswith("next") and played.__contains__("7"):
        await message.channel.send("Playlist ended, type reset to start it again")

    if message.content.startswith("balance"):
        await message.channel.send("Your new balance is")
        await message.channel.send(str(gamble_amount[0]))
        await message.channel.send("Deposit once you hit 10k or 20k for surprise")

    if message.content.startswith("gamble"):
        word_list = message.content.split()
        gamble_deposit = int(word_list[-1])
        gamble_amount[0] += random.randint(-gamble_deposit, gamble_deposit)

        if gamble_amount[0] <= 0 :
            gamble_amount[0]=0
            await message.channel.send("You are out of money")

        await message.channel.send("Your new balance is")
        await message.channel.send(str(gamble_amount[0]))


    if message.content.startswith("work"):
        gamble_amount[0]+=100
        await message.channel.send("Your new balance is")
        await message.channel.send(str(gamble_amount[0]))


    if message.content.startswith("meme"):
        rand = random.randint(0, 3)
        if rand == 0:
            await message.channel.send(file=discord.File("meme1.jpeg"))
        elif rand == 1:
            await message.channel.send(file=discord.File("meme2.jpeg"))
        else:
            await message.channel.send(file=discord.File("meme3.jpeg"))




    if message.content.startswith("diamond") and trivia_list.__contains__("0"):
        gamble_amount[0] += 1000
        await message.channel.send("Correct, you gained 1000 gamba points")
        await message.channel.send("Your new balance is")
        await message.channel.send(str(gamble_amount[0]))
        counter = 0
    if message.content.startswith("amphibian") and trivia_list.__contains__("1"):
        gamble_amount[0] += 1000
        await message.channel.send("Correct, you gained 1000 gamba points")
        await message.channel.send("Your new balance is")
        await message.channel.send(str(gamble_amount[0]))
        counter = 0
    if message.content.startswith("11") and trivia_list.__contains__("3"):
        gamble_amount[0] += 1000
        await message.channel.send("Correct, you gained 1000 gamba points")
        await message.channel.send("Your new balance is")
        await message.channel.send(str(gamble_amount[0]))
        counter = 0
    if message.content.startswith("32") and trivia_list.__contains__("2"):
        gamble_amount[0] += 1000
        await message.channel.send("Correct, you gained 1000 gamba points")
        await message.channel.send("Your new balance is")
        await message.channel.send(str(gamble_amount[0]))
        counter = 0
    if message.content.startswith("skin") and trivia_list.__contains__("4"):
        gamble_amoun[0] += 1000
        await message.channel.send("Correct, you gained 1000 gamba points")
        await message.channel.send("Your new balance is")
        await message.channel.send(str(gamble_amount[0]))
        counter = 0
    if message.content.startswith("green") and trivia_list.__contains__("5"):
        gamble_amount[0] += 1000
        await message.channel.send("Correct, you gained 1000 gamba points")
        await message.channel.send("Your new balance is")
        await message.channel.send(str(gamble_amount[0]))
        counter = 0
    if message.content.startswith("8") and trivia_list.__contains__("6"):
        gamble_amount[0] += 1000
        await message.channel.send("Correct, you gained 1000 gamba points")
        await message.channel.send("Your new balance is")
        await message.channel.send(str(gamble_amount[0]))
        counter = 0
    if message.content.startswith("honey") and trivia_list.__contains__("7"):
        gamble_amount[0] += 1000
        await message.channel.send("Correct, you gained 1000 gamba points")
        await message.channel.send("Your new balance is")
        await message.channel.send(str(gamble_amount[0]))
        counter = 0
    if message.content.startswith("cheetah") and trivia_list.__contains__("8"):
        gamble_amount[0] += 1000
        await message.channel.send("Correct, you gained 1000 gamba points")
        await message.channel.send("Your new balance is")
        await message.channel.send(str(gamble_amount[0]))
        counter = 0
    if message.content.startswith("blue") and trivia_list.__contains__("9"):
        gamble_amount[0] += 1000
        await message.channel.send("Correct, you gained 1000 gamba points")
        await message.channel.send("Your new balance is")
        await message.channel.send(str(gamble_amount[0]))
        counter = 0
    if counter==1:
        await message.channel.send("Incorrect, type trivia to try again")
        counter=0
        trivia_list.clear()


    if message.content.startswith("trivia"):
        if rand1==9:
            rand1=0
        if rand1 == 0:
            await message.channel.send("What is the hardest natural substance on Earth?")
            trivia_list.append("0")
        elif rand1 == 1:
            await message.channel.send("Frogs belong to which animal group?")
            trivia_list.append("1")
        elif rand1 == 2:
            await message.channel.send("How many teeth does an adult human have?")
            trivia_list.append("2")
        elif rand1 == 3:
            await message.channel.send("How many players in a football match")
            trivia_list.append("3")
        elif rand1 == 4:
            await message.channel.send("What is the largest organ?")
            trivia_list.append("4")
        elif rand1 == 5:
            await message.channel.send("What is the color of an emerald?")
            trivia_list.append("5")
        elif rand1 == 6:
            await message.channel.send("How many planets are in our solar system?")
            trivia_list.append("6")
        elif rand1 == 7:
            await message.channel.send("What do bees make?")
            trivia_list.append("7")
        elif rand1 == 8:
            await message.channel.send("Which is the fastest land animal?")
            trivia_list.append("8")
        elif rand1 == 9:
            await message.channel.send("What color are Smurfs?")
            trivia_list.append("9")
        rand1 += 1
        counter+=1

    if gamble_amount[0] > 20000 and message.content.startswith("deposit"):
        await  message.channel.send(file=discord.File("pepe2.png"))
        return
    if gamble_amount[0] > 10000 and message.content.startswith("deposit"):
        await message.channel.send(file=discord.File("pepe1.png"))

    if message.content.startswith("help"):
        await message.channel.send("Commands are below")
        await message.channel.send("trivia\n"
                                   "gamble Xamount\n"
                                   "deposit\n"
                                   "meme\n"
                                   "work\n"
                                   "balance\n"
                                   "Hello/hi/wassup\n"
                                   "music\n"
                                   "image/pfp\n"
                                   "next\n"
                                   "reset")

client.run("")
