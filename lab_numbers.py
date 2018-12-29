from math import sqrt

def main():
    print("This program calculate the square root of a given number using the Newton's method")
    x = eval(input("What is the number for which you want to calculate the square root?"))
    n = eval(input("How many iterations do you want to use?"))
    trueSqrt = sqrt(x)
    
    guess = x/2
    for i in range(n):
        guess=(guess+x/guess)/2
        print(guess)
        
    print("The difference between my guess and the real result is " + str(trueSqrt--guess))

main()
