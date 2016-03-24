def computescore(s):
    if s >= 0.9 and s <= 1.0:
        print 'grade is A'
    elif s >= 0.8 and s<=1.0 :
	    print 'grade is B'
    elif s >= 0.7 and s<=1.0 :
	    print 'grade is C'
    elif s >= 0.6 and s <= 1.0 :
	    print 'grade is D'
    elif s >= 0.0 and s <= 0.6 :
	    print 'grade is F'
    else :
        print 'ERROR'
    return s

inp=input('enter numberscore\n')
score=float(inp)
result=computescore(score)
print "we are back" , result
