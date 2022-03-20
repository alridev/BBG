import asyncio
import os
import sys
from json import loads
from random import choice
from colorama import Fore,init
from requests import post
from os import system
from telethon import TelegramClient, events
from time import sleep,time
from telethon.errors.rpcerrorlist import FloodWaitError
C = Fore
init()
system('cls')
bb =f'''{C.YELLOW}
$$$$$$$   $$$$$$$    $$$$$$ 
$$    $$  $$    $$  $$    $$
$$    $$  $$    $$  $$      
$$$$$$$   $$$$$$$   $$  $$$$
$$    $$  $$    $$  $$    $$
$$    $$  $$    $$  $$    $$
$$$$$$$   $$$$$$$    $$$$$$  
{C.LIGHTYELLOW_EX}by https://lolz.guru/members/2977610/                       
'''

#удалил - гей
print(bb)
chars = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
class bbg():
    def __init__(self):
        try:
            with open('config.json','r+',encoding='utf-8') as config:
                config = dict(loads(config.read()))
                self.accounts = []
                if not os.path.exists(os.path.abspath(os.path.join(config['accounts']))):open(os.path.abspath(os.path.join(config['accounts'])),'r+',encoding='utf-8');return print('Write file accounts.txt')
                
                with open(os.path.abspath(os.path.join(config['accounts'])),'r+',encoding='utf-8') as accounts:
                    for account in accounts.readlines():
                        self.accounts.append(account.replace('\n','').split(':'))
                self.logs_bot_token = config['logs_bot_token']
                self.logs_user = config['logs_user']
                self.limit_gen = config['limit_gen']
                self.clients = []
                print(C.LIGHTGREEN_EX+'Config loaded.')
                for i in config:print(C.LIGHTMAGENTA_EX+i,C.RED+'-'+C.MAGENTA,config[i])

        except Exception as e:
            print(C.RED+"Exception as read config.json --",e)
            return

        self._log_('Program started!')
        asyncio.get_event_loop().run_until_complete(self.connect_to_account())
        for client in self.clients:
                    asyncio.ensure_future(self.launch(client))
        for client in self.clients:
            client[0].run_until_disconnected()
    def _log_(self,message):
                post(
                        url='https://api.telegram.org/bot{0}/{1}'.format(self.logs_bot_token, 'sendMessage'),
                                        data={'chat_id': int(self.logs_user), 'text': '<b><a href="https://lolz.guru/threads/3656270">[BBG]</a> by <a href="https://lolz.guru/members/2977610/     ">e3587190d33749ac</a></b>\n<i>'+message+'</i>','parse_mode': 'html'}
                    )    
    async def connect_to_account(self):
        for account in self.accounts:
            try:
                if not os.path.exists('sessions'):os.mkdir('sessions')
                client = TelegramClient(f'sessions/bbg_{account[0]}',int(account[0]),account[1])
                print(C.CYAN+'Account: '+C.MAGENTA+' '.join(account))
                await client.start(account[2])
                self.clients.append([client,account[0]])
                self._log_(f"Successful connection to <code>{account[0]}</code>!")
            except Exception as e:
                self._log_(f"Exception as connect to <code>{account[0]}</code>\n"+str(e))
    
    async def launch(self,ch):
            client,account = ch
            self._log_(f'Started generate via account <code>{account[0]}</code>.')
            @client.on(events.NewMessage(159405177))
            async def on_message(event):
                try:
                    message = event.message.message
                    if 'вы получили' in message.lower() or 'you have received' in message.lower():self._log_(f'Account: <code>{account}</code>\n'+message)
                except:pass
            for i in range(self.limit_gen):
                    start  = time()
                    try:await client.send_message('BTC_CHANGE_BOT','/start c_'+self.generate())
                    except FloodWaitError as e:self._log_(f'Timeout, flood error via account <code>{account}</code>\n{str(e)}');sleep(int(str(e).replace('A wait of ','').replace('seconds is required (caused by SendMessageRequest)','')))
                    except Exception as e:self._log_(f'Exception via account <code>{account}</code> as send message to @BTC_CHANGE_BOT\n{str(e)}')
                    stop = time()
                    if (stop-start) < 1.1: sleep(1.1-(stop-start))
                    
            self._log_(f'Finished via account <code>{account}</code>.')
            self.clients.remove([client,account])
    def generate(self):
        token = ''
        for i in range(32):token += choice(chars)
        return token 



f  =  bbg()

print(C.RED+'Program exit with 30 seconds.')
sleep(30)
sys.exit(0)
