#import sys, os
#sys.path.insert(0, os.path.abspath('...'))

import paquete.funciones as fun
print(fun.eliana(4,2))

def test():
    assert fun.eliana(4,2)==2