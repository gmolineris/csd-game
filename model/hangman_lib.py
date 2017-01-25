class HangMan:

    def __init__(self):
        self.secretWord = "i"
    
    def validate(self, word):
        return word in self.secretWord 
