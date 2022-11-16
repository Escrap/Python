# x = input("What's X?")

    # SyntaxError: unterminated string literal (detected at line 2) input handles strings or "literals" add int

#x = int(input("What's X?"))
#print(f"x is {x}")

        # What if some user enters cat
        # Output =   x = int(input("What's X?"))
                #ValueError: invalid literal for int() with base 10: 'cat'

        # Type of error handling with "try" and "except" keywords

#try:
#
#    x = int(input("What's X? "))
#
#except ValueError:
#    print("x is not an integer")
#    
#else:
#    print(f"x is {x}")



# Reprompt Break with loop
# Add in a loop to prompt user for x as an int

#while True:
#    try:
#        x = int(input("What's X? "))
#    except ValueError:
#        print("x is not an integer")
#    else:
#        break
#
#print(f"x is {x}")

# What if you want more numbers later
# Create your own function get_int

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's X? "))
        except ValueError:
            print("x is not an integer")
        else:
            
            return x
main()
# above is not running and I don't know why remember to call main