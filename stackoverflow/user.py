
class User:
    '''Class to maintain user of stackoverflow'''
    def __init__(self,user_id:int,username:str,email:str,reputation:int)->None:
        self.user_id = user_id
        self.username = username
        self.email = email
        self.reputation = reputation

