def solution_station_4(n: int) -> bool:
    try:
        
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    except Exception:
        return False

n = int(input().strip())
print(solution_station_4(n))