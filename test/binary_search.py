from opfu.binary_search import binary_search

if __name__ == '__main__':
    def func(x):
        return x*x - 4

    print(binary_search(0, 10, func))