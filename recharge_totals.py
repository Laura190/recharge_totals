import os
import csv
from collections import defaultdict

def get_chargeable_hours(directory):
    chargeable_hours = defaultdict(float)
    total_recharge = defaultdict(float)

    for subdir, _, files in os.walk(directory):
        if os.path.basename(subdir).startswith('2024'):
            for file in files:
                if file.endswith('24.csv'):
                    file_path = os.path.join(subdir, file)
                    print(file)
                    with open(file_path, mode='r') as csvfile:
                        csvreader = csv.DictReader(csvfile)
                        for row in csvreader:
                            resource = row['Resource']
                            hours = float(row['Costed Hours'])
                            recharge = float(row['Recharge'])
                            chargeable_hours[resource] += hours
                            total_recharge[resource] += recharge

    return chargeable_hours, total_recharge

def main():
    directory = '/home/laura/Desktop/InProgress/recharges/'  # Change this to your target directory
    chargeable_hours, total_recharge = get_chargeable_hours(directory)

    print(f'Resource, Costed Hours, Recharge')
    for resource in chargeable_hours:
        print(f'{resource}, {chargeable_hours[resource]}, £{total_recharge[resource]:.2f}')

if __name__ == "__main__":
    main()