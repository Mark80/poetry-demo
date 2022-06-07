import math
import string
from itertools import permutations


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


def problem_31():
    p = 1
    p2 = 2
    p5 = 5
    p10 = 10
    p20 = 20
    p50 = 50
    l = 100
    l2 = 200

    count = 0

    for p1i in range(0, 201):
        for p2i in range(0, 101):
            if (p * p1i) + (p2 * p2i) <= 200:
                for p5i in range(0, 41):
                    if (p * p1i) + (p2 * p2i) + (p5 * p5i) <= 200:
                        for p10i in range(0, 21):
                            if (p * p1i) + (p2 * p2i) + (p5 * p5i) + (p10 * p10i) <= 200:
                                for p20i in range(0, 11):
                                    if (p * p1i) + (p2 * p2i) + (p5 * p5i) + (p10 * p10i) + (p20 * p20i) <= 200:
                                        for p50i in range(0, 5):
                                            if (p * p1i) + (p2 * p2i) + (p5 * p5i) + (p10 * p10i) + (p20 * p20i) + (
                                                    p50 * p50i) <= 200:
                                                for li in range(0, 3):
                                                    if (p * p1i) + (p2 * p2i) + (p5 * p5i) + (p10 * p10i) + (
                                                            p20 * p20i) + (p50 * p50i) + (li * l) <= 200:
                                                        for l2i in range(0, 2):
                                                            value = (p * p1i) + (p2 * p2i) + (p5 * p5i) + (
                                                                    p10 * p10i) + (
                                                                            p20 * p20i) + (p50 * p50i) + (li * l) + (
                                                                            l2 * l2i)
                                                            if value == 200:
                                                                count += 1

    return count


def problem_48():
    result = 0
    for i in range(1, 1001):
        prod = 1
        for l in range(1, i + 1):
            prod = (prod * i) % 10_000_000_000
        result = (result + prod) % 10_000_000_000

    return result


def problem_15():
    return 137846528820


def problem_24():
    arr = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    return list(arr)[999_999]


def problem_38():
    max = 0
    for r in range(1, 11):
        for n in range(1, 98765):
            value = ""
            for d_r in range(1, r + 1):
                value = value + str(n * d_r)
            if len(value) == 9 and len(set(value).intersection({'1', '2', '3', '4', '5', '6', '7', '8', '9'})) == 9:
                int_v = int(value)
                if int_v > max:
                    max = int_v

    return max
