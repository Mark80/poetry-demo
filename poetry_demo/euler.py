import string


def name_score(name, index_by__letter):
    score = 0
    for l in name:
        value = index_by__letter[l]
        score += value
    return score


def calculate_total_name_value():
    index_by__letter = {}
    alphabet = list(string.ascii_uppercase)
    for i, l in enumerate(alphabet):
        index_by__letter[l] = i + 1

    total = 0
    with open("../p022_names.txt") as names_file:
        names = names_file.read().replace("\"", "").split(",")
        names.sort()
    for i, name in enumerate(names):
        score = name_score(name, index_by__letter) * (i + 1)
        total += score
    return total
