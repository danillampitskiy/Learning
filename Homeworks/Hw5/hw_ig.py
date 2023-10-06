# 1. Implement a function that flatten incoming data:
# non-iterables and elements from iterables (any nesting depth should be supported)
# function should return an iterator (generator function)
# don't use third-party libraries

def merge_elems(*elems):
    for elem in elems:
        if isinstance(elem, str):
            yield from elem
        elif hasattr(elem, '__iter__'):
            yield from merge_elems(*elem)
        else:
            yield elem

# Example input
a = [1, 2, 3]
b = 6
c = 'zhaba'
d = [[1, 2], [3, 4]]

# Output: 1 2 3 6 z h a b a 1 2 3 4
for item in merge_elems(a, b, c, d):
    print(item, end=' ')



# 2. Implement a map-like function that returns an iterator (generator function)
# extra functionality: if arg function can't be applied, return element as is + text exception

def map_like(fun, *elems):
    for elem in elems:
        try:
            yield fun(elem)
        except Exception as e:
            yield f"{elem}: {str(e)}"


# Example input
a = [1, 2, 3]
b = 6
c = 'zhaba'
d = True
fun = lambda x: x[0]

# Output:
# 1
# 6: 'int' object is not subscriptable
# z
# True: 'bool' object is not subscriptable
for result in map_like(fun, a, b, c, d):
    print(result)

