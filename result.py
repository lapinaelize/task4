import pandas

# Get input from terminal
get_info = input("Enter information: ")

try:
    fails = pandas.read_excel("description.xlsx", sheet_name="LookupAREA")  # If no pages are specified, then the last one saved is open
    info_list = fails.values.tolist()

# write your program code here
    data = pandas.read_csv("data.csv")  
except FileNotFoundError:
    print("Error: One or more files are missing.")
    exit(1)  


region_code = None
for row in info_list:
    if get_info.lower() == row[1].lower():  
        region_code = row[0]  
        break

if not region_code:
    print(0)
    exit(0)

geo_sum = data[data['Area'] == region_code]['geo_count'].sum()  

print(int(geo_sum))  