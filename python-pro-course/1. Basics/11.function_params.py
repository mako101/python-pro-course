def house(no_of_doors=2, no_of_windows=5, roof_type='tiled'):
    print('This House will have:')
    print(no_of_doors, 'doors')
    print(no_of_windows, 'windows')
    print('And a', roof_type, 'roof')
    print()

house(roof_type='thatched', no_of_windows=7)

house('foobar', 'nutta', 3)