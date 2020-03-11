# fun with python functions
# python syntax expects two blank lines before a function defintion 
# (not including comments)


# define a function
def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text) // 2)


# the 'parameter' defines the data the function takes
# if a parameter is referenced with a '*', it represents that the
# parameter can be multiple arguments entered
# default values can be set as paremeters
def center_text(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    # converts args into text string
    # the separator is now set as an argument, and is dynamic based on
    # input into the function by an argument, or defaults to a space
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text) // 2)
    # text variable is sliced to remove final separator
    print(" " * left_margin, text[:-1], end=end, file=file, flush=flush)


# call the function
# when calling the function, you pass it arguments (as the parameter)
center_text("spam and eggs")
center_text("spam, spam and eggs")
center_text(12)
center_text("spam, spam, spam and spam")
center_text("first", "second", 3, 4, "spam", sep=":")