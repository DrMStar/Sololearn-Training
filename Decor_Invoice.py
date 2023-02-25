"""def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

@decor
def print_text():
    print("Hello world!")

print_text();
"""

#your code goes here
def decor(func):
    def wrap(num):
        print("***")
        func(num)
        print("***")
        print("END OF PAGE")
    return wrap
    
@decor
def invoice(num):
    print("INVOICE #" +num)

#num = "42"
#a = input()
invoice(input());
