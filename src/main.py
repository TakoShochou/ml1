import perceptron as p

data = [ (0, 0), (0, 1), (1, 0), (1, 1) ]

print('perceptron AND demo')
for d in data:
    print(f'{d} -> {p.AND(*d)}')

print('perceptron NAND demo')
for d in data:
    print(f'{d} -> {p.NAND(*d)}')

print('perceptron OR demo')
for d in data:
    print(f'{d} -> {p.OR(*d)}')

print('perceptron XOR demo')
for d in data:
    print(f'{d} -> {p.XOR(*d)}')
