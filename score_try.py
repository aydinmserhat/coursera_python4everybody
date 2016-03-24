try :
    inp=input('enter numberscore\n')
    score=float(inp)
    if score >= 0.9 and score <= 1.0:
        print 'grade is A'
    elif score >= 0.8 and score<=1.0 :
        print 'grade is B'
    elif score >= 0.7 and score<=1.0 :
        print 'grade is C'
    elif score >= 0.6 and score<=1.0 :
        print 'grade is D'
    elif score >= 0.0 and score <= 0.6 :
        print 'grade is F'
    else :
        print 'ERROR'
except:
    print 'bad score'


