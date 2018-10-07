##http://adventofcode.com/2017/day/2
##
##--- Day 2: Corruption Checksum ---
##As you walk through the door, a glowing humanoid shape yells in your direction. "You there! Your state appears to be idle. Come help us repair the corruption in this spreadsheet - if we take another millisecond, we'll have to display an hourglass cursor!"
##
##The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum. For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.
##
##For example, given the following spreadsheet:
##
##5 1 9 5
##7 5 3
##2 4 6 8
##The first row's largest and smallest values are 9 and 1, and their difference is 8.
##The second row's largest and smallest values are 7 and 3, and their difference is 4.
##The third row's difference is 6.
##In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.
##
##What is the checksum for the spreadsheet in your puzzle input?


##ALGORITHM
##-read input row by row
##-sort smallest to largest
##-sum += largest minus smallest
##-return sum


dataLine = []
sum =0

with open("2ainput.txt") as dataFile:
    for row in dataFile:
        dataLine.append([int(x) for x in row.split()]) #read into list as lists of integers (each row of numbers = 1 list, all rows live in main list dataLine)

    for row in dataLine:    
        row.sort()                      #sort each row, smallest to largest
        sum += row[-1] - row[0]         #sum += largest minus smallest
 #       print(row)                     #printouts to help visually track what's going on
#        print("largest:", row[-1], " minus smallest:", row[0], "equals:", (row[-1] - row[0]))
#        print(sum)
        
print(sum)



    
