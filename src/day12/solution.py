import re


def create_graph(data):
    graph = dict()
    for a, b in data:
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)
    return graph


def recurse_node(graph, start_node, paths, visited=list()):
    if start_node == "end":
        return visited

    visited_without_large = [x for x in visited if re.match(r"^[a-z]*$", x)]

    for node in graph[start_node].difference(visited_without_large):

        visited_copy = [x for x in visited] + [node]
        result = [recurse_node(graph, visited_copy[-1], paths, visited_copy)]
        if result[0]:
            paths += result

    return []


# visit small caves at most once
def part1(data):
    graph = create_graph(data)

    paths = []
    start = "start"
    recurse_node(graph, "start", paths, [start])
    return len(paths)


################################################################################


def recurse_node_part2(graph, start_node, paths, visited=list()):
    if start_node == "end":
        return visited

    for node in graph[start_node].difference(["start"]):

        duplicates = [
            x
            for x in visited
            if visited.count(x) > 1
            and re.match(r"^[a-z]*$", x)
            and x != "start"
            and x != "end"
        ]

        if re.match(r"^[a-z]*$", node):
            if duplicates:
                if node in visited:
                    continue

        visited_copy = [x for x in visited] + [node]

        result = [recurse_node_part2(graph, visited_copy[-1], paths, visited_copy)]
        if result[0]:
            paths += result

    return []


# visit one small cave at most twice, rest at most once
def part2(data):
    graph = create_graph(data)

    paths = []
    start = "start"
    recurse_node_part2(graph, "start", paths, [start])
    paths.sort()
    return len(paths)


data = open("src/day12/input.txt", "r").readlines()  # 3576, 84271
# data = open("src/day12/example3.txt", "r").readlines()  # 226, 3509
# data = open("src/day12/example2.txt", "r").readlines()  # 19, 103
# data = open("src/day12/example.txt", "r").readlines()  # 10, 36
# data = open("src/day12/test1.txt", "r").readlines()  # 3, 5
# data = open("src/day12/test2.txt", "r").readlines()  # 4, 12

data = [line.strip("\n") for line in data]
data = [line.split("-") for line in data]

print(part1(data))
print(part2(data))
