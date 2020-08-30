
def func1():
    print("func1() ran in one.py")

def func2():
    print("func2() ran in one.py")

if __name__ == "__main__":
    print("one.py start execution..........")
    func1()
    func2()
    print("one.py finish execution.........")
else:
    print("\none.py is being imported into another module\n")
