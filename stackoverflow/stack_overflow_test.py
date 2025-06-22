import pytest
from user import User
from question import Question

@pytest.fixture
def user():
    return User(1, "Test_User", "testuser@email.com", 0)

def test_user_create():
    user = User(1,"Test_User","testuser@email.com",0)
    assert user.user_id == 1
    assert user.username == "Test_User"
    assert user.email == "testuser@email.com"
    assert user.reputation == 0

def test_question_create(user):
    question = Question(user,"What is Python?","help with python")
    assert question.author == user
    assert question.title == "What is Python?"
    assert question.content == "help with python"
    assert question.votes == 0
    assert question.answers == []
    assert question.comments == []
    assert question.tags == []
    assert question.created_at is not None









