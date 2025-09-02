def solution_station_3(n: int) -> bool:
    if n%3==0:
        return True
    return False

n = int(input().strip())
print(solution_station_3(n))
