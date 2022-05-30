import math
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


def problem_27():
    max_a = -1000
    max_b = -1000
    count = 0
    max_value = 2 * (1000 * 1000) + 1000
    print(max_value)
    primi = primes(max_value)
    for a in range(-1000, 1000):
        for b in range(-1000, 1000):
            current_count = 0
            check = True
            n = 0
            while check and n <= max_value:
                value = (n * n) + (a * n) + b
                if binary_search(primi, value) == -1:
                    check = False
                else:
                    current_count += 1
                    n += 1

            if current_count > count:
                count = current_count
                max_a = a
                max_b = b
    return max_a * max_b


def primes(n):
    nums_primes = [2, 3]
    for i in range(5, n + 1, 2):
        sqrt = int(math.sqrt(i))
        is_prime = True
        count = 2
        while is_prime and count <= sqrt:
            if i % count == 0:
                is_prime = False
            count += 1
        if is_prime:
            nums_primes.append(i)
    return nums_primes


def binary_search(lst, target):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] > target:
            end = mid - 1
        elif lst[mid] < target:
            start = mid + 1
        else:
            return mid
    return -1
