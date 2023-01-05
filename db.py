from mysql import connector

from config import DB_CREDENTIALS

class CTFdDB:
    conn = connector.connect(**DB_CREDENTIALS)
    cursor = conn.cursor()

    @staticmethod
    def init_db():
        CTFdDB.cursor.execute("""
            CREATE TABLE IF NOT EXISTS solves (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                chall_id INT NOT NULL
            )
        """)
        CTFdDB.conn.commit()