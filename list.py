lst = []
n = int(input())

operations = [input() for _ in range(n)]

commands = {
    'insert': lambda idx, val: lst.insert(int(idx), int(val)),
    'print': lambda: print(lst),
    'remove': lambda val: lst.remove(int(val)),
    'append': lambda val: lst.append(int(val)),
    'sort': lambda: lst.sort(),
    'pop': lambda: lst.pop(),
    'reverse': lambda: lst.reverse()
}


for operation in operations:
    name, *args = operation.split()
    command = commands.get(name)
    command(*args)
