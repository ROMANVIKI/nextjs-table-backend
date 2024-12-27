import csv
from app.models import DataTable

file_path = "tasks(5).csv"

def parse_boolean(value):
    return str(value).strip().lower() in ['true', '1', 'yes']


with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        DataTable.objects.create(
         code=row['code'],
         title=row['title'],
         status=row['status'],
         priority=row['priority'],
         archived=parse_boolean(row['archived']),
        )

#                 )

# csv_file_paths = ["tasks(1).csv", "tasks(2).csv", "tasks(3).csv", "tasks(4).csv"]
#
#
# for file_path in csv_file_paths:
#     try:
#         with open(file_path, 'r') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 DataTable.objects.create(
#                     code=row['code'],
#                     title=row['title'],
#                     status=row['status'],
#                     priority=row['priority'],
#                     archived=parse_boolean(row['archived']),
#                 )
#         print(f"Data imported successfully from {file_path}!")
#     except FileNotFoundError:
#         print(f"File {file_path} not found. Please check the file path.")
#     except Exception as e:
#         print(f"An error occurred while importing {file_path}: {e}")


