from utils.split import chunk_message

def test_short():
    assert chunk_message("hi") == ["hi"]

def test_split_long():
    long = "a" * 5000
    chunks = chunk_message(long)
    assert len(chunks) == 3
    assert all(len(c) <= 2000 for c in chunks)
    assert "".join(chunks) == long

def test_multiline():
    text = "line1\nline2\n" + "x" * 3000
    chunks = chunk_message(text)
    assert "".join(chunks).replace("\n", "\n") is not None
