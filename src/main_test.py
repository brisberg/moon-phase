import pytest
from main import mainfunction

## Tests
def test_simple(capsys):
    mainfunction()

    captured = capsys.readouterr()
    assert captured.out == 'Welcome to Moon Phase!\n'