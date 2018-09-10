
#### J Bird Answer
#### read data from input file into inData list
##with open("1a_input.txt") as f:
##    inData = f.readlines()

data_line = []
sum = 0


## jason's answer
with open("1a_input.txt") as f:
    for line in f:
        data_line += line.rstrip()

for i in range(len(data_line)-1):
    if data_line[i] == data_line[i-1]:  ##if current == previous:
        sum += int(data_line[i])             ##sum += current
        
print(sum)

        
## iterate over string as a list of characters
## try comparing with previous, uses wrap around for 1st and last cases

##for line in (##range data_line.len() -1


          
          
          
          
          


                
             

    

