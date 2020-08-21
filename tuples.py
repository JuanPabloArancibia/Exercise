# n = int(input())
# lst = [int(i) for i in input().split()][:n]
#
# tup = tuple(lst)
# print(hash(tup))

n = int(input())
integer_list = list(map(int, input().split()))[:n]
tup = tuple(integer_list)
print(hash(tup))
