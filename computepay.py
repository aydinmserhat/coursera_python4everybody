def computepay(h,r,l,m):
    if h <= l:
    	p=h*r
    	print '$' , p
    else :
    	p=l*r+(h-l)*m
    	print '$' , p
        return p

try :
    inp=input('enter hours\n')
    hrs=float(inp)
    inp_2=input('enter rates under the limit\n')
    rate=float(inp_2)
    inp_3=input('enter your limit of hour\n')
    lim=float(inp_3)
    inp4=input('enter rates passing limit\n')
    rate_much=float(inp4)
except :
    print "ERROR"


print "in the main code" , hrs , rate , lim , rate_much
pay=computepay(hrs,rate,lim,rate_much)
print "we are back" , pay

        

    	
