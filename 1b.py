
##Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list. That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it. Fortunately, your list has an even number of elements.


data_line = []
sum = 0


with open("1a_input.txt") as f:
    for line in f:
        data_line += line.rstrip()

for i in range(len(data_line)-1):
    if data_line[i] == data_line[int(i - (len(data_line)/2))]:  ##if current == half way around list:
        sum += int(data_line[i])             ##sum += current
        
print(sum)

        



          
          
          
          
          


                
             

    

