class DatabaseCredentials():
    def __init__(self):
        self.connection_str = ''
        self.conn_args = {'check_same_thread': False}

# mysql+pymysql://myuser:mypassword@172.17.0.2/Shortly