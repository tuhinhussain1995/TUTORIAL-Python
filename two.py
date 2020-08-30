
import one

def func3():
    print("func3() ran in two.py")

if __name__ == "__main__":
    print("two.py start execution ###########")
    one.func1()
    one.func2()
    func3()
    print("two.py finish execution ##########")
else:
    print("two.py is being imported into another module")
