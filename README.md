# timer

Basic Python application that allows users to track time spent on customizable activities. Users can view daily averages spent on each activity with a customizable start date, and set personal goals.

## Features

- **Activity Tracking**:Start, pause, and stop a timer for a selected activity.
- **Activity Management**: Add and delete activities.
- **Data Visualization**: Summarize the time spent on each activity.
- **Theme Customization**: Change the background and font color of the timer.
- **Goal Setting**: Set goals for each activity and compare their actual time spent with these goals.

## Usage

To run the application, execute the `time_main.py` file:

```bash
python time_main.py
```

## Interface

The main interface of the application includes:

- A timer display
- Buttons to start/pause and stop the timer
- A dropdown menu to select an activity
- Buttons to add and delete activities
- A button to visualize data
- A button to change the theme

## Dependencies

This application requires the following Python libraries:

- `tkinter`
- `tkcalendar`
- `datetime`
- `simpledialog`
- `messagebox`
- `colorchooser`

## Code Structure

The `TimerApp` class is the main class of the application. It initializes the Tkinter window and all the widgets, and it contains methods to handle all the functionalities of the application.

The `ActivityManager` class manages the list of activities.

The `DataStorage` class handles the storage and retrieval of data.

The `display_activities_with_goals` and `calculate_daily_average` functions in the `visualization` module are used to visualize the data.

## Note

This application saves the data in a JSON file. Make sure to have write access to the directory where the application is running.
