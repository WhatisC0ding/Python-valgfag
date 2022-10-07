class Store:
    def __init__(self):
        self.value = 0
    def __call__(self, x):
        self.value += x
        return self.value

store = Store()
print(store(2))
print(store(30))
