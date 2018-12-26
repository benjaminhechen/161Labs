"""
Benjamin Chen
CSC161 Lab8 TR 1230-145
"""
def get_input():
    while True:
        userNum = eval(input("Please enter an even integer larger than 2: "))
        try:
            int(userNum)
        except ValueError:
            print("Bad Input")
        if userNum % 2 != 0 or userNum <= 2:
            print("Wrong Input")
        else:
            return userNum
    
    

def is_prime(n):
    i = 5
    if n < 1 or n == 1:
        return False
    elif n < 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    while (i*i < n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    

def main():    
    i = 0
    j = 0
    
    num = get_input()
     
    while i < num:
        j = num - i
        #print(i, j)
        if is_prime(i) and is_prime(j):
            print(str(num) + "=" + str(i) + "+" + str(j))
            break
        else:
            i += 1
    
    if not is_prime(i) or not is_prime(j):
        print("Goldbach's conjecture doesn't hold for " + str(num))
    
    
main()