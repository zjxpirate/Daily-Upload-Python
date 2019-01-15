

import collections


def examine_buildings_with_sunset(sequence):
    BuildingWithHeight = collections.namedtuple('BuidingWithHeight', ('id', 'height'))

    candidates = []
    for building_idx, building_height in enumerate(sequence):
        print(building_idx)

        while candidates and building_height >= candidates[-1].height:
            candidates.pop()
        candidates.append(BuildingWithHeight(building_idx, building_height))


    print("\n")
    print(sequence)
    print("Have view of sunset")
    print("east  ----->  west")

    return [c.id+1 for c in reversed(candidates)]




def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))





input = [1, 2, 3, 4, 5, 6, 7]


print(examine_buildings_with_sunset(input))







