"""
print("meow")
print("meow")
print("meow")
"""
"""
mensage = input("What mensage do you want to print? ")
i = input("How many times do you what to print the mensage? ")
i = int(i)
while i != 0:
    print(mensage)
    i = i - 1
"""
"""
for i in [0, 1, 2, 3, 4]:
    print("meow")
"""
"""
for i in range(100000):
    print("meow", i+1)
"""
"""
print("meow\n" * 3, end="")
"""
"""
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
"""

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()