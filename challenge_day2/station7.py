def solution_station_7(expr: str):
    values = {
        "e": 0.5,
        "c": 4,
        "a": 3,
        "b": -1,
        "d": 7
    }

    return float(eval(expr, {}, values))
