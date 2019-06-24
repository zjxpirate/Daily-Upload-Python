

# 1. graphs boot camp

import collections

MatchResult = collections.namedtuple('MatchResult', ('winning_team', 'losing_team'))

list1 = [MatchResult(winning_team='B', losing_team='D'),
         MatchResult(winning_team='B', losing_team='E'),
         MatchResult(winning_team='C', losing_team='F'),
         MatchResult(winning_team='A', losing_team='B'),
         MatchResult(winning_team='A', losing_team='C')]

def can_team_a_beat_team_b(matches, team_a, team_b):

    def build_graph():
        graph = collections.defaultdict(set)
        for match in matches:
            graph[match.winning_team].add(match.losing_team)
        return graph

    def is_reachable_dfs(graph, curr, dest, visited=set()):
        if curr == dest:
            return True
        elif curr in visited or curr not in graph:
            return False
        visited.add(curr)
        return any(is_reachable_dfs(graph, team, dest) for team in graph[curr])

    return is_reachable_dfs(build_graph(), team_a, team_b)


print(can_team_a_beat_team_b(list1, 'B', 'D'))

