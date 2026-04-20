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
    service TEXT,
    login TEXT,
    password TEXT
)''')

db.commit()

@Disp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f'''Hi! \nIn this bot, you can save your account data \nto save, enter: \n/add [service] [Login] [Password]
    \nto get, enter: /get [service]
    \nto delete serivce, enter: /del [service]
    \nto delete special account, enter: /del [service] [login]
    \n⛔WITHOUT SPACES⛔''')

@Disp.message(Command('add'))
async def AddAccount(message: types.Message):
    messageSize = message.text.split()
    messageIndecs = len(messageSize)
    
    if messageIndecs != 4:
        await message.answer(f'Something went wrong! \nYou must enter: \n/add [Service] [Login] [Password] \n⛔WITHOUT SPACES⛔')
        return 
    
    else:
        UsersInfo.execute('INSERT INTO Users VALUES(?, ?, ?, ?)', (
            message.from_user.id,
            messageSize[1],
            messageSize[2],
            messageSize[3]
        ))
        
        db.commit()
        await message.answer(f'✅ Your base is safe! Account for {messageSize[1]} added.')


@Disp.message(Command('get'))
async def getData(message: types.Message):
    GetSize = message.text.split()
    GetIndecs = len(GetSize)
    if GetIndecs != 2:
        await message.answer(f'You only need to write the service name! \n⛔WITHOUT SPACES⛔')
        return
    else:
        UsersInfo.execute('SELECT * FROM Users WHERE userid = ? AND service = ?', (message.from_user.id, GetSize[1]))
        result = UsersInfo.fetchall()
        if result:
            for account in result:
                await message.answer(f'👾Service: {account[1]}, 🧾Login: {account[2]}, 🔑Password: {account[3]}')
        else:
            await message.answer(f"⛔I couldn\'t find your information⛔Make sure you\'ve specified the correct service")
@Disp.message(Command('del'))
async def Delete(message: types.Message):
    DeleteSize = message.text.split()
    DeleteIndecs = len(DeleteSize)
    if DeleteIndecs == 2:
        UsersInfo.execute('DELETE FROM Users WHERE userid = ? AND service = ?', (message.from_user.id, DeleteSize[1]))
        await message.answer('Your service have been successfully deleted')
        db.commit()
    elif DeleteIndecs == 3:
        UsersInfo.execute('DELETE FROM Users WHERE userid = ? AND service = ? AND login = ?', (message.from_user.id, DeleteSize[1], DeleteSize[2]))
        await message.answer('Your account have been successfully deleted')
        db.commit()
    else:
        await message.answer(f'''🚫Incorrect spelling! \n/del [Service] - if you want to delete all services 
        \n/del [Service] [Login] - special account \n⛔WITHOUT SPACES⛔''')
async def main():
    await Disp.start_polling(bot)

if __name__ == '__main__':
    try: 
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')