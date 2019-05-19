
import collections

# 7. render a calendar


# event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

# Endpoint is a tuple (start_time, 0) or (end_time, 1) so that if times
# are equal, start_time comes first
Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))

def find_max_simultaneous_events(A):

    # builds an array of all endpoints.
    E = [
        p for event in A for p in (Endpoint(event.start, True), Endpoint(event.finish, False))
    ]

    # sorts the endpoint array according to the time, record the maximum number of simultaneous events
    E.sort(key=lambda e: (e.time, not e.is_start))

    # track the number of simultaneous events, record the maximum number of simultaneous events
    max_num_simultaneous_events, num_simultaneous_events = 0, 0

    for e in E:
        if e.is_start:
            num_simultaneous_events += 1
            max_num_simultaneous_events = max(num_simultaneous_events, max_num_simultaneous_events)
        else:
            num_simultaneous_events -= 1

    return max_num_simultaneous_events




