
from sys import stdin   


for f in stdin :   


    n , m = map ( int , f . split ())


    arr = [ n ]


    s = 0 #S is used as the output mechanism 


    w = 0


    if ( m == 0 or m == 1 ):  


        print ( 'Boring!' )


        w += 1


    if ( w == 0 ):


        while  ( n % m == 0 ):


            arr . append ( n // m )


            if ( n // m == 1 ): break


            n = n // m


        if ( n % m != 0 ):


            s += 1


            print ( 'Boring!' )


        if ( s == 0 ):


            print (* arr )   