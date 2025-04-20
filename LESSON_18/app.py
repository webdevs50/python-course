## Modules
import converters  # Importing the whole module

print(converters.kg_to_lbs(70))

## Also, we can import only a specific function from a module
from converters import lbs_to_kg

print(lbs_to_kg(235))


import utils

print(utils.find_max([20, 33, 11, 23, 14, 55, 6, 70]))


## First way of importanting a module from a package
import ecommerce.shipping

print(ecommerce.shipping.calc_shipping())

## Second best apparoach of importing a module from a package

from ecommerce.shipping import calc_shipping
print("Simple way of module importing")
print(calc_shipping())