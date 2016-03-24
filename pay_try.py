try :
    inp=input('enter hours\n')
    hrs=float(inp)
    inp_2=input('enter rates under the limit\n')
    rate=float(inp_2)
    inp_3=input('enter your limit of hour\n')
    lim=float(inp_3)
    inp4=input('enter rates passing limit\n')
    rate_much=float(inp4)
    if hrs <= lim:
        pay=hrs*rate
        print '$' , pay
    else :
        pay=lim*rate+(hrs-lim)*rate_much
        print '$' , pay
except :
    print "error" 