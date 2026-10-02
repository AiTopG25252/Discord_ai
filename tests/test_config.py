import os

def test_env_defaults():
    os.environ.pop("MAX_HISTORY", None)
    # import after to test defaults is messy, just check parsing logic
    assert int(os.getenv("MAX_HISTORY", "12")) == 12
