# Discord-Pug-bot
Simple Discord 10man bot that picks teams and moves them into their voicechannels

Create the following channels `🔊Lobby` `🔵CT` `🔴T` `💥ready-room💥`. 

![Image of config](https://scontent.fsyd6-1.fna.fbcdn.net/v/l/t1.15752-9/70760526_1170460396479105_8676906833635442688_n.png?_nc_cat=104&_nc_oc=AQmsJ1yyadmYmYeklEscRVtkcH6MUsoFT9J9DlFdJo8_gjCy2rLC8OIAxO2fjHsjicA&_nc_ht=scontent.fsyd6-1.fna&oh=7b7abbbea59b278603e72fe4d3013a20&oe=5DF6D77A)

Make sure you are in developer mode in discord. Copy id of each channel and paste it into the myToken.py config file.

**COMMANDS** `.r  .unready  .lobby  .stop .pick`

**HOW TO USE**
1. Join `🔊Lobby voicechannel`
2. `.r` in `💥ready-room💥`
3. When 10 players `.r`, the bot will then select 2 random captains and place them into `🔵CT`and `🔴T` voicechannels.
4. Captains will use the `.pick @user` command to pick players from the lobby. The picked players will automatically be moved to their teams voicechannels.
5. Once teams are picked. The bot will start the server and give the ip to join. 
6. When the live match has been completed use the command `.stop` to stop the server and restart the 10man. 

My discord https://discord.gg/YkNpEbg , join if you have any questions about the bot 👍
`keep in mind that there are still bugs and still need fixing on some code`

**RUNNING THE BOT**
- First run `python -m pip install -U discord.py` (Requires python 3)
- Then change myTokenTemplate.py to myToken.py, and edit that file to put your discord bot token in it
- Run `python bot.py`
