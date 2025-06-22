from datetime import datetime
class Question:
    '''implements the question class for stack overflow'''

    def __init__(self, author, title, content):
        self.author = author
        self.title = title
        self.content = content
        self.votes = 0
        self.answers = []
        self.comments = []
        self.tags = []
        self.created_at = datetime.now()
