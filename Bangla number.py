def f ( n ): 


    if ( n >= 10000000 ):


        f ( math . floor ( n / 10000000 ))


        print ( 'kuti' , end = '' )


        n %= 10000000


    if ( n >= 100000 ):


        f ( math . floor ( n / 100000 ))


        print ( 'lakh' , end = '' )


        n % = 100000


    if ( n >= 1000 ):


        f ( math . floor ( n / 1000 ))


        print ( 'hajar' , end = '' )


        n % = 1000


    if ( n >= 100 ):


        f ( math . floor ( n / 100 ))


        print ( ' shata' , end = '' )


        n % = 100


    if ( n >= 1 ):


        print ( f '  { n } ' , end = '' )


import math 


from sys import stdin   


u = 1


for s in stdin :   


    n = int ( s )


    print ( f ' { u } .' , end = '' )


    if ( n > 0 ):


        f ( n )


            


    else : print ( ' 0' )


    print ( ' \n ' )


    u += 1

