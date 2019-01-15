

import collections


def examine_buildings_with_sunset(sequence):
    BuildingWithHeight = collections.namedtuple('BuidingWithHeight', ('id', 'height'))

    candidates = []
    for building_idx, building_height in enumerate(sequence):
        print("candidates: ", candidates)
        print("Building Height: ", building_height)
        print("\n")

        while candidates and building_height >= candidates[-1].height:
            # print(building_height)
            # print(candidates[-1])
            candidates.pop()
        candidates.append(BuildingWithHeight(building_idx, building_height))


    print("\n")
    print("Building height east  ----->  west")
    print(sequence)

    print("\nBuilding that has sunset views: ")
    return [c.height for c in reversed(candidates)]




def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))





input = [6, 4, 5, 3, 2, 1]


print(examine_buildings_with_sunset(input))







