def read_input(data):
    polymer_template = data[:1][0]
    pair_insertion_rules = data[2:]
    pair_insertion_rules = [x.split(" -> ") for x in pair_insertion_rules]
    rules = {}
    for pair, insert in pair_insertion_rules:
        a, b = pair
        rules[(a, b)] = insert
    return (polymer_template, rules)


def create_template_tuples(template):
    template_tuples = []
    for i in range(len(template) - 1):
        a = template[i]
        b = template[i + 1]
        template_tuples.append((a, b))
    return template_tuples


def step(template, rules: dict):
    tt = create_template_tuples(template)
    new_tuples = []

    for tuple1, tuple2 in tt:
        current_tuple = ()
        if rules[(tuple1, tuple2)]:
            current_tuple = (tuple1, rules[(tuple1, tuple2)], tuple2)
        else:
            current_tuple = (tuple1, tuple2)

        new_tuples.append(current_tuple)

    new_string = ""
    for t in new_tuples:
        if len(t) == 3:
            a, b, c = t
            new_string += a + b
        if len(t) == 2:
            a, b = t
            new_string += a
        pass

    new_string += new_tuples[-1][-1]
    return new_string


def check_quantity(template):
    counter = dict()

    for c in template:
        counter[c] = counter.get(c, 0) + 1

    highest = max([x for x in counter.values()])
    lowest = min([x for x in counter.values()])

    return highest - lowest


def part1(data):
    (template, rules) = read_input(data)
    for i in range(10):
        print(i)
        template = step(template, rules)

    return check_quantity(template)


def part2(data):
    pass


data = open("src/day14/input.txt", "r").readlines()
data = open("src/day14/example.txt", "r").readlines()

data = [line.strip("\n") for line in data]

print(part1(data))
print(part2(data))
