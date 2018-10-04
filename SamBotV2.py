#SambotV2 made for sam johnson

import discord
import asyncio
import time
import random

from discord.ext import commands
from discord.ext.commands import Bot
from config import config_dict


bot = commands.Bot(command_prefix = config_dict["prefix"])
bot.remove_command('help')


@bot.event
async def on_ready():
    print('Watashi ga kita! // I am here!')
#####
#if you uncomment these two commands, be aware that the clear command will echo the deleted messages back into chat,
#either change it to print not say the deleted messages or comment out the deleted message entirely
#####
# #display sent messages in log
# @bot.event
# async def on_message(message):
#     author = message.author
#     content = message.content
#     print('{}: {}'.format(author, content))
#     await bot.process_commands(message) #this is needed at the end of on_message events to enable commands to run
# #display deleted messages in log (only works on message bot was online to see)
# @bot.event
# async def on_message_delete(message):
#     author = message.author
#     content = message.content
#     channel = message.channel
#     await bot.send_message(channel, '{}: {}'.format(author, content))
#     await bot.process_commands(message) #this is needed at the end of on_message events to enable commands to run

#ping pong
@bot.command()
async def ping():
    await bot.say('Pong!')
#marco polo
@bot.command()
async def marco():
    await bot.say('Polo!')

#echo command
@bot.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await bot.say(output)

#deletes messages (default 100) from channel
@bot.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount+1)): #add 1 so that it deletes your clear command and then the number of messages wanted, may cause issues if amount goes above 100
        messages.append(message)
    await bot.delete_messages(messages)
    await bot.say(str(amount) + " messages deleted") 

#####
#embed commands
#####
@bot.command(pass_context=True)
async def displayembed(ctx):
    #this name here is used in the embed.set below ie name.set etc
    #command is prefixdisplayembed where prefix is your predix and embed is the name set here
    channel = ctx.message.channel
    embed = discord.Embed(
        title = 'Title',
        description = 'This is a description',
        colour = discord.Colour.blue()

    )
#you can leave the url empty it just wont display is all
    embed.set_footer(text='This is a footer.')
    embed.set_image(url='')
    embed.set_thumbnail(url='')
    embed.set_author(name='Author name', icon_url='')
    embed.add_field(name='Field Name', value='Field Value', inline=False)
    embed.add_field(name='Field Name', value='Field Value', inline=True)
    embed.add_field(name='Field Name', value='Field Value', inline=True)
#add as many fields as you like
#i mean, it might break at some point but who knows
    #await bot.say(embed=embed)
    await bot.say.send_message(channel, embed=embed)
#pick one or the other

#####
#help commands
#####
@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    help = discord.Embed(
        colour = discord.Colour.orange()

    )
    help.set_author(name='Help')
    help.add_field(name='s!ping', value='Returns Pong!', inline=False)

    await bot.send_message(author, embed=help)
    await bot.say("@" + str(author) + " I send you a PM with the basic commands")

bot.run(config_dict["token"])
