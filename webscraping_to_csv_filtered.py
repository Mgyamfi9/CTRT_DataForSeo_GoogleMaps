import pandas as pd
import json

# Path to your JSON file
json_file = 'CTRT_DataForSeo_GoogleMaps\DataForSEO_Output\mg_extracted_GoogleMapsDataset_hospital_raw.json'


# Read the JSON data from the file
with open(json_file) as json_file:
    data = json.load(json_file)
    print("File opened")

# Extract items from JSON
items = data['tasks'][0]['result'][0]['items']

# Initialize lists to store data
type_list = []
rank_absolute_list = []
title_list = []
rating_list = []
rating_type_list = []

# Iterate through items and extract required fields
for item in items:
    type_list.append(item['type'])
    rank_absolute_list.append(item['rank_absolute'])
    title_list.append(item['title'])
    if 'rating' in item and item['rating'] is not None:
        rating_list.append(item['rating']['value'])  # Assuming you want the 'value' from rating
        rating_type_list.append(item['rating']['rating_type'])  # Assuming you want the 'rating_type' from rating
    else:
        rating_list.append(None)
        rating_type_list.append(None)

# Create DataFrame
df = pd.DataFrame({
    'type': type_list,
    'rank_absolute': rank_absolute_list,
    'title': title_list,
    'rating': rating_list,
    'rating_type': rating_type_list
})

# Display the DataFrame
print(df)