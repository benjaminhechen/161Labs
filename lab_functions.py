def square_each(nums):
 
    for i in range(len(nums)):
        nums[i] = nums[i]*nums[i]
    
def sum_list(nums):
    sum = 0
    
    for i in range(len(nums)):
        sum += nums[i]
        
    return sum

def to_numbers(str_list):
    for i in range(len(str_list)):
         str_list[i] = int(str_list[i])
    
     
def main():
    print("This program computes the sum of the squares of numbers read from a file.")
    filename = input("Please enter the file name:")    
    
    
    file = open(filename)
     
    lines = file.read()
    lineArray = lines.split(',')
    
    to_numbers(lineArray)
    
    square_each(lineArray)
    
    print("The sum of the squares of the numbers in the file is ", sum_list(lineArray))
    
    file.close()

main()
