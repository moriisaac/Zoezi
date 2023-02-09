import tkinter as tk
ggh
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
           self.user = None
        self.plan = None
        self.current_workout = 0
        self.label = tk.Label(self, text="Welcome to Zoezi Workout Planner!", font=("Helvetica", 20))
        self.label.pack(pady=50)
        self.name_label = tk.Label(self, text="Name:")
        self.name_entry = tk.Entry(self)
        self.age_label = tk.Label(self, text="Age:")
        self.age_entry = tk.Entry(self)
        self.weight_label = tk.Label(self, text="Weight (kg):")
        self.weight_entry = tk.Entry(self)
        self.height_label = tk.Label(self, text="Height (cm):")
        self.height_entry = tk.Entry(self)
        self.goal_label = tk.Label(self, text="Workout goal (strength/cardio):")
        self.goal_entry = tk.Entry(self)
        self.start_button = tk.Button(self, text="Start Workout", command=self.start_workout)
        self.name_label.pack()
        self.name_entry.pack()
        self.age_label.pack()
        self.age_entry.pack()
        self.weight_label.pack()
        self.weight_entry.pack()
        self.height_label.pack()
        self.height_entry.pack()
        self.goal_label.pack()
        self.goal_entry.pack()
        self.start_button.pack(pady=50)

    def start_workout(self):
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        weight = float(self.weight_entry.get())
        height = float(self.height_entry.get())
        goal = self.goal_entry.get()
        self.user = User(name, age, weight, height, goal)
        self.plan = create_plan(self.user)
        self.label.config(text="Starting workout...")
        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        self.age_label.pack_forget()
        self.age_entry.pack_forget()
        self.weight_label.pack_forget()
        self.weight_entry.pack_forget()
        self.height_label.pack_forget()
        self.height_entry.pack_forget()
        self.goal_label.pack_forget()
        self.goal_entry.pack_forget()
        self.start_button.pack_forget()
        self.next_exercise()

    def next_exercise(self):
        if self.current_workout >= len(self.plan.workout_list):
            self.label.config(text="Congratulations! You have completed your workout.")
            return
        
 if name == "main":
# Code to gather user information and create a workout plan
  user = User(name, age, weight, height, goal)
  plan = create_plan(user)
