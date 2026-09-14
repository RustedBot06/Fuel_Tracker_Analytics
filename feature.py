from stats import *
from mileage import *

def entry_summary(prev_avg, tupl,count): #So long because of formatting~
    if count>=2:
        listofdates, mileages = mil() 
        price, amount, odo, date, isfull = tupl 
        current_mileage = mileages[-1] 
        last_mileage = mileages[-2] 
        print("\n" + "=" * 42) 
        print(" REFILL SUMMARY") 
        print("=" * 42) 
        print(f"Date : {date}")
        print(f"Odometer : {odo} km") 
        print(f"Fuel filled : {amount:.2f} L") 
        print(f"Total cost : ₹{price:.2f}") 
        print(f"Fuel rate : ₹{price / amount:.2f}/L") 
        print(f"Full tank refill : {'Yes' if isfull else 'No'}") 
        print("-" * 42) 
        print(f"Previous mileage : {last_mileage:.2f} km/L") 
        print(f"Current mileage : {current_mileage:.2f} km/L") 
        print(f"Average mileage : {prev_avg:.2f} km/L") 
        print("-" * 42) 
        if prev_avg is None:
            print("Sufficient data not available for comparison.")
        else: 
            if current_mileage > last_mileage: 
                change = (current_mileage - last_mileage) * 100 / last_mileage 
                print(f"Since last refill : ↑ {change:.2f}% improvement") 
            elif current_mileage < last_mileage: 
                change = (last_mileage - current_mileage) * 100 / last_mileage 
                print(f"Since last refill : ↓ {change:.2f}% reduction") 
            else: 
                print("Since last refill : Same mileage") 
            if current_mileage > prev_avg: 
                change = (current_mileage - prev_avg) * 100 / prev_avg 
                print(f"Vs. average : ↑ {change:.2f}% above average") 
            elif current_mileage < prev_avg: 
                change = (prev_avg - current_mileage) * 100 / prev_avg 
                print(f"Vs. average : ↓ {change:.2f}% below average") 
            else: 
                print("Vs. average : Same as average") 
                print("=" * 42)
    else: 
        print("Entry Summary Unavailable for 2 or less entries.")