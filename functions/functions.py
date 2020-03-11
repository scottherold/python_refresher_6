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
def center_text(text):
    text = str(text)
    left_margin = (80 - len(text) // 2)
    print(" " * left_margin, text)


# call the function
# when calling the function, you pass it arguments (as the parameter)
center_text("spam and eggs")
center_text("spam, spam and eggs")
center_text(12)
center_text("spam, spam, spam and spam")