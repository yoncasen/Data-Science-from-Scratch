""""""
""" MODULES """
""""""

# One way is to simply import the module itself
import re
my_regex = re.compile("[0-9]+" , re.I)

# if you have the same in your code already, use an alias.
import re as regex
my_regex = re.compile("[0-9]+" , re.I)

# if the module has an unhandy name, and you're goint to type alot.
import matplotlib.pyplot as plt
plt.plot(...)

# If you need a few specific values from a module, 
# you can import them explicitly and use them without qualification
from collections import defaultdict,Counter
lookup = defaultdict(int)
my_counter = Counter()

