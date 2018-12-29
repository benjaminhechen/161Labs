stocks = 0
funds = 1000

def test_data(filename, col, day):

    Date = []
    Open = []
    High = []
    Low = []
    Close = []
    AdjClose = []
    Volume = []
    
    file = open(filename, "r")
    file.readline() # to get rid of titles
    for line in file:

        temp = line.split(",")
        Date.append(temp[0])
        Open.append(temp[1])
        High.append(temp[2])
        Low.append(temp[3])  
        Close.append(temp[4])  
        AdjClose.append(temp[5])  
        Volume.append(temp[6])  
    
    if col == 'date':
        return float(Date[day-1])
    elif col == 'open':
        return float(Open[day-1])
    elif col == 'high':
        return float(High[day-1])
    elif col == 'low':
        return float(Low[day-1])
    elif col == 'close':
        return float(Close[day-1])
    elif col == 'adj_close':
        return float(AdjClose[day-1])
    elif col == 'volume':
        return float(Volume[day-1])
    
    
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
    
def main():
    
    global funds
    global stocks
    
    stocks = 0
    funds = 1000
    
    filename = input("Enter a filename for stock data (CSV format): ")
    alg1_stocks, alg1_balance = alg_moving_average(filename)
    
    print("The results are: " + str(alg1_stocks) + " stocks, balance of " + str(alg1_balance))

    stocks = 0
    funds = 1000
    
    
    #not sure why it makes 1359100 for AAPL, but only 5187 for MSFT
main()

if __name__ == '__name__':
    main()
