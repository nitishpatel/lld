import pytest
from user import User

def test_user_create():
    user = User(1,"Test_User","testuser@email.com",0)
    assert user.id == 1
