# S, N = input(), int(input())
# for part in zip(*[iter(S)] * N):
#     d = dict()
#     print(''.join([d.setdefault(c, c) for c in part if c not in d]))
#
#
# for n in zip(*[iter(S)] * N):
#     print(n)

lst = [1, 2, 2, 3, 6, 7, 8, 9, 12, 54]
lst_iter = [iter(lst)]
for n in zip(*lst_iter):
    print(n)
print(lst_iter)

# for i in zip(*[iter(lst)] * N):
#     print(i)