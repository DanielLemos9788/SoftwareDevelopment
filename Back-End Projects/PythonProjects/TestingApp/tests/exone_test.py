import pytest

# function: runs once per test
# class: runs once per class of tests
# module: runs once per module
# module: runs once per session


@pytest.fixture(scope="module")
def fix_one():
    print('running-fixture-one')
    return 1


@pytest.mark.skip
def test_example():
    print("First Validation Test")
    assert 1 == 1


def test_example_one(fix_one):
    print("First Validation Test")
    num = fix_one
    assert num == 1


def test_example_two():
    assert 125 == 125


def test_example_xx(fix_one):
    print("XX Validation Test")
    num = fix_one
    assert num == 1




