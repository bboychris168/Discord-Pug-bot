import asyncio
import discord
import myToken
import random
import requests
from aiodathost.aiodathost import dathost


#loads of vars we'll need to persist
client = discord.Client()
ourServer = None
inProgress = False
readyUsers = []
firstCaptain = None
secondCaptain = None
teamOne = []
teamTwo = []
currentPickingCaptain = ""
pickNum = 1
team1VoiceChannel = None
team2VoiceChannel = None
serverName = myToken.guildID

#dathost = dathost(username=myToken.datHostUser, password=myToken.datHostPass)
dathost = dathost(username="", password="")

@client.event
async def on_ready():
    global ourServer
    global team1VoiceChannel
    global team2VoiceChannel
    
    team1VoiceChannel = client.get_channel(myToken.team1ChannelId)
    team2VoiceChannel = client.get_channel(myToken.team2ChannelId)
    await client.change_presence(status=discord.Status.online, activity=discord.Game(".r in 💥ready-room💥")) 
    print('------')    
    print('Logged in as {} with id {}'.format(client.user.name, client.user.id))
    print('VC1 Name is {}\nVC2 Name is {}'.format(team1VoiceChannel, team2VoiceChannel))
    print('------')    
    #loop over all the servers the bots apart
    

@client.event
async def on_message(message):
    #we received a message
    #modifying these globals
    global inProgress
    global readyUsers
    global firstCaptain
    global secondCaptain
    global teamOne
    global teamTwo
    global pickNum
    

    #extract the author from the message
    author = message.author

    #make sure they're using the bot setup channel
    #if(message.channel.id != myToken.setupChannelId):
    if (message.channel.name != "💥ready-room💥" and message.content.lower() == ".r"):
        embed = discord.Embed(description="**Please use the**" "💥ready-room💥" "**channel!**", color=0x03f0fc)
        await message.channel.send(embed=embed)
        await message.delete(delay=0) 
        #if they aren't using an appropriate channel, return
        return

    #ready command
    if (message.content == '!gaben' or message.content.lower() == '.r') and inProgress == False and len(readyUsers) < 10:        
        #check if they are already ready
        #if (False):    #use this line to test full flow of the bot.
        if(author in readyUsers):   #comment out this line to test full flow of the bot.
            embed = discord.Embed(description=author.mention + "**You're already ready!**", color=0xff0000)
            await message.channel.send(embed=embed)
            await message.delete(delay=0)
            
            return
        #actually readying up
        else:
            #add them to the ready list and send a message
            readyUsers.append(author)
            if(len(readyUsers) == 8 or len(readyUsers) == 9):
                embed = discord.Embed(description="<@&" + str(myToken.csRoleID) + ">" + " **we only need** " + str(10 - len(readyUsers)) + " `.r` **to join**", color=0x03f0fc)
                await message.channel.send(embed=embed)
                await message.delete(delay=0)
            
            elif(len(readyUsers) == 10):
                #we have 10 ready users, now need captains
                embed = discord.Embed(description="**Picking Captains**", color=0x03f0fc)
                await message.channel.send(embed=embed)
                inProgress = True
                firstCaptain = readyUsers[random.randrange(len(readyUsers))]
                readyUsers.remove(firstCaptain)
                secondCaptain = readyUsers[random.randrange(len(readyUsers))]
                readyUsers.remove(secondCaptain)
                embed = discord.Embed(description="**Captains** \n Team:" + firstCaptain.mention + "\n Team:" + secondCaptain.mention, color=0x03f0fc)
                await message.channel.send(embed=embed)
                await firstCaptain.move_to(team1VoiceChannel)
                await secondCaptain.move_to(team2VoiceChannel)
                embed = discord.Embed(description="🔵" + firstCaptain.mention + "**it is now your pick, pick with `.pick @user`.** \n **Players:** \n" + " \n ".join(str(x.mention) for x in readyUsers), color=0x03f0fc)
                await message.channel.send(embed=embed)
                await message.delete(delay=0)
            
            elif(len(readyUsers) != 0):
                embed = discord.Embed(description=author.mention + "**is now ready, we need **" + str(10 - len(readyUsers)) + " **more**", color=0x03f0fc)
                await message.channel.send(embed=embed)
                await message.delete(delay=0)
            return

    #pick command
    elif (message.content.lower().startswith('.pick') and inProgress == True and pickNum < 9):
        #make sure a captain is picking, and its his turn
        if author == firstCaptain and (pickNum == 1 or pickNum == 4 or pickNum == 6 or pickNum == 8):
            #get the user they picked
            if(len(message.mentions) != 1):
                embed = discord.Embed(description="**Please pick a user by @ing them. `!pick @user`**", color=0x03f0fc)
                await message.channel.send(embed=embed)
                return

            pickedUser = message.mentions[0]
            #make sure hes a real user
            if (pickedUser not in (name for name in readyUsers)):
                embed = discord.Embed(description=str(pickedUser) + "**is not in the `🔊Lobby`, please pick again.**", color=0xff0000)
                await message.channel.send(embed=embed)
                return

            #add him to team one
            teamOne.append(pickedUser)
            
            #move him to voice channel for team 1
            await pickedUser.move_to(team1VoiceChannel)

            #remove him from ready users
            readyUsers.remove(pickedUser)     

            #increment pick number
            pickNum+=1

            #check if we're done picking
            if (pickNum == 9):
                embed = discord.Embed(description=''' **Console connect:** \n `connect 139.99.144.30:28448; password t27D9M`

                **Team** 🔵CT \n ''' + " \n ".join(sorted(str(x.name) for x in teamOne)) + '''
                
                **Team** 🔴T \n ''' + " \n ".join(sorted(str(x.name) for x in teamTwo)) + '''
                **\n Pick maps when joined into server**''', color=0x33ff00)
                embed.set_footer(text="Server is now loading. Please wait about 20 seconds for server to start!", icon_url="https://cdn.dribbble.com/users/46633/screenshots/1185889/civchoice-loading-gifs800x600.gif")
                deleteAll = await message.channel.send(embed=embed)
                await dathost.start(myToken.serverId)
                await asyncio.sleep(300)
                await deleteAll.channel.purge(limit=100)
                embed = discord.Embed(description="**Join `🔊Lobby` and  `.r` in `💥ready-room💥` to ready up!**", color=0xb603fc)
                await message.channel.send(embed=embed)
                inProgress = False
                readyUsers = []
                firstCaptain = None
                secondCaptain = None
                pickNum = 1
                return
            #check if we need to pick again or its other captains turn
            if(pickNum == 2 or pickNum == 3 or pickNum == 5 or pickNum == 7):
                embed = discord.Embed(description="🔴" + secondCaptain.mention + " **it is now your pick, pick with `.pick @user`.\n Players:** \n" + " \n ".join(str(x.mention) for x in readyUsers), color=0x03f0fc)
                await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(description="🔵" + firstCaptain.mention + " **please pick again from \n**" + " \n ".join(str(x.mention) for x in readyUsers), color=0x03f0fc)
                await message.channel.send(embed=embed)

        #similar to above, just for team 2 and captain 2
        elif author == secondCaptain and (pickNum == 2 or pickNum == 3 or pickNum == 5 or pickNum == 7):
            #get the user they picked
            if(len(message.mentions) != 1):
                embed = discord.Embed(description="**Please pick a user by @ing them. `.pick @user`**", color=0x03f0fc)
                await message.channel.send(embed=embed)
                return

            pickedUser = message.mentions[0]
            teamTwo.append(pickedUser)
            
            #move him to voice channel for team 2
            await pickedUser.move_to(team2VoiceChannel)

            #remove him from ready users
            readyUsers.remove(pickedUser)    

            pickNum+=1
            if(pickNum == 1 or pickNum == 4 or pickNum == 6 or pickNum == 8):
                embed = discord.Embed(description="🔵" + firstCaptain.mention + " it is now your pick, pick with `.pick @user`. \n **Players:** \n" + " \n ".join(str(x.mention) for x in readyUsers), color=0x03f0fc)
                await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(description="🔴" + secondCaptain.mention + "**please pick again from** \n" + " \n ".join(str(x.mention) for x in readyUsers), color=0x03f0fc)
                await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(description="You're not a captain, sorry, but please let the captains select!", color=0xff0000)
            await message.channel.send(embed=embed)
        return

    #unready command               
    elif (message.content.lower() == '.unready' or message.content == '!ungaben' and inProgress == False):
        #make sure the user exists
        for user in readyUsers:
            if user == author:
                readyUsers.remove(user)
                #unready message
                embed = discord.Embed(description=author.mention + "**Is no longer ready. We need** " + str(10 - len(readyUsers)) + " **more!**", color=0xff0000)
                await message.channel.send(embed=embed)            
                break
        return

    #stopping one        
    elif message.content.lower() == '.stop':
        inProgress = False
        readyUsers = []
        firstCaptain = None
        secondCaptain = None
        pickNum = 1
        embed = discord.Embed(description="**Current 10man finished, need** 10 **readied players**", color=0xff0000)
        embed.set_footer(text="Server is shutting down", icon_url="https://i.imgur.com/EXemST2.gif")
        deleteAll = await message.channel.send(embed=embed)
        await message.delete(delay=0)
        await dathost.stop(myToken.serverId)
        await asyncio.sleep(30)
        await deleteAll.channel.purge(limit=100)
        embed = discord.Embed(description="**Join `🔊Lobby` and  `.r` in `💥ready-room💥` to ready up!**", color=0xb603fc)
        await message.channel.send(embed=embed)
        return
    #checks for anyone in a lobby
    elif message.content.lower().startswith('.lobby'):
        if (len(readyUsers) == 0):
            embed = discord.Embed(description="__**Lobby:**__" + "\n There are currently no players in queue!", color=0xebe534)
            await message.channel.send(embed=embed)
            await message.delete(delay=0)
        else:
            embed = discord.Embed(description="__**Lobby:**__ \n" + " \n ".join(sorted(str(x.name) for x in readyUsers)), color=0xebe534)
            await message.channel.send(embed=embed)  
            await message.delete(delay=0)  
            return

client.run(myToken.token)
