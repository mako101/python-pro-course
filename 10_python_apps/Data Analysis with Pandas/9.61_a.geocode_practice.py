from geopy.geocoders import *

gl = Nominatim()

address = gl.geocode('Muralla romana de Lugo, Roman City Walls, El Carmen, Lugo, Galicia, 27001, Spain')

print(address, '\n')

print(address.latitude, address.longitude, address.altitude, '\n')

for x, y in address.raw.items():
    # if x == 'type' or x == 'display_name':
    #     print(x, ':', y)
    print(x, ':', y)

print('\n' * 2)

coordinates = gl.reverse('51.4871143, -0.2160496')

print(coordinates, '\n')

for x,y in coordinates.raw.items():
    print(x, ':', y)
