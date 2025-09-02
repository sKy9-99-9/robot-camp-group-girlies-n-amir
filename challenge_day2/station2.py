from datetime import datetime

def solution_station_2(date_str: str) -> str:
        weekdays = {
        0: "月曜日",  # Monday
        1: "火曜日",  # Tuesday
        2: "水曜日",  # Wednesday
        3: "木曜日",  # Thursday
        4: "金曜日",  # Friday
        5: "土曜日",  # Saturday
        6: "日曜日",  # Sunday
    }

<<<<<<< HEAD

        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return weekdays[date_obj.weekday()]
=======
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return weekdays[date_obj.weekday()]

date_input = input("Enter a date (yyyy-mm-dd): ").strip()
print(solution_station_2(date_input))
>>>>>>> a6c33b9b66d0a7f907b1692a160f7bc8bf28e435
