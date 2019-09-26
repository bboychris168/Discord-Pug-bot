# Discord-Pug-bot
Simple Discord 10man bot that picks teams and moves them into their voicechannels

Create the following channels `🔊Lobby` `🔵CT` `🔴T` `💥ready-room💥`. 

![Image of config](https://scontent.fsyd6-1.fna.fbcdn.net/v/l/t1.15752-9/70760526_1170460396479105_8676906833635442688_n.png?_nc_cat=104&_nc_oc=AQmsJ1yyadmYmYeklEscRVtkcH6MUsoFT9J9DlFdJo8_gjCy2rLC8OIAxO2fjHsjicA&_nc_ht=scontent.fsyd6-1.fna&oh=7b7abbbea59b278603e72fe4d3013a20&oe=5DF6D77A)


![Image of config](https://scontent.fsyd5-1.fna.fbcdn.net/v/t1.15752-9/70962484_2471421796514889_6404407747189669888_n.jpg?_nc_cat=105&_nc_oc=AQllz8vQNts-QqbaofW3_W51olAZPZRI05ut7ZIlWux-e8J_uU614WWE9gP2X31iTMM&_nc_ht=scontent.fsyd5-1.fna&oh=db748a39a363ae3ba165cc1e55ba0da8&oe=5E3D90B5) 


![Image of config](https://scontent.fsyd5-1.fna.fbcdn.net/v/t1.15752-9/71756161_2376723492588753_3446406385376428032_n.jpg?_nc_cat=103&_nc_oc=AQkj1XXPAc54FOTxDSu2lBFSMxmkd1ywawCC7zerVKBo_pbn3n4AGRBrYTwOUXVK5jY&_nc_ht=scontent.fsyd5-1.fna&oh=145871bafc7986c00a2fae8e9a53416d&oe=5DEFB28C)

Make sure you are in developer mode in discord. Copy id of each channel and paste it into the myToken.py config file.

**COMMANDS** `.r  .unready  .lobby  .stop .pick`

**HOW TO USE**
1. Join `🔊Lobby voicechannel`
2. `.r` in `💥ready-room💥`
3. When 10 players `.r`, the bot will then select 2 random captains and place them into `🔵CT`and `🔴T` voicechannels.
4. Captains will use the `.pick @user` command to pick players from the lobby. The picked players will automatically be moved to their teams voicechannels by the bot.
5. Once teams are picked. The bot will start the server and give the ip to join. 
6. When the live match has been completed use the command `.stop` to stop the server and restart the 10man. 

My discord https://discord.gg/YkNpEbg , join if you have any questions about the bot 👍
`keep in mind that there are still bugs and still need fixing on some code`

**RUNNING THE BOT**
- First run `python -m pip install -U discord.py` (Requires python 3)
- Then change myTokenTemplate.py to myToken.py, and edit that file to put your discord bot token in it
- Run `python bot.py`
