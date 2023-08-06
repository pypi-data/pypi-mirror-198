def add_numbers(a,b):
    return a+b

class enter_key:
    def __init__(self):
        print("Please enter a key below")
        self.key = input()
        print('Key entered is : ',self.key)
    def show(self): 
        print('inisde show enter key')   
        return self.key

class set_parameters:
    def __init__(self):
        self.model_engine = 'davinci'
        self.temp = 0.2
        print("Please enter a model engine:")
        self.model_engine = input()
        print("Please set the accuracy temperature :")
        self.temp = float(input())
    def show_parameters(self):
        return self.model_engine,self.temp
class qna(enter_key,set_parameters):
    def __init__(self):
        print('iniside qna')
        self.key = enter_key().show()
        self.show_parameters = set_parameters().show_parameters()
        print(self.key,'/',self.show_parameters)
    def question(self):
        print('here',self.key)
        if self.key == "":
            print("You have not entered the API key!")
        print("Enter question below : ",self.key)
        self.question = input()
        self.answer = 'Not configured yet'
        print(self.answer)
