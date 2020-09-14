from search import *


def run():
    print("Loading the files and preparing the system...")
    init("./some")
    print("The system is ready.", end=" ")
    while True:
        term = input("Enter your text:")
        while term[-1] != '#':
            res = search(term)
            for i in range(len(res)):
                print(f"{i + 1}.", end=" ")
                res[i].print()
            term += input(term)


run()
