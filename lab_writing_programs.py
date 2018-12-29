def main():
    print("This is a calculator.")
    x = eval(input("How many calculations would you like to evaluate?"))
    
    for i in range(x):
        userInput = input("Enter a Mathematical Expression:")
        evalUserInput = eval(userInput)
        print(userInput + "=" + str(evalUserInput))
        
main()

#changes made in lines 7 and 9 for extra credit (user input taken in and range arg adjusted)
#pretty-printed changes made for extra credit at lines 10, 11, 12
