import asyncio
import sqlite3

from Config import TOKEN
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandStart

bot = Bot(token = TOKEN)
Disp = Dispatcher()

db = sqlite3.connect('Data.db')
UsersInfo = db.cursor()

UsersInfo.execute('''CREATE TABLE IF NOT EXISTS Users(
    userid INTEGER,
    service text,
    password text,
    login text
)''')

db.commit()

@Disp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f'Hi! \nIn this bot, you can save your account data \nto save, enter: \n/add [service] [password] [login]')

@Disp.message(Command('add'))
async def AddAccount(message: types.Message):
    messageSize = message.text.split()
    messageIndecs = len(messageSize)
    if messageIndecs != 4:
        await message.answer(f'Something went wrong! \nYou must enter: \n/add [service] [password] [login] \n WITHOUT SPACES')
        return 
    else:
        UsersInfo.execute('INSERT INTO Users VALUES(?, ?, ?, ?)',(
            message.from_user.id,
            messageSize[1],
            messageSize[2],
            messageSize[3]
        ))
        await message.answer(f'Your base is safe!')
        db.commit()


@Disp.message(Command('get'))
async def getData(message: types.Message):
    GetSize = message.text.split()
    GetIndecs = len(GetSize)
    if GetIndecs != 2:
        await message.answer(f'You only need to write the service name! \n WITHOUT SPACES')
        return
    else:
        UsersInfo.execute('SELECT * FROM Users WHERE userid = ? AND service = ?', (message.from_user.id, GetSize[1]))
        result = UsersInfo.fetchone()
        if result:
            await message.answer(f'Your base is: \n service: {GetSize[1]}, password: {result[2]}, login {result[3]}')
        else:
            await message.answer(f"⛔I couldn\'t find your information⛔Make sure you\'ve specified the correct service")
async def main():
    await Disp.start_polling(bot)

if __name__ == '__main__':
    try: 
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')