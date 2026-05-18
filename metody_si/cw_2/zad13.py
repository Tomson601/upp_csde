# Napisać program, który utworzy listę 20 liczb całkowitych z przedziału 1...10, a następnie wypisze na ekranie ile razy każda z liczb z tego
# przedziału powtarza siew liscie.
# Przykład: wylosowane liczby: 6 5 4 5 10 5 8 3 10 6 6 6 4 3 2 8 1 3 4 7
# Wystąpienia:
# 1 – 1
# 2 – 1
# 3 – 3
# 4 – 3
# 5 – 3
# 6 – 4
# 7 – 1
# 8 – 2
# 9 – 0
#10 - 2

import random

random_list = []

for i in range(20):
    random_list.append(random.randint(1, 10))

print("Wylosowane liczby: ", random_list)

for num in range(1, 11):
    count = random_list.count(num)
    print(f"{num} - {count}")

