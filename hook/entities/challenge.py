import logging
from json.decoder import JSONDecodeError

from requests import RequestException

from utils.session import session as s

from ..db import CTFdDB

category_cache = dict()

class Challenge:
    chall_category: str = None
    def __init__(self, chall_id: int, chall_name: str, chall_solves: int = None) -> None:
        self.chall_id = chall_id
        self.chall_name = chall_name
        self.chall_solves = chall_solves

        self._set_category()

    def _set_category(self) -> None:
        global category_cache

        if self.chall_category: return
        if self.chall_id in category_cache:
            self.chall_category = category_cache[self.chall_id]
            return

        try:
            self.chall_category = s.get(f"/challenges/{self.chall_id}").json()['data']['category']
            category_cache = {self.chall_id: self.chall_category}
        except (RequestException, JSONDecodeError, KeyError) as e:
            logging.error(e)
            return
    
    def users_solved(self) -> list:
        try:
            users = s.get(f"/challenges/{self.chall_id}/solves").json()['data']
            return users
        except (RequestException, JSONDecodeError, KeyError) as e:
            logging.error(e)
            return []
    
    def local_users_solved(self) -> list:
        CTFdDB.cursor.execute("SELECT user_id from solves WHERE chall_id = %s", (self.chall_id,))
        return CTFdDB.cursor.fetchall()

    @staticmethod
    def challenges_solves() -> list:
        try:
            challs = s.get("/statistics/challenges/solves").json()['data']
            return challs
        except (RequestException, JSONDecodeError, KeyError) as e:
            logging.error(e)
            return