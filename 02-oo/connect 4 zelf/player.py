class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
    
    def __str__(self): #om de print te veranderen zoals bij java toString
        return f"Player {self.name} with token {self.token}"
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value is None or len(value) < 1:
            raise ValueError("name is not valid")
        self.__name = value

    @property
    def token(self):
        return self.__token
    
    @token.setter
    def token(self, value):
        self.__token = value
