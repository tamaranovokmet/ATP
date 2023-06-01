import csv
import os

# List the CSV files to be joined
csv_files = ['atp_rankings_current.csv', 'atp_rankings_20s.csv', 'atp_rankings_10s.csv', 'atp_rankings_00s.csv']

# Specify the output file name
output_file = 'joined_file.csv'

# Open the output file in write mode
with open(output_file, 'w', newline='') as output_csv:
    writer = csv.writer(output_csv)

    # Iterate over each CSV file
    for csv_file in csv_files:
        # Open the current CSV file
        with open(csv_file, 'r') as input_csv:
            reader = csv.reader(input_csv)

            # Write each row from the current CSV file to the output file
            for row in reader:
                writer.writerow(row)

print('CSV files joined successfully.')