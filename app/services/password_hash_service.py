from passlib.context import CryptContext

schemes=["bcrypt"]
pwd_context = CryptContext(schemes, deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)