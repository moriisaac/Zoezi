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
    # code to create a workout plan for the user based on their information and goal
    return Plan(user, workout_list)

def start_workout(plan):
    # code to start the workout and guide the user through each exercise
    pass

def track_progress(plan):
    # code to track the user's progress and store their workout history
    pass

# Main program
if __name__ == "__main__":
    # code to gather user information and create a workout plan
    user = User(name, age, weight, height, goal)
    plan = create_plan(user)

    # code to start the workout and track progress
    start_workout(plan)
    track_progress(plan)
