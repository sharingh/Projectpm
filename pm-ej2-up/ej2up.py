import collections

#####################################################################
# Ejercicio 2

import json
repetidos = [1,2,3,"1","2","3",3,4,5]
r = [1,"5",2,"3"]
d_str = '{"valor":125.3,"codigo":123}'

#####################################################################
print('')
# Ej2.1

# Si solo es sacar los que se repiten

print([x for x in set(repetidos)])

# Sino arma una lista sin los que se repiten

print("************************")

print([x for x, y in collections.Counter(repetidos).items() if y == 1])

#####################################################################
print('')
# Ej2.2

def repeat(a, b):
    return list(set(a) & set(b))
print(repeat(repetidos, r))

#####################################################################
print('')
# Ej2.3
dic = json.loads(d_str)
print(type(dic))
print('')
#####################################################################
