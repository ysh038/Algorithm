import sys

n = int(sys.stdin.readline())

people = {}

for i in range(n):
    name,where = sys.stdin.readline().split()
    if where == "enter":
        people[name] = where
    else:
        if name in people:
            people.pop(name)

people = sorted(people,reverse=True)

for person in people:
    print(person)