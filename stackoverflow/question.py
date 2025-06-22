from datetime import datetime
from user import User
class Question:
    '''implements the question class for stack overflow'''

    def __init__(self,author:User, title:str, content:str) -> None:
        self.id = id(self)
        self.author = author
        self.title = title
        self.content = content
        self.votes = 0
        self.answers = []
        self.comments = []
        self.tags = []
        self.created_at = datetime.now()
