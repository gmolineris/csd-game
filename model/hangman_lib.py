from random import random

class HangMan():
    def __init__(self):
        self.secret = [1,2,3,4]

    def validate(self, value):
        i = 0
        result = ''
        for v in value:
            if (int(v) == self.secret[i]):
               result += '*'
            elif (int(v) in self.secret):
               result += '?'
            else:
               result += '_'
            i+=1     
        return result  




