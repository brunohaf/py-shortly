from models.url import Url, UrlRequest
from models.user import User
from .dependencies import DbSessionMock, is_valid_url
from fastapi import HTTPException
from services import url_shortener_service
from pytest import fixture

#Arrange

session = DbSessionMock()

def get_db_mock_obj(model : type):
    return session.db[model][0]

@fixture
def get_valid_urlRequest():
    return UrlRequest(url='https://www.google.com', user_id=1)

@fixture
def get_valid_dbuser():
    return get_db_mock_obj(User)

@fixture
def get_valid_dburl():
    return get_db_mock_obj(Url)


def test_get_long_url_should_succeed(get_valid_dburl):
    #Act
    try:
        long_url = url_shortener_service.get_long_url(get_valid_dburl.id, session)
    
    #Assert
        assert long_url is not None
    except Exception:
        assert False

def test_get_long_url_should_raise_HTTPException():
    
    #Arrange
    invalid_url_id = 222222

    #Act
    try:
        _ = url_shortener_service.get_long_url(invalid_url_id, session)
    
    #Assert
        assert False
    except Exception as e:
        assert type(e) is HTTPException

def test_shorten_should_succeed(get_valid_urlRequest):

    #Act
    try:
        shortened = url_shortener_service.shorten(get_valid_urlRequest, session)
    
    #Assert
        assert shortened is not None
        assert type(shortened) is str
        assert len(shortened) > 0
        assert shortened.startswith('http')
    except Exception:
        assert False

def test_get_url_id():

    #Arrange 
    user_id = '2224'

    #Act
    url_id = url_shortener_service.get_url_id(user_id)

    #Assert
    assert url_id is not None
    assert type(url_id) is str
    assert 10 >= len(url_id) > 0
    

def test_get_user_urls_should_succeed(get_valid_dbuser):

    #Arrange
    dbuser_urls = list(filter(lambda url: url.owner_id == get_valid_dbuser.id, session.db[Url]))

    #Act
    fetched_urls = url_shortener_service.get_user_urls(get_valid_dbuser, session)

    #Assert
    assert fetched_urls is not None
    assert type(fetched_urls) is list
    assert len(fetched_urls) == len(dbuser_urls)
    assert all(any(str(url.id) in fetched_url for fetched_url in fetched_urls) for url in dbuser_urls)

def test_build_url_for_id_should_return_valid_url(get_valid_dburl):

    # Act
    url_to_check = url_shortener_service.build_url_for_id(get_valid_dburl.id)

    # Assert
    assert url_to_check is not None
    assert type(url_to_check) is str
    assert len(url_to_check) > 0
    assert is_valid_url(url_to_check)