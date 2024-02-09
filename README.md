# Roblox-Starter
### Little Python project to start Roblox and Roblox Studio from the command-line.

## Install
Pull this repository with _git_:
`git clone https://github.com/ralphwuu/roblox-starter.git`

## Usage
Run python path/to/roblox-starter/main.py through a desktop shortcut<br>
Add a command-line argument to run Studio, accepted values are:<br>
true, do, yes, on, 1<br>
There's also a second argument that is responsible for having the script<br>
delay closing itself with the value being a number like:<br>
5 - for five seconds of delay.

## Run on logon
If you have a Windows user that doesn't do anything else beside play
or use Roblox Studio or you wish for Roblox to run on-logon then you can:
1. Place or symlink the script to the user auto starting folder
%APPDATA%\Microsoft\Windows\Start Menu\Programs\
2. Create a Task Scheduler task to run the script on user logon.