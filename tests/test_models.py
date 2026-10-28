from hopiumcode.models import Chunk, Hit


def test_chunk_ref_format():
    c = Chunk("a/b.py::f", "a/b.py", 3, 9, "function", "f", "def f(): ...", "python")
    assert c.ref == "[a/b.py:3-9]"


def test_hit_holds_chunk():
    c = Chunk("x::#1", "x.md", 1, 2, "doc", None, "text", "markdown")
    assert Hit(c, 0.5, "vector").chunk is c
