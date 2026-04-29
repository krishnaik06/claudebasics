from calculator import add, divide, multiply, subtract

OPS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def format_result(value):
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def evaluate(line):
    parts = line.split()
    if len(parts) != 3:
        raise ValueError("invalid input - expected '<num> <op> <num>' or 'quit'")
    a_str, op, b_str = parts
    if op not in OPS:
        raise ValueError(f"unknown operator '{op}' (use + - * /)")
    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        raise ValueError(f"could not parse number in '{line}'")
    return OPS[op](a, b)


def repl():
    while True:
        try:
            line = input("> ").strip()
        except EOFError:
            print()
            return
        if not line:
            continue
        if line.lower() in ("quit", "exit"):
            return
        try:
            result = evaluate(line)
        except ZeroDivisionError:
            print("Error: division by zero")
            continue
        except ValueError as e:
            print(f"Error: {e}")
            continue
        print(format_result(result))


if __name__ == "__main__":
    repl()
