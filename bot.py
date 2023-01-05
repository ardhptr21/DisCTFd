from json.decoder import JSONDecodeError
import logging
import asyncio
from requests import RequestException

from config import *
from db import CTFdDB
from session import session as s
from sender import sender

class CTFdBot:

    async def initial(self):
        await sender.send(content="CTFdBot is online")
        await asyncio.sleep(10)

        try:
            challs = s.get("/statistics/challenges/solves").json()['data']
        except (RequestException, JSONDecodeError, KeyError) as e:
            logging.error(e)
            asyncio.create_task(self.initial())
            return

        for chall in challs:
            try:
                users = s.get(f"/challenges/{chall['id']}/solves").json()['data']
            except (RequestException, JSONDecodeError, KeyError):
                logging.error(e)
                asyncio.create_task(self.solves())
                return

            if not users:
                asyncio.create_task(self.solves())
                return

            for user in users:
                CTFdDB.cursor.execute("INSERT INTO solves (user_id, chall_id) VALUES (%s, %s)", (user['account_id'], chall['id']))
            CTFdDB.conn.commit()
        
        logging.info("INITIAL DATA LOADED")

        asyncio.create_task(self.solves())

    async def solves(self):
        await asyncio.sleep(10)

        try:
            challs = s.get("/statistics/challenges/solves").json()['data']

            for chall in challs:
                if chall['solves'] > 0:
                    CTFdDB.cursor.execute("SELECT user_id from solves WHERE chall_id = %s", (chall['id'],))
                    ids = CTFdDB.cursor.fetchall()

                    try:
                        solvers = s.get(f"/challenges/{chall['id']}/solves").json()['data']
                    except (RequestException, JSONDecodeError, KeyError, IndexError) as e:
                        logging.error(e)
                        asyncio.create_task(self.solves())
                        return

                    if not ids:
                        solver = solvers[0]
                        if solver:
                            await sender.send(content=f"FIRST BLOOD! {chall['name']} has been pwned by {solver['name']}")
                            CTFdDB.cursor.execute("INSERT INTO solves (user_id, chall_id) VALUES (%s, %s)", (solver['account_id'], chall['id']))
                            CTFdDB.conn.commit()
                            logging.info(f"SEND A FIRST BLOOD MESSAGE")
                    else:
                        if len(solvers) > len(ids):
                            new_solvers = solvers[len(ids):]
                            for solver in new_solvers:
                                await sender.send(content=f"BLOOD! {chall['name']} has been pwned by {solver['name']}")
                                CTFdDB.cursor.execute("INSERT INTO solves (user_id, chall_id) VALUES (%s, %s)", (solver['account_id'], chall['id']))
                                CTFdDB.conn.commit()
                                logging.info("SEND A BLOOD MESSAGE")

        except (RequestException, JSONDecodeError, KeyError) as e:
            logging.error(e)
            asyncio.create_task(self.solves())
            return

        asyncio.create_task(self.solves())
        

    async def run(self):
        await self.initial()
