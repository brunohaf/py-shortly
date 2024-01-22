from models.url import Url
from models.user import User
from urllib.parse import urlsplit


from configs.database import Base

class DbQueryMock():
    def __init__(self, model):
        self.model = model
        self.data = DbSessionMock.db[model]

    def filter_by(self, **kwargs):
        self.data = [d for d in self.data if all(d.__dict__[k] == v for k, v in kwargs.items())]
        return self
    
    def first(self):
        return self.data[0] if len(self.data) > 0 else None
    
    def all(self):
        return self.data
     
class DbSessionMock():
    db = {
            Url: [Url(id=123, original_url='https://www.google.com', owner_id = 1), Url(id=456, original_url='https://www.google.com', owner_id = 2), Url(id=789, original_url='https://www.google.com', owner_id = 1)],
            User: [User(id=1, username='test', hashed_password='test'), User(id=2, username='test2', hashed_password='test2'), User(id=3, username='test3', hashed_password='test3')]
    }
    
    def query(self, Base):
        return DbQueryMock(Base)

    def add(self, instance : object):
        DbSessionMock.db[type(instance)].append(instance)
        pass

    def commit(self):
        pass

def is_valid_url(url):
    try:
        result = urlsplit(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False