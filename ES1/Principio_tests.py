# -*- coding: utf-8 -*-
"""
Created on Wed May 13 19:05:42 2020

@author: alexp
"""

import Flights as fly

d=['BCN', 'CND', 'BRS']
c=[123, 456, 789]

testing = fly.comprovacion( 4, d, c, 50)
print (testing)

destinos, codigos, precio = fly.append_desti('MAD', 369, 10, d, c, 50)
print (destinos, codigos, precio)

destinos, codigos, precio = fly.delete_desti('MAD', 369, 10,destinos, codigos, precio)
print (destinos, codigos, precio)

destinos, codigos, precio = fly.delete_desti('BCN', 369, 10,destinos, codigos, precio)
print (destinos, codigos, precio)