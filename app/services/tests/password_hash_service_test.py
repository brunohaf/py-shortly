from services import password_hash_service as pwd_service

# Arrange
PASSWORD = "SuperComplexPassword!"

def test_get_password_hash_should_be_different_from_original_password():

    # Act
    hashed_password = pwd_service.get_password_hash(PASSWORD)

    # Assert
    assert hashed_password != PASSWORD

def test_get_password_hash_alg_should_be_bcrypt():


    # Arrange
    hashd = pwd_service.get_password_hash(PASSWORD)

    # Act
    alg = pwd_service.pwd_context.identify(hashd)

    # Assert
    assert alg == 'bcrypt'

def test_verify_password_should_be_valid():

    # Arrange
    hashd = pwd_service.get_password_hash(PASSWORD)

    # Act
    is_valid_password = pwd_service.verify_password(PASSWORD, hashd)

    # Assert
    assert is_valid_password is True