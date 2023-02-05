import tkinter as tk

class User:
    def __init__(self, name, age, weight, height, goal):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.goal = goal

class Workout:
    def __init__(self, name, muscle_group, sets, reps, weight):
        self.name = name
        self.muscle_group = muscle_group
        self.sets = sets
        self.reps = reps
        self.weight = weight

class Plan:
    def __init__(self, user, workout_list):
        self.user = user
        self.workout_list = workout_list

def create_plan(user):
    # Code to create a workout plan based on the user's information and goal
    if user.goal == "strength":
        workout_list = [Workout("Squats", "Legs", 3, 8, 50),
                        Workout("Bench Press", "Chest", 3, 8, 40),
                        Workout("Deadlifts", "Back", 3, 8, 60)]
    elif user.goal == "cardio":
        workout_list = [Workout("Jogging", "Cardio", None, 30, None),
                        Workout("Cycling", "Cardio", None, 45, None),
                        Workout("Swimming", "Cardio", None, 30, None)]
    else:
        raise ValueError("Invalid goal type")
    return Plan(user, workout_list)

class WorkoutApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Zoezi Workout Planner")
        self.geometry("500x500")
