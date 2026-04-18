from unittest.mock import MagicMock

import pytest
from app.file_reader import read_file


def test_read_file(monkeypatch):
    mock_file = MagicMock()
    mock_file.__enter__.return_value.readable.return_value = "hello"

    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)

    result = read_file("dummy.txt")
    assert result == "hello"

    mock_open.assert_called_once_with("dummy.txt", "r")
