

def sort_by_age(tuples):
    """Sorts a list of tuples by age."""
    return sorted(tuples, key=lambda x: x[1])

#use case example;

people = [
    ("Brian", 40),
    ("Kevin", 35),
    ("Jeff", 45),
    ("Victor", 25),
    ("Alfred", 5)
]

sorted_people = sort_by_age(people)

print("Sorted by age:")
for person in sorted_people:
    print(f"{person[0]}: {person[1]} years old")