import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("fitness_tracker.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS workouts (
                        id INTEGER PRIMARY KEY,
                        date TEXT,
                        exercise TEXT,
                        duration INTEGER,
                        calories_burned INTEGER)''')
    conn.commit()
    conn.close()

def log_workout(exercise, duration, calories_burned):
    conn = sqlite3.connect("fitness_tracker.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO workouts (date, exercise, duration, calories_burned) VALUES (?, ?, ?, ?)",
                   (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), exercise, duration, calories_burned))
    conn.commit()
    conn.close()
    print("Workout logged successfully!")

def view_workouts():
    conn = sqlite3.connect("fitness_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM workouts")
    workouts = cursor.fetchall()
    conn.close()
    
    if workouts:
        print("\nWorkout History:")
        for workout in workouts:
            print(f"ID: {workout[0]}, Date: {workout[1]}, Exercise: {workout[2]}, Duration: {workout[3]} min, Calories Burned: {workout[4]}")
    else:
        print("No workouts logged yet.")

def main():
    init_db()
    while True:
        print("\nFitness Tracker")
        print("1. Log Workout")
        print("2. View Workouts")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            exercise = input("Enter exercise name: ")
            duration = int(input("Enter duration (minutes): "))
            calories_burned = int(input("Enter calories burned: "))
            log_workout(exercise, duration, calories_burned)
        elif choice == "2":
            view_workouts()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
