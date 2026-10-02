"""Split long text into Discord-safe 2000-char chunks."""


def chunk_message(text: str, limit: int = 2000) -> list[str]:
    text = text or "..."
    if len(text) <= limit:
        return [text]
    chunks, current = [], ""
    for line in text.splitlines(keepends=True):
        if len(current) + len(line) > limit:
            chunks.append(current)
            current = ""
        current += line
    if current:
        chunks.append(current)
    # hard-split any oversized chunk
    out = []
    for c in chunks:
        while len(c) > limit:
            out.append(c[:limit])
            c = c[limit:]
        out.append(c)
    return out
