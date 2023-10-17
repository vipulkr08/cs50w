def annouce(func):
    def wrapper():
        print("About to run the function")
        func()
        print("Done with the function")
    return wrapper

@annouce
def hello():
    print("Hello, world!")

hello()