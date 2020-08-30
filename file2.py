
import file1

def func3():
    print("func3() ran in two.py")

def main():
    print("two.py start execution ###########")
    file1.func1()
    file1.func2()
    func3()
    print("two.py finish execution ##########")
