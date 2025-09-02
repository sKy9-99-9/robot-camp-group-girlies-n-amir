from datetime import datetime

def solution_station_2(date_str: str):
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        weekdays = {
        0: "月曜日",  # Monday
        1: "火曜日",  # Tuesday
        2: "水曜日",  # Wednesday
        3: "木曜日",  # Thursday
        4: "金曜日",  # Friday
        5: "土曜日",  # Saturday
        6: "日曜日",  # Sunday
    }
        return weekdays[date_obj.weekday()]
        


