import json

class DataStorage:
    def __init__(self, file_name="activity_log.json"):
        self.file_name = file_name
        self.data = {}  # Initialize the self.data dictionary
        self.load_data()

    def load_data(self):
        try:
            with open(self.file_name, 'r') as file:
                self.data = json.load(file)
                # Ensure that 'activities' and 'goals' keys exist
                self.data.setdefault('activities', {})
                self.data.setdefault('goals', {})
                # Ensure activities have the correct structure (list for logs)
                for activity, logs in self.data['activities'].items():
                    if not isinstance(logs, list):
                        self.data['activities'][activity] = []  # Correct the structure if not a list
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = {'activities': {}, 'goals': {}}  # If the file does not exist or is empty/corrupted, initialize self.data with the structure

    def save_data(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.data, file, indent=4)

    def set_goal_for_activity(self, activity, goal_hours, goal_minutes):
        print(f"Activity: {activity}, Goal Hours: {goal_hours}, Goal Minutes: {goal_minutes}")
        # Ensure the 'goals' dictionary exists and is correctly structured
        self.data['goals'][activity] = {'hours': goal_hours, 'minutes': goal_minutes}
        self.save_data()

    def get_goal_for_activity(self, activity):
        # Return the goal for the specified activity, defaulting to 2 hours if not set
        return self.data.get('goals', {}).get(activity, {'hours': 1, 'minutes': 30})
