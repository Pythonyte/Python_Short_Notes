'''
A ChainMap is a class from the collections module that provides the ability to link multiple mappings together such that they end up being a single unit. If you look at the documentation, you will notice that it accepts *maps, which means that a ChainMap will accept any number of mappings or dictionaries and turn them into a single view that you can update. Let’s look at an example so you can see how this works:


'''
from collections import ChainMap
car_parts = {'hood': 500, 'engine': 5000, 'front_door': 750}
car_options = {'A/C': 1000, 'Turbo': 2500, 'rollbar': 300}
car_accessories = {'cover': 100, 'hood_ornament': 150, 'seat_cover': 99}
car_pricing = ChainMap(car_accessories, car_options, car_parts)

print(car_pricing)
print(car_pricing['hood'])

'''
if we get duplicate keys after combining all maps, the ChainMap will contain all values and go through each map in order to see if that key exists and has a value. If it does, then the ChainMap will return the first value it finds that matches that key.
'''

car_accessories = {'cover': 100, 'hood':230,'hood_ornament': 150, 'seat_cover': 99}
car_pricing = ChainMap(car_accessories, car_options, car_parts)
print(car_pricing)
print(car_pricing['hood'])
