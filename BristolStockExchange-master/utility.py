import os


# needed for BSE n_days
def getDaysFromSec(seconds):
    return seconds/60/60/24

# deletes old csvs quickly
def delete_csv():
    csv_directory = os.getcwd()
    for filename in os.listdir(csv_directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(csv_directory, filename)
            os.remove(file_path)

print(getDaysFromSec(600))