import math
limit = float(input("Enter the limit on queue length, -1 for infinity "))
c = float(input("Enter the number of servers "))
l = float(input("Enter the arrival rate "))
mu = float(input("Enter the service rate "))
noq=0
rho = l/mu
ls=0
lq=0
ws=0
wq=0
p0=0
if limit==-1 and c==1:
   p0 = 1 - rho
   ls = rho/p0
   lq = pow(rho,2)/p0
   ws = ls/l
   wq = lq/l
if limit!=-1 and c==1:
    p0 = (1-rho)/(1-pow(rho,limit+1))
    ls = (rho*(1+ limit*pow(rho,limit+1) -(limit+1)*pow(rho,limit)))/((1-rho)*(1-pow(rho,limit+1)))
    me = l*(1 - pow(rho,limit)*p0)
    lq = ls - (me/mu)
    ws = ls/me
    wq = lq/me
if limit==-1 and c!=1:
    d = rho/c
    count = c
    i = 0
    cal = 0
    while i<count:
        cal += pow(rho,i)/math.factorial(i)
        i=i+1
    cal1 = (pow(rho,c)/(math.factorial(c)))*(1/(1-d))
    p0 = 1/(cal1 + cal)
    lq = pow(rho,c+1)*p0/(math.factorial(c-1)*(pow(c-rho,2)))
    ls = lq +rho
    ws = ls/l
    wq = lq/l
    i=0
    noq=0
    while i<=count:
        noq += (pow(rho,i)*p0/(math.factorial(i)))
        i=i+1
else:
    d = rho/c
    count = c
    i = 0
    cal = 0
    while i<count:
        cal += pow(rho,i)/math.factorial(i)
        i=i+1
    cal1 = (1 - pow(d,limit-c+1))/(1-d)
    p0 = 1/(cal + (cal1)*pow(rho,c)/(math.factorial(c)))
    i=0
    noq=0
    while i<=count:
        noq += (pow(l,i)*p0)/(math.factorial(i)*pow(mu,i))
        i=i+1
    mal = (pow(rho,c+1)*p0)/((math.factorial(c-1))*(pow((c-rho),2)))
    mal2 = 1 - (pow((d),limit-c+1)) - ((limit-c+1)*(1-d)*pow(d,limit-c))
    lq = (mal*mal2)
    ls = lq + rho
    ws = ls/l
    wq = lq/l
    pn = (pow(rho,limit)*p0)/(math.factorial(c)*pow(c,limit-c))
print("p0 = ",p0)
print()
print("length of system =",ls)
print()
print("length of queue =",lq)
print()
print("waiting time of server in min =",ws*60)
print()
print("waiting time of queue in min =",wq*60)
print()
print("p2(valid only if number of server is 1) =",pow(rho,2)*p0)
print()
print("no queue =", noq)
print("waiting time of server in hrs =",ws)
print()
print("waiting time of queue in hrs =",wq)
print()
