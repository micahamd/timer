from data_storage import DataStorage
from datetime import datetime


def display_activities_with_goals(start_date):
    storage = DataStorage()  # Utilize the DataStorage class to load data
    activities = storage.data.get('activities', {})
    goals = storage.data.get('goals', {})

    print("Activity - Daily Average - Goal")
    for activity, logs in activities.items():
        daily_avg_hours, daily_avg_minutes = calculate_daily_average(logs, start_date)
        goal = goals.get(activity, {'hours': 1, 'minutes': 30})
        goal_hours, goal_minutes = goal.get('hours', 1), goal.get('minutes', 30)

        print(f"{activity} - {daily_avg_hours:02d}:{daily_avg_minutes:02d} - {goal_hours:02d}:{goal_minutes:02d}")

      
def calculate_daily_average(logs, start_date):
    total_duration = 0
    activity_days = set()

    print(f"start_date: {start_date}")

    for log in logs:
        try:
            start_time = datetime.strptime(log['start'], "%Y-%m-%d %H:%M:%S")
            end_time = datetime.strptime(log['end'], "%Y-%m-%d %H:%M:%S")

            print(f"start_time: {start_time}, end_time: {end_time}")

            # Skip logs that are before the start_date
            if start_time.date() < start_date:
                continue

            duration = (end_time - start_time).total_seconds()
            total_duration += duration
            activity_days.add(start_time.date())
        except Exception as e:
            print(f"Error processing log {log}: {e}")

    num_days = max(1, len(activity_days))
    avg_duration = total_duration / num_days

    print(f"total_duration: {total_duration}, num_days: {num_days}")

    # Convert the average duration from seconds to hours and minutes
    avg_hours = int(avg_duration // 3600)
    avg_minutes = int((avg_duration % 3600) // 60)

    return avg_hours, avg_minutes

# Ensure there is a blank line at the end of the file
