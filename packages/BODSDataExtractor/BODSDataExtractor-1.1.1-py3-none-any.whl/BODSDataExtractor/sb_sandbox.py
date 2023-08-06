import os
import pandas as pd


def find_match(string_list, wanted):
  for string in string_list:
    if str(string).startswith(wanted):
      return True
  return False


wanted = 'atcosch'

timetable_files = "C:\\Users\\sbrittain\\OneDrive - KPMG\\Desktop\\Essex TTs"

file = os.listdir(timetable_files)

for file in os.listdir(timetable_files):
  with open(f'{timetable_files}\\{file}') as timetable:
    df = pd.read_csv(timetable)
    stop_from = df['stop_from']

    if find_match(stop_from, wanted):
      print(timetable)


