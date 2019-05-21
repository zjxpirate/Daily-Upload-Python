

import collections

# 10. Partitioning and sorting an array with many repeated entries

Person = collections.namedtuple('Person', ('age', 'name'))

seq = [Person(age=13, name='David'),
       Person(age=15, name='Bob'),
       Person(age=13, name='Chip'),
       Person(age=14, name='Tim'),
       Person(age=15, name='Joe')
]

print(seq)

def group_by_age(people):
    age_to_count = collections.Counter((person.age for person in people))
    print("age_to_count: ", age_to_count)

    age_to_offset, offset = {}, 0
    for age, count in age_to_count.items():
        age_to_offset[age] = offset
        offset += count

    print("age_to_offset: ", age_to_offset)
# [Person(age=13, name='David'), Person(age=15, name='Alex'), Person(age=14, name='Andy'), Person(age=13, name='Jim'), Person(age=15, name='Phil'), Person(age=15, name='Bob'), Person(age=13, name='Chip'), Person(age=14, name='Tim')]
    while age_to_offset:

        from_age = next(iter(age_to_offset))
        print("from_age", from_age)

        from_idx = age_to_offset[from_age]
        print("from_idx: ", from_idx)

        to_age = people[from_idx].age
        print("to_age: ", to_age)

        to_idx = age_to_offset[people[from_idx].age]
        print("to_idx: ", to_idx)


        print("people[from_idx]: ", people[from_idx])
        print("people[to_idx]: ", people[to_idx])
        people[from_idx], people[to_idx] = people[to_idx], people[from_idx]
        print("people[from_idx]: ", people[from_idx])
        print("people[to_idx]: ", people[to_idx])


        # use age_to_count to see when we are finished with a particular age
        age_to_count[to_age] -= 1

        if age_to_count[to_age]:
            age_to_offset[to_age] = to_idx + 1
        else:
            del age_to_offset[to_age]

group_by_age(seq)

print(seq)










