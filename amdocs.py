#from scipy.spatial.distance import pdist
import math
import decimal
from itertools import repeat
def truncate(number, digits) -> float:
    stepper = pow(10.0, digits)
    return math.trunc(stepper * number) / stepper
def distance(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return math.hypot(x2-x1,y2-y1)
def main():
    testcases=int(input())
    output=[]
    #print(testcases)
    for i in range(0, testcases):
        L=int(input())
        #print (L)
        shipcoordinates=[]
        for j in range(0, L):
            x = list(map(int, input().split()))
            shipcoordinates.append(x)
        for m in range(0,len(shipcoordinates)):
            pOne = shipcoordinates[m]
            radius=[]
            
            for item in range(0,len(shipcoordinates)):
                 if (m!=item):
                     #print('pOne',pOne)
                     pTwo = shipcoordinates[item]
                     #print('pTwo',pTwo )
                     #coordDist = truncate(distance(pOne,pTwo),2)
                     coordDist = distance(pOne,pTwo)
                     #print('coordDist',coordDist )
                     radius.append(coordDist)
            #effdist=decimal.Decimal(min(radius)).quantize(decimal.Decimal(".01"))
            effdist=min(radius)
            count = 0
            diam=effdist*2
            #print ('effdist',effdist)
            #print ('diam',diam)
            for r in radius[0:]:
                        if (r <= diam): 
                           #print(r)
                           count = count + 1
            final=decimal.Decimal(effdist).quantize(decimal.Decimal(".01"))
            output.append((final,count))
    for item in output:
        print  (item[0]," ".join(map(str, item[1:])))

    
main()