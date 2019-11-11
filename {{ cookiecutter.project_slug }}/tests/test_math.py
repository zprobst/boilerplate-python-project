from {{ cookiecutter.project_slug }}.math import add


def test_add_simple():
    assert 2 == add(1, 1)


def test_add_negative():
    assert 2 == add(4, -2)
