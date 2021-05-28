from mysql.connector import connect
from mysql.connector.errors import Error
import asyncio

class Handler(object):
    def __init__(self, user: str, pswd: str, dbname: str):
        self.user = user
        self.pswd = pswd
        self.dbname = dbname

    def create_db_loop(self, function):
        ioloop = asyncio.get_event_loop()
        tasks = [
            ioloop.create_task(function)
        ]
        wait_tasks = asyncio.wait(tasks)
        ioloop.run_until_complete(wait_tasks)
        ioloop.close()

    async def getChatInformation(self, chat_id: int):
        connection = connect(user=self.user, password=self.pswd, database=self.dbname)
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM groups WHERE group_id={chat_id}')
        values = cursor.fetchall()

        print(values)

sql = Handler(user='', pswd='', dbname='')
sql.create_db_loop(sql.getChatInformation(chat_id=123))
