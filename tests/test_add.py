import shared_workflow_test


def test_sanity():
    assert 1 + 1 == 2


def test_add():
    assert shared_workflow_test.add_numbers(1, 2) == 3
