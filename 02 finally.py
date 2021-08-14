# ---------------finally--------------/
try:
    a = int(input("enter no: "))
    b = 1/a
    print(b)
except Exception as e:
    print(e)
    exit()

finally:         # it excutes , as the error is occurs or not
    print("we are done")
