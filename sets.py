basket = {'banana','orange','apple','pear','orange','banana'}
print(basket)   #prints the sets values without repeating values in set

print('orange' in basket)

print('mango' in basket)

import math
raw_data = [5.3,float('NaN'),5.6,353.5,24.4,float('NaN')]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
        print(filtered_data)

