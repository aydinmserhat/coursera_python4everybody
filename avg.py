# using infinite loop to calculate avarage until typing the "done".
count = 0
total = 0
while True: 
    inp=raw_input('enter a number\n')
	if inp == 'done' : 
        break
	if len(inp) < 1	:
		break

	# do the work
    try :
    	num = float(inp)
    except:
    	print 'invalid input'
        continue

    count = count + 1
    total = total + num
    print num, total, count

print 'avarage is\n', total / count







