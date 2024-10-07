class GoatNotFoundException(Exception):
    print("inside")
    pass

try:
    raise GoatNotFoundException()
except GoatNotFoundException:
    print('Goat not found!')