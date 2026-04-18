from unittest.mock import MagicMock

import pytest
from app.system import get_user


def test_get_user(monkeypatch):
    monkeypatch.setenv("USER", "dipayan")
    assert get_user() == "dipayan"
