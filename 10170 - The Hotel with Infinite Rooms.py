
"""


S+(S+1)+(S+2)+……+n=((S+n)×(n–S+1))/2 (Arithmetic series trapezoidal formula) ≤ D (n is the minimum integer value of this formula)


"""


from sys import stdin   


import math 


for f in stdin :   


    all = 0


    S , D = map ( int , f . split ())


    f =( 2 * D )+( S * S )- S


    ans =((- 1 +(( 1 -( 4 *(- f )))** 0.5 ))/ 2 )


    print ( math . ceil ( ans ))