from api.dependencies.security import get_password_hash, verify_password, create_access_token, decode_access_token

def test_password_hashing():
    password = "test123"
    hashed = get_password_hash(password)
    assert verify_password(password, hashed)

def test_jwt_token_creation_and_decoding():
    data = {"sub": "testuser"}
    token = create_access_token(data)
    decoded = decode_access_token(token)
    assert decoded == "testuser"