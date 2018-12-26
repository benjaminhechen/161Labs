"""
Benjamin Chen
CSC161 Project Milestone 2 TR 1230-145
"""

stocks = 0
funds = 1000
    
def transact(funds1, stocks1, qty, price, buy=False, sell=False):
    global funds
    global stocks
    
    if buy == sell:
        #print("Ambigious transaction! Can't determine whether to buy or sell. No action performed.")    
        return funds, stocks
    elif buy and funds >= qty*price:
        funds -= qty*price
        stocks += qty
        #print("Insufficient funds")
        return funds, stocks
    elif sell and stocks >= qty:
        funds += qty*price
        stocks -= qty
        #print("Insufficient stock")
        return funds, stocks

def alg_moving_average(filename):
    global funds
    global stocks
    
    Prices = [] #open column for prices
    file = open(filename, "r")
    file.readline() # to get rid of titles
    for line in file:
        temp = line.split(",")
        Prices.append(float(temp[1]))

    i = 21
    while i < len(Prices):
        total = 0
    
        j = i-21
        while j < i:
            total += Prices[j]
            j += 1
            
        movAvg = total/20
        
        if i == len(Prices):
            transact(funds, stocks, stocks, Prices[i], buy=False, sell=True)
        elif Prices[i] > movAvg*1.05:
            transact(funds, stocks, 10, Prices[i], buy=False, sell=True)
        elif Prices[i] < movAvg*0.95:
            transact(funds, stocks, 10, Prices[i], buy=True, sell=False)
        i += 1
        
    transact(funds, stocks, stocks, Prices[i-1], buy=False, sell=True)
    
    return(stocks, funds)

'''
Custom Algorithm:
First, for each day, we take in the high and the low prices and take the difference.
We take that difference and cast it as an integer, then get the binary value of that integer
If the sum of the 0s and 1s is odd, buy 5 stocks at the opening price, if even, sell 5 stocks at the opening price
'''   
    
def alg_mine(filename):
    global funds
    global stocks
    
    #create 3 arrays to hold values
    PricesOpen = [] 
    PricesHigh = []
    PricesLow = []
    file = open(filename, "r")
    file.readline() # to get rid of titles
    for line in file:
        temp = line.split(",")
        #load the prices in the arrays
        PricesOpen.append(float(temp[1]))
        PricesHigh.append(float(temp[2]))
        PricesLow.append(float(temp[3]))
     
    commands = []    
    s = 0
    for i in range(len(PricesHigh)):
        #calculate the difference
        difference = PricesHigh[i] - PricesLow[i]
        #conver to binary
        binary = "{0:b}".format(int(difference))
        
        #calculate sum, then mod sum
        s = 0
        binaryStr = str(binary)
        
        for i in binaryStr:
            s += int(i)
            
        commands.append(s%2)
    
    j=0
    while j < len(PricesOpen):
        if j == len(PricesOpen):
            #if last day, sell everything
            transact(funds, stocks, stocks, PricesOpen[j], buy=False, sell=True)
        elif commands[j] == 1:
            #if odd, buy
            transact(funds, stocks, 5, PricesOpen[j], buy=True, sell=False)
        elif commands[j] == 0:
            #if even, sell
            transact(funds, stocks, 5, PricesOpen[j], buy=False, sell=True)
        j+=1
    
    #sell everything just in case
    transact(funds, stocks, stocks, PricesOpen[j-1], buy=False, sell=True)    
    
    return(stocks, funds)

def main():
    
    global funds
    global stocks
    
    stocks = 0
    funds = 1000
    
    filename = input("Enter a filename for stock data (CSV format): ")
    alg1_stocks, alg1_balance = alg_moving_average(filename)
    
    print("The results for the moving average are: " + str(alg1_stocks) + " stocks, balance of " + str(alg1_balance))

    stocks = 0
    funds = 1000
    
    
    alg2_stocks, alg2_balance = alg_mine(filename)
    print("The results for the custom algorithm are: " + str(alg2_stocks) + " stocks, balance of " + str(alg2_balance))
    
    stocks = 0
    funds = 1000
    
main()

if __name__ == '__name__':
    main()