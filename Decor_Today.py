from datetime import date


def decor(func):
    def wrap():
        #print("============")
        todays()
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")
    
def todays():
    today = date.today()
    print("Today's date:", today)

decorated = decor(print_text)
decorated()

#decorated = decor(todays)
