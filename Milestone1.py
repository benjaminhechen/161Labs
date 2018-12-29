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
    
    
def transact(funds, stocks, qty, price, buy=False, sell=False):
    
    
    if buy == sell:
        print("Ambigious transaction! Can't determine whether to buy or sell. No action performed.")    
        return funds, stocks
    elif buy and funds >= qty*price:
        funds -= qty*price
        stocks += qty
        print("Insufficient funds")
        return funds, stocks
    elif sell and stocks >= qty:
        funds += qty*price
        stocks -= qty
        print("Insufficient stock")
        return funds, stocks

def main():
    print(test_data("AAPL.csv", "close", 25))
    

main()
