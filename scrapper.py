# importing all the files
from bs4 import BeautifulSoup
import requests
import csv
import time
import pandas as pd
import numpy as np

# URL for the website
Start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Creating headers for the csv
headers = ["name", "distance", "mass", "radius"]

# Using Get Request Method
page = requests.get(Start_url)
# Waiting for 5 seconds
time.sleep(5)

# print(page)

soup_object = BeautifulSoup(page.text, "html.parser")


# Getting the list of tables
start_table = soup_object.find("table")

# Getting all the rows
table_rows = start_table.find_all("tr")
temp_list_1 = []

# Getting all the data in temp_list_1
for tr in table_rows:
    td = tr.find_all("td")
    temp_list_2 = []
    for td_tag in td:
        temp_list_2.append(td_tag.text.rstrip())
    temp_list_1.append(temp_list_2)

# print(temp_list_1)

star_name = []
star_distance = []
star_mass = []
star_radius = []

for i in range(1, len(temp_list_1)):
    if(temp_list_1[i][1] == "?"):
        star_name.append("")
    else:
        star_name.append(temp_list_1[i][1])
    if(temp_list_1[i][3] == "?"):
        star_distance.append("")
    else:
        star_distance.append(temp_list_1[i][3])
    if(temp_list_1[i][5] == "?"):
        star_mass.append("")
    else:
        star_mass.append(temp_list_1[i][5])
    if(temp_list_1[i][6] == "?"):
        star_radius.append("")
    else:
        star_radius.append(temp_list_1[i][6])

# print("star_name :- ", star_name)
# print("star_distance :- ", star_distance)
# print("star_radius :- ", star_radius)
# print("star_mass :- ", star_mass)

star_data = []

# Storing all data in star_data to create csv
for i in range(0, len(temp_list_1)-1):
    temp_star_data = []
    temp_star_data.append(star_name[i])
    temp_star_data.append(star_distance[i])
    temp_star_data.append(star_mass[i])
    temp_star_data.append(star_radius[i])
    star_data.append(temp_star_data)

# print(star_data)

# Creating csv file 
# with open("scrapper_2.csv", "a+") as f:
#     csv_writer = csv.writer(f)
#     csv_writer.writerow(headers)
#     csv_writer.writerows(star_data)

# Another URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

headers_2 = ["name", "distance", "mass", "radius"]

# Using Get Request Method
page_2 = requests.get(START_URL)

# Waiting for 5 seconds
time.sleep(5)
soup_object_2 = BeautifulSoup(page_2.text, "html.parser")

all_tables = soup_object_2.find_all("table")
start_table_2 = []
for index, tables in enumerate(all_tables):
    if(index == 7):
        start_table_2 = tables

table_rows_2 = start_table_2.find_all("tr")

temp_list_3 = []

for tr_tags in table_rows_2:
    td_tags = tr_tags.find_all("td")
    temp_list_4 = []
    for td_tag_2 in td_tags:
        temp_list_3.append(td_tag_2.text.rstrip())
    temp_list_4.append(temp_list_3)

print(len(temp_list_4[0]))

star_name_2 = []
star_distance_2 = []
star_mass_2 = []
star_radius_2 = []

for i in range(0, len(temp_list_4[0])-1):
    if(i % 10 == 0):
        star_name_2.append(temp_list_4[0][i])
    elif(i % 10 == 5):
        star_distance_2.append(temp_list_4[0][i])
    elif(i % 10 == 7):
        star_mass_2.append(temp_list_4[0][i])
    elif(i % 10 == 8):
        star_radius_2.append(temp_list_4[0][i])


# print("star_name :- ", star_name_2)
# print("star_distance :- ", star_distance_2)
# print("star_radius :- ", star_radius_2)
# print("star_mass :- ", star_mass_2)

new_star_data = []

for i in range(0, len(star_name_2)-1):
    temp_star_data_2 = []
    temp_star_data_2.append(star_name_2[i])
    temp_star_data_2.append(star_distance_2[i])
    temp_star_data_2.append(star_mass_2[i])
    temp_star_data_2.append(star_radius_2[i])
    new_star_data.append(temp_star_data_2)

df = pd.DataFrame(new_star_data, columns = headers_2)
df.to_csv("scrapper_3.csv")