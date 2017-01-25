class HangMan:

    def __init__(self):
        self.secretWord = "palabra"
        self.body = ["O","O","O","O","O","O"]
        self.partial = ["_","_","_","_","_","_","_"]
        
    
    def validate(self, word):
        i=0
        is_found = False
        if (len(word)==1):
            for letter in self.secretWord:
                if (letter==word):
                    self.partial[i] = word
                    is_found = True
                i+=1
            if not is_found:
                j=0
                for b in self.body:
                    if b=='O':
                        self.body[j]='X'
                        break
                    j+=1
        str_res=""
        str_b=""
        for p in self.partial:
            str_res=str_res+p

        for b in self.body:
            str_b=str_b+b
  
        return str_b, str_res 
