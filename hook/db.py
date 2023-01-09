from mysql import connector

from config import DB_CREDENTIALS

class CTFdDB:
    conn = connector.connect(**DB_CREDENTIALS)
    cursor = conn.cursor()

    @staticmethod
    def init_db():
        CTFdDB.cursor.execute("""
            DROP TABLE IF EXISTS solves;
        """)
        CTFdDB.cursor.execute("""
            CREATE TABLE IF NOT EXISTS solves (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                chall_id INT NOT NULL
            );
        """)
        CTFdDB.conn.commit()
    
    @staticmethod
    def add_solve(user_id: int, chall_id: int):
        CTFdDB.cursor.execute("INSERT INTO solves (user_id, chall_id) VALUES (%s, %s)", (user_id, chall_id))
        CTFdDB.conn.commit()