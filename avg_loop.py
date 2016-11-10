numlist = list() # create empty list
while True : 
	inp = raw_input('enter numbers\n')
	if inp == 'done' : break
	value = float(inp)
    numlist.append(value) # append all numbers into the new list
average = sum(numlist) / len(numlist) # sum is reserved word in python, collects all numbers in list cumulatively
print 'average is' , average 	
