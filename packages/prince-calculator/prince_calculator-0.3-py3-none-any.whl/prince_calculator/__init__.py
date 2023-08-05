def add_numbers(a,b):
    return a+b

def enter_key():
    print("Please enter a key below")
    key = input()
    print('Key entered is : ',key)
    return key

def set_parameters():
    print("Please enter a model engine:")
    model_engine = input()
    print("Please set the accuracytemperature :")
    temp = float(input())
    return model_engine,temp

def qna():
    print("Enter question below : ")
    question = input()
    answer = 'Not configured yet'
    return answer
