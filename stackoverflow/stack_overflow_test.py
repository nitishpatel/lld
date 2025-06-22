import pytest
from user import User

def test_user_create():
    user = User(1,"Test_User","testuser@email.com",0)
    assert user.user_id == 1
    assert user.username == "Test_User"
    assert user.email == "testuser@email.com"
    assert user.reputation == 0



