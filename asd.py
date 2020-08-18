from collections import Counter

def maximumOccurringCharacter(text):
    # Write your code here
    char = Counter(text).most_common(1)[0][0]
    return



maximumOccurringCharacter("helloworld")

set = {1, 1, 1, 4, 4, 5, 8, 7, 9}
list = list(set)
list.sort(reverse=False)
print(list)
print(set)
