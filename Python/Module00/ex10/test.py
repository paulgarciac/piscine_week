
# Function returns a generator when it encounters 'yield'.
def simple_generator():
    x = 1
    yield x
    yield x + 1
    yield x + 2

generator_object = simple_generator()
print(generator_object)  # only generator. no code runs. no value gets returned

for i in generator_object:
    print(i)

for i in simple_generator():
    print(i)