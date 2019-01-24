

import heapq



list1 = [5, 7, 9, 1, 3]

heapq.heapify(list1)

heapq.heappush(list1, 4)

heapq.heappush(list1, 11)

print(list1)

print(heapq.nsmallest(2, list1))

print(heapq.nlargest(3, list1))

print("heap pop: ", heapq.heappop(list1))

print("after pop: ", list1)


print("heap push pop: ", heapq.heappushpop(list1, 16))

print("The new heap: ", list1)
