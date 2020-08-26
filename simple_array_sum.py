n = int(input())

ar_lst = list(map(int, input().rstrip().split()))
if n == len(ar_lst):
    result = sum(ar_lst)
    print(result)
else:
    print("Mal")





