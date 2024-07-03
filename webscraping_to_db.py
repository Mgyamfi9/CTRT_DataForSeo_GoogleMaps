import pandas as pd
import json

# Path to your JSON file
json_file = 'CTRT_DataForSeo_GoogleMaps\DataForSEO_Output\mg_extracted_GoogleMapsDataset_kumasi_schools_raw.json'


# Read the JSON data from the file
with open(json_file) as json_file:
    data = json.load(json_file)
    print("File opened")

# Extract items from JSON
items = data['tasks'][0]['result'][0]['items']

# Flatten the items list including all keys and nested objects
df = pd.json_normalize(items, sep='_')

# Display the DataFrame
print(df)



#df.to_csv('Webscraping_Schools_Output.csv', index=False)

import pandas as pd
from sqlalchemy import create_engine

# Define your connection details
server = 'ctrt-sqlserver.database.windows.net'
database = 'ctrt-sqldb'
username = 'CTRT-admin'
password = 'Hso2Ghana'
port = '1433'  # Default is 1433, e.g., '1433'

# Create the connection string for SQLAlchemy
connection_string = (
    f"mssql+pyodbc://{username}:{password}@{server}:{port}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

# Establish the connection using SQLAlchemy create_engine
engine = create_engine(connection_string, echo=False)  # Set echo=True for debugging


# Define the target schema and table name in the database
new_schema = 'bronze'
new_table_name = 'MG_Church_Kumasi'

# Write DataFrame to the new table in the specified schema in the database
df.to_sql(new_table_name, engine, schema=new_schema, if_exists='replace', index=False)

print(f"Data written to {new_schema}.{new_table_name} successfully.")