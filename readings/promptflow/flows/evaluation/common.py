import ast


def parse_set(x):
    try:
        return set(ast.literal_eval(x)) if x else set()
    except Exception:
        print("Bad item:", x)
        raise
