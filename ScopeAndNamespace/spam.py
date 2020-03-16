# example of multiple nested functions (uncommon)
def spam1():


    def spam2():


        def spam3():
            z = " even more spam"
            # locals() shows the variables, functions and classes local
            # to the current scope
            print("In spam3, the locals are{}".format(locals()))
            return z
        
        y = " more " + x # y must exist before spam3 is called
        y += spam3() # do not combine these assignments
        print("In spam2, the locals are {}".format(locals()))
        return y

    x = "spam" # x must exist before spam2 is called
    x += spam2() # do not comine these assignments
    print("In spam1, the locals are {}".format(locals()))
    return x

print(spam1())
print(locals())
# globals() displays all global variables, functions and classes
print(globals())