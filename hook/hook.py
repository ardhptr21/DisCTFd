import asyncio
import logging

from config import *
from config import SLEEP_TIME
from utils.session import session as s

from .db import CTFdDB
from .entities.challenge import Challenge
from .sender import sender


class CTFdHook:

    async def initial(self):
        await asyncio.sleep(SLEEP_TIME)

        challs = Challenge.challenges_solves()
        
        if not challs:
            asyncio.create_task(self.initial())
            return

        for c in challs:
            chall = Challenge(c['id'], c['name'])
            users = chall.users_solved()

            if not users:
                asyncio.create_task(self.solves())
                return

            for user in users: CTFdDB.add_solve(user['account_id'], chall.chall_id)
        
        logging.info("INITIAL DATA LOADED")

        asyncio.create_task(self.solves())

    async def solves(self):
        await asyncio.sleep(SLEEP_TIME)

        challs = Challenge.challenges_solves()

        if not challs:
            asyncio.create_task(self.solves())
            return

        for c in challs:
            chall = Challenge(c['id'], c['name'], c['solves'])
            if chall.chall_solves > 0:
                ids = chall.local_users_solved()
                solvers = chall.users_solved()

                if not solvers: continue

                if not ids:
                    solver = solvers[0]
                    if solver:
                        await sender.send_first_blood(chall.chall_name, chall.chall_category, solver['name'])
                        CTFdDB.add_solve(solver['account_id'], chall.chall_id)
                        logging.info(f"SEND A `FIRST BLOOD` MESSAGE")
                else:
                    if len(solvers) > len(ids):
                        new_solvers = solvers[len(ids):]
                        for solver in new_solvers:
                            await sender.send_solved(chall.chall_name, chall.chall_category, solver['name'])
                            CTFdDB.add_solve(solver['account_id'], chall.chall_id)
                            logging.info("SEND A `SOLVED` MESSAGE")

        asyncio.create_task(self.solves())
        

    async def run(self):
        CTFdDB.init_db()
        logging.info("Starting CTFdBot")
        await self.initial()