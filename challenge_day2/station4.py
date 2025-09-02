def solution_station_4(n: int) -> bool:
    try:
        
        if n <= 1:
            print(False)
            return
        if n <= 3:
            print(True)
            return
        if n % 2 == 0 or n % 3 == 0:
            print(False)
            return
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                print(False)
                return
            i += 6
        print(True)
    except Exception:
        print(False)

n = int(input().strip())
solution_station_4(n)