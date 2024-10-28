import csv
from datetime import datetime
import os
from collections import defaultdict

def calculate_days(start_time, end_time):
    # Parse the input times
    start = datetime.strptime(start_time, '%m/%d/%y %I:%M %p')
    end = datetime.strptime(end_time, '%m/%d/%y %I:%M %p')
    
    # Calculate the difference in seconds
    delta = end - start
    seconds = delta.total_seconds()
    
    # Calculate the number of days
    days = (seconds // 86400) + 1  # 86400 seconds in a day
    
    return int(days)

def read_times_from_csv(file_path):
    resource_days = defaultdict(int)
    
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            resource = row['Resource']
            start_time = row['Begin']
            end_time = row['End']
            days = calculate_days(start_time, end_time)
            resource_days[resource] += days
    
    return resource_days

def read_times_from_subfolders(base_path):
    total_resource_days = defaultdict(int)
    
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith('2024.csv'):
                file_path = os.path.join(root, file)
                resource_days = read_times_from_csv(file_path)
                for resource, days in resource_days.items():
                    total_resource_days[resource] += days
    print(f"Resource, Total Days")
    for resource, total_days in total_resource_days.items():
        print(f"{resource},{total_days}")

def main():
    base_path = '/home/laura/Desktop/InProgress/recharges'
    read_times_from_subfolders(base_path)

if __name__ == "__main__":
    main()