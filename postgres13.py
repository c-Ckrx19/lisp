from database import PostgreSQL


class MyPostgres(PostgreSQL):
    def __init__(self):
        super().__init__(db='', host='', user='', pwd='', port=)
        self.cur = conn.cursor()
    
    def create_table(self, create_table_command):
        self.cur.execute(create_table_command)
        self.commit()
    
    def read(self):
        pass

    def write(self):
        pass
