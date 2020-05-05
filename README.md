Project currently not mantained. A new version will be in the works. 

# Discord-Pug-bot
Simple Discord 10man bot that picks teams and moves them into their voicechannels

Create the following channels `🔊Lobby` `🔵CT` `🔴T` `💥ready-room💥`. 

![Image of config](https://scontent.fsyd1-1.fna.fbcdn.net/v/l/t1.15752-9/70760526_1170460396479105_8676906833635442688_n.png?_nc_cat=104&_nc_sid=b96e70&_nc_ohc=i4_VqQpfn1MAX87-xl0&_nc_ht=scontent.fsyd1-1.fna&oh=4f29568c505c293d2f25e5bfcce1412d&oe=5EB88706)


![Image of config](https://scontent.fsyd1-1.fna.fbcdn.net/v/t1.15752-9/70962484_2471421796514889_6404407747189669888_n.jpg?_nc_cat=105&_nc_sid=b96e70&_nc_ohc=8Zc79qpz0JoAX-gk3Jn&_nc_ht=scontent.fsyd1-1.fna&oh=c99f2a2d8c3721afc36f8ba69f1126d6&oe=5EB8FECB) 


![Image of config](https://scontent.fsyd1-1.fna.fbcdn.net/v/t1.15752-9/71756161_2376723492588753_3446406385376428032_n.jpg?_nc_cat=103&_nc_sid=b96e70&_nc_ohc=DCh7z5DObicAX_Hw83K&_nc_ht=scontent.fsyd1-1.fna&oh=2c538fb1f118ffa57982f74739cc4397&oe=5EB7C2F4)

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
