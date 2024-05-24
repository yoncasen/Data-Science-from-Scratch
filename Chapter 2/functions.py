""""""
""" FUNCTIONS """
""""""

# A function is a rule for taking zero or more inputs and returning a corresponding output.
def double(x):
  """
  This is where you put an optional docstring that explains what the function does.
  For example, this function mutliplies its input by 2.
  """
  return x * 2

# Python functions are first-class, 
# which means that we can assign them to variables and pass them into functions just like any other arguments:

def apply_to_one(f):
  """ Calls the function f with 1 as its argument """
  return f(1)

my_double = double                  # refers to the previously defined function
x = apply_to_one(my_double)         # equals 2

# you can create short anonymous functions, or lambdas

y = apply_to_one(lambda x: x + 4)   # equals 5

# you can assing lambdas to variables, but you can just use def instead

another_double = lambda x: x * 2    # don't do this

def another_double(x):
  """ Do this instead """
  return 2 * x

# Functions parameters can also be given default arguments.
def my_print(message  = "my default message"):
  print(message)

my_print("hello")                   # prints 'hello'
my_print()                          # prints 'my default message'

# It is sometimes useful to specify arguments by name
def full_name(first = "What's-his-name", last="Something"):
  return first + " " + last

full_name("Jane","Doe")
full_name("Jane")
full_name(last="Doe")

