def fibonacci(limit = 10):
    a, b = 0, 1
    for i in range(0, limit):
        print(f'{a}', end=' ')
        a, b = b, a+b

print('MYOEIS', __name__)

if __name__ == '__main__':
    fibonacci(7)
    print('\n')