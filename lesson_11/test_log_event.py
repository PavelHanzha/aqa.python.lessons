import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


import os
import pytest
from log_event import log_event

LOG_FILE = "login_system.log"

@pytest.mark.parametrize(
    "username, status, expected_level",
    [
        ("user1", "success", "INFO"),
        ("user2", "expired", "WARNING"),
        ("user3", "failed", "ERROR"),
        ("user4", "unknown", "ERROR"),
    ]
)
def test_log_event(username, status, expected_level):
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.truncate(0)

    log_event(username, status)

    assert os.path.exists(LOG_FILE)

    with open(LOG_FILE, encoding="utf-8") as f:
        content = f.read()
        assert username in content
        assert status in content
        assert expected_level in content
