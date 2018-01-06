# -*- coding: cp1252 -*-
def kostnad(p, r, a):
    k=p+(a+1)*p*r/2
    print "Den totala kostnade efter",a,"år är",int(k),"kr."

kostnad(50000, 0.03, 10)
