import math

def calculate_fine(days_late):
    fine          = 0
    week          = 1
    days_left     = days_late
 
    while days_left > 0:
        days_this_week  = min(7, days_left)
        rate_per_day    = 10 * math.factorial(week)
        fine           += days_this_week * rate_per_day
        days_left      -= 7
        week           += 1
 
    return fine