"""PERSON: NAME, AGE, HEIGHT"""
person_list = []
while True:
    person = input()
    if not person:
        break
    person_list.append(tuple(person.split(",")))

person_list = sorted(person_list, key = lambda p: (p[0], p[1], p[2]))
print(person_list)
