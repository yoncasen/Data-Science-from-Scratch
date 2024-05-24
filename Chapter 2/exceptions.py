#when something goes wrong while the program is running, 
#Python raises an exception

#unhandled exceptions will cause the program to crash. 
#To handle use try, except

try:
  print(0/0)
except ZeroDivisionError:
  print("cannot divide by zero")