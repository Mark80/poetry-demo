from poetry_demo.euler import *


def test_version():
    print(calculate_total_name_value())


def test_primes():
    print(problem_27())


def test_coin():
    assert problem_31() == 73682


def test_problem_48():
    print(problem_48())
