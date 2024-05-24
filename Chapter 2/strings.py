""""""
""" STRINGS """
""""""

# Single or double quotes can be used to create a string, 
# but the quotes have to match

single_quoted_string = 'data science'
double_quoted_string = "data science"

# multiline strings requires three double quotes
multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""

# Python uses backslashes to encode  special characters

tab_string = "\t"
len(tab_string) # is 1

# you can create raw strings to use a backslash as itself.
not_tab_string = r"\t"
len(not_tab_string) # is 2

# f-string, provides a simple way to substitute values into strings.
first_name = "Jane"
last_name = "Doe"

full_name1 = first_name + " " + last_name             #string addition
full_name2 = "{0} {1}".format(first_name,last_name)   #string.format

full_name3 = f"{first_name} {last_name}"
 