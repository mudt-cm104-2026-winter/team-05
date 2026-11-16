_entries = []
_next_id = 1


def all_entries():
    """Return a copy of all entries, oldest first."""
    return list(_entries)


def add_entry(num1, op, num2, result):
    """Store a new entry and return it."""
    global _next_id
    entry = {"id": _next_id,
             "num1": num1,
             "op": op, 
             "num2": num2, 
             "result": result,
             "expression": f"{num1} {op} {num2} = {result}",
             }
    _entries.append(entry)
    _next_id += 1
    return entry

def clear_entries():
    """Clear all entries."""
    global _next_id
    _entries.clear()
    _next_id = 1