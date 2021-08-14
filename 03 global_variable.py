# -------------global variable--------------/

x =56
def func1():
    global x
    print(f"it is a global variable {x}")
    x = 8
    print(f"it is a local variable {x}")
    
func1()
print(f"it prints local varible {x}")