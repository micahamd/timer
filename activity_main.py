import os
from data_storage import DataStorage

class ActivityManager:
    def __init__(self):
        self.data_storage = DataStorage()  # Setup to handle 'activities'
        self.activities = self.load_activities()
        self.selected_activity = None
        self.initialize_preset_activities()  # Optionally initialize pre-set activities

    def initialize_preset_activities(self):
        # Pre-set activities, add any you wish to start with
        preset_activities = ["Study", "Workout"]
        for activity in preset_activities:
            self.add_activity(activity)

    def save_activities(self):
        # Instead of resetting activities, ensure existing structure is preserved
        for activity in self.activities:
            if activity not in self.data_storage.data['activities']:
                self.data_storage.data['activities'][activity] = []  # Ensure list structure
        self.data_storage.save_data()

    def load_activities(self):
        # Load activities from DataStorage
        return list(self.data_storage.data.get('activities', {}).keys())

    def add_activity(self, activity_name):
        if activity_name not in self.activities:
            self.activities.append(activity_name)
            # Ensure it's initialized correctly in DataStorage
            if activity_name not in self.data_storage.data['activities']:
                self.data_storage.data['activities'][activity_name] = []  # Initialize as a list
            self.save_activities()
            return True
        return False

    def delete_activity(self, activity_name):
        if activity_name in self.activities:
            self.activities.remove(activity_name)
            if activity_name in self.data_storage.data['activities']:
                del self.data_storage.data['activities'][activity_name]  # Remove from DataStorage as well
            self.save_activities()
            return True
        return False

    def select_activity(self, activity_name):
        if activity_name in self.activities:
            self.selected_activity = activity_name
            return True
        return False

    def get_activities(self):
        return self.activities

    def get_selected_activity(self):
        return self.selected_activity
