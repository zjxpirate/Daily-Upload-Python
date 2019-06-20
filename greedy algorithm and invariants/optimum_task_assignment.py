

# 2. compute an optimum assignment of tasks

import collections

list1 = [5, 2, 1, 6, 4, 4]

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))

def optimum_task_assignment(task_durations):
    task_durations.sort()
    return [
        PairedTasks(task_durations[i], task_durations[~i])
        for i in range(len(task_durations) // 2)
    ]


print(optimum_task_assignment(list1))



