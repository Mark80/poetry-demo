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


def primes_less(n):
    nums_primes = [2, 3]
    for i in range(5, n + 1, 2):
        sqrt = int(math.sqrt(i))
        is_prime = True
        count = 2
        while is_prime and count <= sqrt:
            if i % count == 0:
                is_prime = False
            count += 1
        if i > n:
            break
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
    result = 0
    for r in range(1, 11):
        for n in range(1, 98765):
            value = ""
            for d_r in range(1, r + 1):
                value = value + str(n * d_r)
            if len(value) == 9 and len(set(value).intersection({'1', '2', '3', '4', '5', '6', '7', '8', '9'})) == 9:
                int_v = int(value)
                if int_v > result:
                    result = int_v

    return result


def problem_18():
    tri = [
        [75]
        , [95, 64]
        , [17, 47, 82]
        , [18, 35, 87, 10]
        , [20, 4, 82, 47, 65]
        , [19, 1, 23, 75, 3, 34]
        , [88, 2, 77, 73, 7, 63, 67]
        , [99, 65, 4, 28, 6, 16, 70, 92]
        , [41, 41, 26, 56, 83, 40, 80, 70, 33]
        , [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
        , [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
        , [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
        , [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
        , [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
        , [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
    ]
    triangle = list(reversed(tri))
    return execute(triangle)


def sum_two_list(list_1, list_2):
    result = []
    index_1 = 0
    index_2 = 0

    while index_1 + 1 < len(list_1):
        val_1 = list_1[index_1] + list_2[index_2]
        val_2 = list_1[index_1 + 1] + list_2[index_2]
        maximus = max(val_2, val_1)
        result.append(maximus)
        index_1 += 1
        index_2 += 1

    return result


def problem_67():
    triangle = read_file()
    return execute(triangle)


def execute(triangle):
    index = 1
    r = triangle[0]
    while index < len(triangle):
        r = sum_two_list(r, triangle[index])
        index += 1
    return r


def problem_11():
    with open("/Users/marco.tosini/toy-project/poetry-demo/poetry_demo/square.txt") as file:
        lines = file.readlines()
    numbers = []
    for line in lines:
        values = list(line.replace("\n", "").split(" "))
        for v in values:
            numbers.append(int(v))
    max_value = 0
    for i, _ in enumerate(numbers):
        prod = 1
        prod_2 = 1
        prod_3 = 1
        prod_4 = 1
        if i + 3 < len(numbers):
            prod = numbers[i] * numbers[i + 1] * numbers[i + 2] * numbers[i + 3]
        if i + 60 < len(numbers):
            prod_2 = numbers[i] * numbers[i + 20] * numbers[i + 40] * numbers[i + 60]
        if i + 63 < len(numbers):
            prod_3 = numbers[i] * numbers[i + 21] * numbers[i + 42] * numbers[i + 63]
        if i + 63 < len(numbers):
            prod_4 = numbers[i] * numbers[i + 19] * numbers[i + 38] * numbers[i + 57]
        m = max(prod_2, prod, prod_3, prod_4)
        if m > max_value:
            max_value = m
    return max_value


def read_file():
    with open("/Users/marco.tosini/toy-project/poetry-demo/poetry_demo/triangle.txt") as file:
        content = file.readlines()
    rows_list = []
    for line in content:
        values = list(line.replace("\n", "").split(" "))
        num_list = []
        for v in values:
            num_list.append(int(v))
        rows_list.append(num_list)
    return list(reversed(rows_list))


def problem_23():
    ab_n = abundant_number_list()
    all_sum_ab = 0
    all_sum = set()
    for i in ab_n:
        for j in ab_n:
            p = i + j
            if p < 28124:
                all_sum.add(p)
    for i in range(1, 28124):
        check = (i in all_sum)
        if not check:
            all_sum_ab += i

    return all_sum_ab


def abundant_number_list():
    abundant_numbers = []
    for n in range(1, 28124):
        s = 0
        for div in range(1, n):
            if n % div == 0:
                s += div
        if s > n:
            abundant_numbers.append(n)

    return abundant_numbers


def problem_28():
    d = 1001
    r = 0
    while d > 1:
        r_up = (d * d)
        l_up = r_up - d + 1
        l_down = l_up - d + 1
        r_down = l_down - d + 1
        print(r_up, l_up, l_down, r_down)
        r += r_up + l_up + l_down + r_down
        d -= 2
    return r + 1


def problem_25():
    count = 0
    index = 1
    a = 0
    b = 1

    while count < 1000:
        c = a + b
        count = len(str(c))
        a = b
        b = c
        index += 1

    return index


def problem_50():
    primes = primes_less(1_000_000)
    primes_set = set(primes)

    max_p = 0
    max_count = 0
    start_index = 0
    max_index = 0
    while start_index < 1_000_000:
        window = primes[start_index:len(primes)]
        partial_sum = 0
        count = 0
        for v in window:
            partial_sum += v
            count += 1
            if partial_sum > 1_000_000:
                break
            if partial_sum in primes_set and count > max_count:
                max_count = count
                max_index = start_index
                max_p = partial_sum
        start_index += 1
    print(max_index)
    return max_p


def problem_29():
    p_set = set()
    for a in range(2, 101):
        for b in range(2, 101):
            r = math.pow(a, b)
            p_set.add(r)

    return len(p_set)


def problem_30():
    r = 0
    for i in range(2, 1000000):
        if is_sum_of_power_fifty(i):
            print(i)
            r += i
    return r


def is_sum_of_power_fifty(n):
    digits = str(n)
    s = 0
    for v in digits:
        s += math.pow(int(v), 5)
    return s == n


def problem_44():
    pentagonal = []

    for n in range(2, 10000):
        pentagonal.append((n * ((3 * n) - 1)) / 2)
    set_p = set(pentagonal)
    r = 0
    print(len(pentagonal))
    for a in range(0, len(pentagonal)):
        for b in range(a, len(pentagonal) - 1):
            s = pentagonal[a] + pentagonal[b]
            d = abs(pentagonal[a] - pentagonal[b])
            if s in set_p and d in set_p:
                print(pentagonal[a], pentagonal[b])
                r = abs(pentagonal[a] - pentagonal[b])

    return r
