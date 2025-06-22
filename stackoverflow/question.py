from datetime import datetime
from user import User
class Question:
    '''implements the question class for stack overflow'''

    def __init__(self, question_id:int,author:User, title:str, content:str) -> None:
        self.id = question_id
        self.author = author
        self.title = title
        self.content = content
        self.votes = 0
        self.answers = []
        self.comments = []
        self.tags = []
        self.created_at = datetime.now()
