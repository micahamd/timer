import csv
from tkinter import filedialog
import tkinter as tk
from tkinter import colorchooser, simpledialog, messagebox  # Import simpledialog here
from datetime import datetime, timedelta
from activity_main import ActivityManager
from data_storage import DataStorage
from visualization import display_activities_with_goals, calculate_daily_average
from tkcalendar import DateEntry # Import DateEntry from tkcalendar module
from tkinter import messagebox



class TimerApp:
    def __init__(self, root_window):
        self.root = root_window
        self.root.title("Timer App")
        self.data_storage = DataStorage()  # Instantiate DataStorage
        
        self.visualize_button = tk.Button(root, text="Summarize data", command=self.visualize_data,
                                          relief='raised',
                                          activebackground='darkgrey', activeforeground='white')
        
        self.visualize_button.config(fg="black", bg="white", activeforeground="black", activebackground="pink")

        self.visualize_button.grid(row=0, column=1, columnspan=2)
        self.current_activity_start = None

        self.timer_label = tk.Label(root, text="00:00:00:000", font=("Arial", 30),bg='maroon',fg='yellow')
        self.timer_label.grid(row=1, column=0, columnspan=2)

        self.start_pause_button = tk.Button(root, text="Start/Pause",
                                            command=self.toggle_timer, relief='raised',
                                            activebackground='lightgreen', activeforeground='black',
                                            bg='green', fg='white',width=10,height=2)
        self.start_pause_button.grid(row=2, column=0)  # Place it in the first row, first column

        self.stop_button = tk.Button(root, text="Stop",
                                     command=self.stop_timer, relief='raised',
                                     activebackground='maroon', activeforeground='white',
                                     bg='red', fg='white',width=10,height=2)
        self.stop_button.grid(row=2, column=1)  # Place it in the first row, second column

        self.theme_button = tk.Button(root, text="Display Theme",
                                      command=self.change_theme,
                                      relief='raised',bg='orange',fg='black',
                                      activebackground='brown', activeforeground='white')
        self.theme_button.grid(row=0, column=0)

        self.running = False
        self.timer_start = None
        self.elapsed_time = timedelta(0)

        # Add Activity Management
        self.activity_manager = ActivityManager()
        self.activity_var = tk.StringVar(root)
        self.activity_var.set("Select Activity")  # default value
        self.activity_menu = tk.OptionMenu(root, self.activity_var, *self.activity_manager.get_activities())
        self.activity_menu.config(fg="black", bg="yellow", activeforeground="pink", activebackground="black")
        self.activity_menu.grid(row=3, column=0,columnspan=2)

        # Add and Delete Activity Buttons
        self.add_activity_button = tk.Button(root, text="Add Activity", command=self.add_activity,
                                             relief='raised',bg='blue',fg='white',
                                             activebackground='darkblue', activeforeground='white')
        self.add_activity_button.grid(row=4,column=0)

        self.delete_activity_button = tk.Button(root, text="Delete Activity", command=self.delete_activity,bg='grey',fg='pink', relief='raised', activebackground='black', activeforeground='pink')
        self.delete_activity_button.grid(row=4,column=1)

        # Add Help Button
        self.help_button = tk.Button(root, text="Help", command=self.show_help,
                                     relief='raised', bg='purple', fg='white',
                                     activebackground='purple', activeforeground='white')
        self.help_button.grid(row=5, column=0, columnspan=2)

    def show_help(self):
        messagebox.showinfo("Help", "Select an activity then start the timer.\nThis will be logged for each date, and can be downloaded as a CSV file after pressing 'Summarize data', then selecting 'Download data' in the new window.\nTo add/delete an activity, you have to manually type it in. After you have added/deleted an activity, restart the application to update the activity list.\nYou can also change the colors of the timer display.\nTo set a goal for an activity, enter the goal in the format HH:MM and press 'Update'.")

    def toggle_timer(self):
        if self.running:
            self.pause_timer()
        else:
            self.start_timer()

    def start_timer(self):
        if not self.running:
            self.running = True
            self.timer_start = datetime.now() - self.elapsed_time
            selected_activity = self.activity_var.get()
            self.activity_manager.select_activity(selected_activity)  # Update this line
            self.current_activity_start = datetime.now()
            self.update_timer()

    def pause_timer(self):
        if self.running:
            self.running = False
            self.elapsed_time = datetime.now() - self.timer_start
            self.record_activity_time()  # Record the time spent on the activity
            self.timer_start = None

    def update_timer(self):
        if self.running:
            elapsed_time = datetime.now() - self.timer_start
            self.elapsed_time = elapsed_time
            self.update_timer_label()
            self.timer_label.after(10, self.update_timer)

    def update_timer_label(self):
        hours, remainder = divmod(self.elapsed_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        milliseconds = int(self.elapsed_time.microseconds / 1000)
        self.timer_label.config(text="{:02}:{:02}:{:02}:{:03}".format(hours, minutes, seconds, milliseconds))

    def stop_timer(self):
        if self.running:
            self.pause_timer()
        self.elapsed_time = timedelta(0)
        self.update_timer_label()

    def record_activity_time(self):
        activity_name = self.activity_manager.get_selected_activity()
        if activity_name and activity_name != "Select Activity":  # Validate activity selection
            end_time = datetime.now()
            duration = end_time - self.current_activity_start  # This is a timedelta object
            activity_data = {
                "start": self.current_activity_start.strftime("%Y-%m-%d %H:%M:%S"),
                "end": end_time.strftime("%Y-%m-%d %H:%M:%S"),
                "duration": duration.total_seconds(),  # Include the duration in the log
            }

            # Check if the activity already has a log list, if not, create one
            if activity_name not in self.data_storage.data['activities']:
                self.data_storage.data['activities'][activity_name] = []

            # Append the new record to the activity's log list
            self.data_storage.data['activities'][activity_name].append(activity_data)

            # Save the updated data to the JSON file
            self.data_storage.save_data()

    def add_activity(self):
        new_activity = simpledialog.askstring("Add Activity", "Enter new activity name:")
        if new_activity:  # This checks for both None and empty string
            if new_activity not in self.activity_manager.get_activities():
                self.activity_manager.add_activity(new_activity)
                self.update_activity_menu()

    def delete_activity(self):
        activity_to_delete = simpledialog.askstring("Delete Activity", "Enter the name of the activity to delete:")
        if activity_to_delete:  # Check that activity_to_delete is not None or an empty string
            if activity_to_delete in self.activity_manager.get_activities():
                self.activity_manager.delete_activity(activity_to_delete)
                self.update_activity_menu()

    def update_activity_menu(self):
        self.activity_menu['menu'].delete(0, 'end')
        for activity in self.activity_manager.get_activities():
            self.activity_menu['menu'].add_command(label=activity,
                                                   command=lambda value=activity: self.activity_var.set(value))
        self.activity_var.set("Select Activity")

    def change_theme(self):
        # Create a new menu
        theme_menu = tk.Menu(self.root, tearoff=0)
    
        # Add options to the menu
        theme_menu.add_command(label="Timer Background", command=self.change_background_color)
        theme_menu.add_command(label="Timer Font Color", command=self.change_font_color)
    
        # Display the menu
        theme_menu.post(self.root.winfo_pointerx(), self.root.winfo_pointery())
    
    def change_background_color(self):
        # Choose background color
        bg_color_info = colorchooser.askcolor(title="Choose background color")
        if bg_color_info is not None and bg_color_info[1] is not None:
            self.timer_label.config(bg=bg_color_info[1])
    
    def change_font_color(self):
        # Choose font color
        fg_color_info = colorchooser.askcolor(title="Choose font color")
        if fg_color_info is not None and fg_color_info[1] is not None:
            self.timer_label.config(fg=fg_color_info[1])
    
    def visualize_data(self):
        # Create a new window for displaying activities
        self.data_window = tk.Toplevel(self.root)
        self.data_window.title("Activity Data")

        # Add a DateEntry widget for the start date
        self.start_date_entry = DateEntry(self.data_window)
        self.start_date_entry.grid(row=0, column=2)  # Place it in the first row, third column

        # Add a 'Download data' button
        self.download_button = tk.Button(self.data_window, text="Download data", command=self.download_data,activebackground='red', activeforeground='black', relief='raised',
                                         bg='pink', fg='brown')
        
        self.download_button.grid(row=1, column=3)  # Place it in the first row, fourth column

        # Bind a function to the DateEntry widget that is called when a new date is selected
        self.start_date_entry.bind("<<DateEntrySelected>>", self.on_date_selected)

        # Add column headers
        tk.Label(self.data_window, text="Activity").grid(row=1, column=0)
        tk.Label(self.data_window, text="Daily Average\nsince Start Date").grid(row=1, column=1)
        tk.Label(self.data_window, text="Enter a Goal in HH:MM").grid(row=1, column=2) 
        tk.Label(self.data_window, text="Enter Start Date").grid(row=0, column=1) 

        # Call update_data to display the data
        self.update_data()
        
    def download_data(self):
        # Get the selected start date
        start_date = self.start_date_entry.get_date()

        # Fetch the data
        activities = self.data_storage.data.get('activities', {})

        # Filter the data based on the selected date
        filtered_data = []
        for activity, logs in activities.items():
            for log in logs:
                log_start_date = datetime.strptime(log['start'], "%Y-%m-%d %H:%M:%S").date()
                if log_start_date >= start_date:
                    duration = timedelta(seconds=log['duration'])
                    duration_str = "{:02}:{:02}".format(int(duration.total_seconds() // 3600), int((duration.total_seconds() % 3600) // 60))
                    filtered_data.append([log_start_date.strftime("%d-%m-%Y"), activity, duration_str])

        # Ask the user where to save the file
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return  # The user cancelled the dialog

        # Write the data to a CSV file
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Activity", "Duration (HH:MM)"])  # Write the header
            writer.writerows(filtered_data)  # Write the data

    def update_data(self):
        # Clear the existing data
        for widget in self.data_window.winfo_children():
            if isinstance(widget, tk.Label) and widget.grid_info()["row"] > 1:
                widget.destroy()

        # Fetch the data
        activities = self.data_storage.data.get('activities', {})
        goals = self.data_storage.data.get('goals', {})
          
        # Display the data in rows
        for i, (activity, logs) in enumerate(activities.items(), start=2):  # Start from the second row
            # Get the date from the DateEntry widget
            start_date = self.start_date_entry.get_date()
    
            # Pass the start_date to the calculate_daily_average function
            daily_avg_hours, daily_avg_minutes = calculate_daily_average(logs, start_date)
    
            tk.Label(self.data_window, text=activity).grid(row=i, column=0)
            tk.Label(self.data_window, text=f"{daily_avg_hours:02d}:{daily_avg_minutes:02d}").grid(row=i, column=1)
    
            # Entry widget for goal with a default value
            goal_hours = goals.get(activity, {'hours': 2, 'minutes': 0})['hours']
            goal_minutes = goals.get(activity, {'hours': 2, 'minutes': 0})['minutes']
            goal_var = tk.StringVar(value=f"{goal_hours:02d}:{goal_minutes:02d}")
            goal_entry = tk.Entry(self.data_window, textvariable=goal_var)
            goal_entry.grid(row=i, column=2)
    
            # Button to update the goal
            update_button = tk.Button(self.data_window, text="Update",
                                      command=lambda a=activity, g=goal_var: self.update_goal(a, g.get()))
            update_button.grid(row=i, column=3)
    
        # Call the display_activities_with_goals function with the start_date
        display_activities_with_goals(start_date)
    
    def on_date_selected(self, event):
        # Call the update_data function when a new date is selected
            self.update_data()
        
    def update_goal(self, activity, new_goal):
        # Validate and update the goal in DataStorage
        try:
            new_goal_hours, new_goal_minutes = map(int, new_goal.split(":"))  # Split the goal into hours and minutes
            print(f"Updating goal for {activity} to {new_goal_hours} hours and {new_goal_minutes} minutes")  # Debug print
            self.data_storage.set_goal_for_activity(activity, new_goal_hours, new_goal_minutes)
            self.data_storage.save_data()
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid goal in the format HH:MM.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
