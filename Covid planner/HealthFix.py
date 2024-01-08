import discord
import cases
import smm

client = discord.Client()

with open('token.env', 'r') as tokenFile:
    token = tokenFile.read()

@client.event
async def on_ready():
    print("Bot is Ready")


def sendHelp():
    help_title = 'How I work'

    helpmessage = f'''Enter query after \'MedHelp\' and I will respond
    \nExample:
    \n> MedHelp Covid
    > Response: {cases.gov()[3]} cases as of {cases.gov()[0]} from {cases.gov()[4]}

    Other queries:

    > MedHelp Workplace SMM
    > Response: {smm.workplace()}

    > MedHelp Updates
    > Response: {smm.govupdate()}
    '''

    return help_title, helpmessage



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('<@!947335354162217030>'):
        title, helpmessage = sendHelp()
        await message.channel.send(embed = discord.Embed(title = title, description = helpmessage))

    prefix = message.content[:7]
    query = message.content[8:]

    if prefix == 'MedHelp':

        if query.lower() == 'workplace smm':
            response = smm.workplace()

        elif query.lower() == 'updates':
            response = smm.govupdate()

        elif query.lower() == 'covid':
            response = f'{cases.gov()[3]} cases as of {cases.gov()[0]} from {cases.gov()[4]}'

        await message.channel.send(content = response)
        return

    else:
        return

client.run(token)
