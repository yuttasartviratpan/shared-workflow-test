import shared_workflow_runner


def test_sanity():
    assert 1 + 1 == 2


def test_add():
    assert shared_workflow_runner.add_numbers(1, 2) == 3
