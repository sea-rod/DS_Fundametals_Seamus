from calories import Calories

if __name__ == "__main__":
    c = Calories("02/07/2024", "30/08/2024", "data.csv")
    print("avg:", c.avg())
    print("std:", c.std())
    print("highest_meal:", c.highest_cal())
    print("highest_meal_per_cal:", c.highest_meal_cal())
