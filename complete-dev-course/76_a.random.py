import random

# random float between 0 and 1
print(random.random())

# select number between 1 and 10
print(random.randint(1,10))

# Print integer from range with specified step
print(random.randrange(0, 101, 7))

items = ['here', 'are', 'some', 'strings', 'of',
         'which', 'we', 'will', 'select', 'one']

# Select random item from the list
print(random.choice(items))

# Select random X amount of items from the list
for item in random.sample(items, 3):
    print(item, end=' '),



