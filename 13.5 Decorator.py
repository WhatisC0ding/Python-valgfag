def trackCall(myFunc):
    def wrapper():
        print('før decorator')
        myFunc()
        print('efter decorator')
    return wrapper

@trackCall
def hello():
    print("Hello World")

hello()