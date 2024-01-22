class DatabaseCredentials(): #TO-DO: Get these from a appsettings.json like file or environment variables
    def __init__(self):
        self.connection_str = ''
        self.conn_args = {'check_same_thread': False}