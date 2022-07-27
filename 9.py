class Vehicle:
    def __del__(self):
        print("Vehicle object destroyed")
        print(10/0)
v = Vehicle()
del v

#Exception ignored in: <function Vehicle.__del__ at 0x0000029167AB4040>
#Traceback (most recent call last):
#  File "C:\Users\PAWANDEEP SINGH\OneDrive\Desktop\assignment 4\9.py", line 4, in __del__
#    print(10/0)
#ZeroDivisionError: division by zero

