from services import password_hash_service as pwd_service
from pytest import fixture

@fixture
def password() -> str:
    return "SuperComplexPassword!"

def test_get_password_hash_should_be_different_from_original_password(password):

    # Act
    hashed_password = pwd_service.get_password_hash(password)

    # Assert
    assert hashed_password != password

def test_get_password_hash_alg_should_be_valid(password):

    # Arrange
    hashd = pwd_service.get_password_hash(password)

    # Act
    alg = pwd_service.pwd_context.identify(hashd)

    # Assert
    assert alg in pwd_service.schemes

def test_verify_password_should_be_valid(password):

    # Arrange
    hashd = pwd_service.get_password_hash(password)

    # Act
    is_valid_password = pwd_service.verify_password(password, hashd)

    # Assert
    assert is_valid_password is True