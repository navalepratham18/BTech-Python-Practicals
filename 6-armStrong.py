def armStrong(start, end):
    for num in range(start, end + 1):
        digits = str(num)
        arm = 0 
        
        leng = len(str(digits))
        
        for digit in digits:
            arm += int(digit)**leng
            
        if arm == num:
            print(num)

start = int(input("Enter the starting point : "))
end = int(input("Enter the ending point : "))
armStrong(start, end)