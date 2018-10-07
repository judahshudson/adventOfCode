##http://adventofcode.com/2017/day/2
##
##  DESCRIPTION
##--- Day 2: Corruption Checksum ---
##--- Part Two ---
##"Great work; looks like we're on the right track after all. Here's a star for your effort." However, the program seems a little worried. Can programs be worried?
##
##"Based on what we're seeing, it looks like all the User wanted is some information about the evenly divisible values in the spreadsheet. Unfortunately, none of us are equipped for that kind of calculation - most of us specialize in bitwise operations."
##
##It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - that is, where the result of the division operation is a whole number. They would like you to find those numbers on each line, divide them, and add up each line's result.
##
##For example, given the following spreadsheet:
##
##5 9 2 8
##9 4 7 3
##3 8 6 5
##In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
##In the second row, the two numbers are 9 and 3; the result is 3.
##In the third row, the result is 2.
##In this example, the sum of the results would be 4 + 3 + 2 = 9.
##
##What is the sum of each row's result in your puzzle input?


##  ALGORITHM
##-read input row by row
##-sort smallest to largest
##-find the only two numbers in each row where one evenly divides the other
##    *start with the largest number
##    check if the next (smaller) number divides it evenly
##    go down line until last num
##    *next take second largest number
##    *repeat checks all the way down to last num
##    *finally move down to second to last num, see if last/smallest num divides it evenly
##-as soon as evenly divided nums are found, sum += their quotient
##-return sum


#   CODE
dataLine = []
sum =0

with open("2ainput.txt") as dataFile:
    for row in dataFile:
        dataLine.append([int(x) for x in row.split()]) #read into list as lists of integers (each row of numbers = 1 list, all rows live in main list dataLine)
        #print("dataLine:", dataLine)   # ***FIX ME*** test printout
        #print()   # ***FIX ME*** test printout
    for row in dataLine:    
        row.sort(reverse=True)          #sort each row, smallest to largest
        #print("row reversed: ", row)   # ***FIX ME*** test printout
        #print()    # ***FIX ME*** test printout
        for i in range(len(row)-1):         #yields exact same answer as code option above
            for n in range(i+1, len(row)-1):
                if row[i] % row[n] == 0:
                    print(row[i], " / ", row[n], " = ", row[i]/row[n],)   # ***FIX ME*** test printout
                    sum += row[i] / row[n]            
print("Sum: ", sum)




#   CODE 1st TRY    (wrong: 2nd level loop iterates over entire list, instead of stepping down chain)
'''
#CODE
dataLine = []
sum =0

with open("2ainput.txt") as dataFile:
    for row in dataFile:
        dataLine.append([int(x) for x in row.split()]) #read into list as lists of integers (each row of numbers = 1 list, all rows live in main list dataLine)
        for row in dataLine:    
            row.sort(reverse=True)          #sort each row, smallest to largest

            for i in row:                       #loop; iterate over entire row, i		            
                for n in range(1, len(row)-1):     #2nd level of iteration, n
                    if i % row[n] == 0:         #see if i(1st level loop) is evenly divisible by n(2nd level)
                        sum += i / row[n]       #if we have a winner, add the quotient to our storage variable "sum"                        
print(sum)
'''

#   ***EXPORE SOLUTIONS***
'''
-code runs
-yields incorrect answer
-iteration logic and flow control seem correct
-check:
    *bounds
    *math
    *run with small data set, use step print()'s to track progress
'''


#   1st try code w/ test printout statemens
'''
            for i in row:                       #loop; iterate over entire row, i		            
                for n in range(1, len(row)-1):     #2nd level of iteration, n
                    if i % row[n] == 0:         #see if i(1st level loop) is evenly divisible by n(2nd level)
                        print(i, " / ", row[n], " = ", i/row[n],)   # ***FIX ME*** test printout
                        sum += i / row[n]       #if we have a winner, add the quotient to our storage variable "sum"            
'''
    
    

    
