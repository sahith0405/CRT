# square pattern
'''n = int(input())
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
'''
# right angle triangle pattern
'''n = int(input())
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()
'''
# inverted right angle triangle pattern
'''n = int(input()) 
for i in range(n):
    for j in range(n - i):
        print("*", end=" ")
    print()
'''
# pyramid pattern
'''n = int(input()) 
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for k in range(2 * i + 1):
        print("*", end=" ")
    print()
'''
# inverted pyramid pattern
'''n = int(input())
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for k in range(2 * (n - i) - 1):
        print("*", end=" ")
    print()
'''
# diamond pattern
'''n = int(input())
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for k in range(2 * i + 1):
        print("*", end=" ")
    print()
for i in range(n - 1):
    for j in range(i + 1):
        print(" ", end=" ")
    for k in range(2 * (n - i - 1) - 1):
        print("*", end=" ")
    print()'''
# number pattern
'''n = int(input())
for i in range(n):
    for j in range(i + 1):
        print(j + 1, end=" ")
    print()'''

# Alphabet pattern
'''n = int(input())
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()'''  
# Floyd's triangle 
'''n = int(input())
num = 1 
for i in range(n):
    for j in range(i + 1):
        print(num, end=" ")
        num += 1
    print()'''

# hollow square pattern
'''n = int(input()) 
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''
