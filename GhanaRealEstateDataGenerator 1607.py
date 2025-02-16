import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

class GhanaRealEstateDataGenerator:
    def __init__(self, start_date, end_date, base_params):
        self.start_date = start_date
        self.end_date = end_date
        self.base_params = base_params
        self.date_range = pd.date_range(start=start_date, end=end_date)
        self.years = (end_date.year - start_date.year) + 1
        
    def generate_region_data(self):
        regions = [
            'Greater Accra', 'Ashanti', 'Western', 'Central', 'Eastern',
            'Bono', 'Bono East', 'Ahafo', 'Brong Ahafo', 'Northern'
        ]
        return pd.DataFrame({
            'region_id': range(1, len(regions) + 1),
            'region_name': regions
        })

    def generate_town_data(self):
        towns = {
            'Greater Accra': [
                'Accra', 'Tema', 'Ga West', 'Accra-Central', 'Achimota', 'Adenta Municipality',
                'Adjen Kotoku', 'Airport', 'Amasaman', 'Amrahia', 'Darkuman', 'Dawhenya',
                'Haatso', 'Lapaz', 'Madina', 'Mallam', 'Mile 11', 'Pantang West', 'Sakumono',
                'Sowutoum', 'Swanlake', 'Taifa', 'Tsuibleoo'
            ],
            'Ashanti': [
                'Kumasi', 'Obuasi', 'Konongo', 'Aboaso', 'Abofour', 'Adanwomase', 'Adum', 'Aduman',
                'Agogo', 'Ahenema Kokobin', 'Ahwiaa', 'Amankyim', 'Antoa', 'Asante-Asamang',
                'Asienimpong', 'Asiwa', 'Atwima Brofoyedur', 'Bekwai', 'Bodwesango', 'Duayaw Nkwanta',
                'Effiduase', 'Ejisu', 'Fomena', 'Gyamase', 'Jacobo', 'Juaben', 'Kodee', 'Kokofu',
                'Kumawu', 'Kuntanse', 'Kuntunse', 'Mampong', 'Manso Atwere', 'Mpasatia', 'New Edubiase',
                'Ntonso', 'Ofinso', 'Ofoase Kokoben', 'Pepease', 'Sekyedumase', 'Sokoban', 'Wiamoase'
            ],
            'Western': ['Sekondi-Takoradi', 'Tarkwa', 'Axim'],
            'Central': ['Cape Coast', 'Winneba', 'Kasoa', 'Assin Manso', 'Fanti Nyankumasi', 'Foso'],
            'Eastern': [
                'Koforidua', 'Nkawkaw', 'Nsawam', 'Aburi', 'Adukrom', 'Adumasa', 'Akim Oda', 'Akoasi',
                'Akosombo', 'Akropong', 'Akyease', 'Akyem Kukurantumi', 'Akyem Kwabeng', 'Anum', 
                'Anyinam', 'Asamankese', 'Asuom', 'Hills', 'Juapong', 'Kade', 'Kpong', 'Krofa', 
                'Kyebi', 'Mamfe', 'Mpraeso', 'New Abirem', 'Nsuta', 'Ogbodjo', 'Oseim', 'Osino', 
                'Pramso', 'Somanya', 'Suhenso', 'Suhum', 'Tease'
            ],
            'Bono': ['Sunyani'],
            'Bono East': ['Techiman'],
            'Ahafo': ['Bibiani'],
            'Brong Ahafo': ['Nkoranza'],
            'Northern': ['Tamale']
        }
        
        town_data = []
        town_id = 1
        for region, region_towns in towns.items():
            for town in region_towns:
                town_data.append({
                    'town_id': town_id,
                    'town_name': town,
                    'region_name': region
                })
                town_id += 1
        
        return pd.DataFrame(town_data)

    def generate_property_type_data(self):
        property_types = ['Apartment', 'House', 'Land', 'Commercial']
        return pd.DataFrame({
            'property_type_id': range(1, len(property_types) + 1),
            'property_type_name': property_types
        })

    def generate_sales_type_data(self):
        sales_types = ['Rent', 'Sale']
        return pd.DataFrame({
            'sales_type_id': range(1, len(sales_types) + 1),
            'sales_type_name': sales_types
        })

    def generate_buyer_data(self, num_buyers=316):
        buyer_types = ['Individual', 'Company', 'Investment Fund']
        occupations = ['Employed', 'Self-employed', 'Investor']
        age_groups = ['18-30', '31-45', '46-60', '60+']
        
        buyers = []
        for i in range(1, num_buyers + 1):
            buyers.append({
                'buyer_id': i,
                'buyer_name': f'Buyer_{i}',
                'buyer_type': np.random.choice(buyer_types),
                'occupation': np.random.choice(occupations),
                'age_group': np.random.choice(age_groups)
            })
        
        return pd.DataFrame(buyers)

    def generate_seller_data(self, num_sellers=645):
        seller_types = ['Individual', 'Company', 'Bank', 'Government']
        
        sellers = []
        for i in range(1, num_sellers + 1):
            sellers.append({
                'seller_id': i,
                'seller_name': f'Seller_{i}',
                'seller_type': np.random.choice(seller_types),
                'years_of_ownership': np.random.randint(1, 20)
            })
        
        return pd.DataFrame(sellers)

    def generate_property_details(self, num_properties=500546):
        region_data = self.generate_region_data()
        town_data = self.generate_town_data()
        property_type_data = self.generate_property_type_data()
        sales_type_data = self.generate_sales_type_data()
        buyer_data = self.generate_buyer_data()
        seller_data = self.generate_seller_data()

        properties = []
        for i in range(1, num_properties + 1):
            try:
                town = town_data.sample().iloc[0]
                region_name = town['region_name']
                
                if region_name not in region_data['region_name'].values:
                    print(f"Warning: Region '{region_name}' not found in region data. Using default values.")
                    region = pd.Series({'region_id': -1, 'region_name': region_name})
                else:
                    region = region_data[region_data['region_name'] == region_name].iloc[0]

                property_type = property_type_data.sample().iloc[0]
                sales_type = sales_type_data.sample().iloc[0]
                buyer = buyer_data.sample().iloc[0]
                seller = seller_data.sample().iloc[0]

                bedrooms, size_sqft = self.generate_property_specs(property_type['property_type_name'], region_name)

                date_on_market = pd.to_datetime(np.random.choice(self.date_range)).to_pydatetime()
                
                # Determine if the property is sold
                is_sold = random.random() > 0.1768  # 80% chance of being sold
                
                if is_sold:
                    days_on_market = random.randint(
                        self.base_params['min_days_on_market'],
                        self.base_params['max_days_on_market']
                    )
                    date_off_market = date_on_market + timedelta(days=days_on_market)
                else:
                    days_on_market = (self.end_date - date_on_market).days
                    date_off_market = None

                base_price = self.base_params['avg_property_price']
                region_factor = self.base_params['region_price_factors'].get(region_name, 1.0)
                property_type_factor = self.base_params['property_type_price_factors'][property_type['property_type_name']]
                year_factor = 1 + (self.base_params['yearly_price_growth'].get(region_name, 0.05) * (date_on_market.year - self.start_date.year))
                
                size_factor = size_sqft / 1000  # Assume 1000 sqft is the baseline
                bedroom_factor = 1 + (bedrooms * 0.1)  # Each bedroom increases price by 10%
                
                month = date_on_market.month
                seasonal_factor = self.base_params['seasonal_factors'][month - 1]
                
                economic_growth_factor = 1 + (self.base_params['economic_growth_rate'] * (date_on_market.year - self.start_date.year))
                
                inflation_factor = 1 + (self.base_params['inflation_rate'] * (date_on_market.year - self.start_date.year))
                interest_rate_factor = 1 - (self.base_params['interest_rate'] * 0.01)
                employment_factor = 1 + (self.base_params['employment_growth_rate'] * (date_on_market.year - self.start_date.year))
                
                urbanization_factor = 1 + (self.base_params['urbanization_rate'].get(region_name, 0.02) * (date_on_market.year - self.start_date.year))
                
                price = (base_price * region_factor * property_type_factor * year_factor * 
                        seasonal_factor * economic_growth_factor * inflation_factor * 
                        interest_rate_factor * employment_factor * urbanization_factor * 
                        size_factor * bedroom_factor *
                        np.random.normal(1, self.base_params['price_volatility']))

                if sales_type['sales_type_name'] == 'Rent':
                    annual_rent_ratio = self.base_params['rent_to_price_ratio'][property_type['property_type_name']]
                    price = price * annual_rent_ratio / 12  # Monthly rent

                school_district_rating = self.generate_school_rating(region_name, town['town_name'])
                crime_rate = self.generate_crime_rate(region_name, town['town_name'])
                distance_to_transport = self.generate_transport_distance(region_name, town['town_name'], property_type['property_type_name'])

                properties.append({
                    'property_id': i,
                    'buyer_id': buyer['buyer_id'],
                    'seller_id': seller['seller_id'],
                    'town_id': town['town_id'],
                    'region_id': region['region_id'],
                    'property_type_id': property_type['property_type_id'],
                    'sales_type_id': sales_type['sales_type_id'],
                    'property_description': f'{bedrooms} bedroom {property_type["property_type_name"]} in {town["town_name"]}, {region_name}',
                    'price_ghc': round(price, 2),
                    'date_on_market': date_on_market,
                    'date_off_market': date_off_market,
                    'days_on_market': days_on_market,
                    'bedrooms': bedrooms,
                    'size_sqft': size_sqft,
                    'school_district_rating': school_district_rating,
                    'crime_rate': crime_rate,
                    'distance_to_transport': distance_to_transport,
                    'office_space_demand': self.base_params['office_space_demand'].get(date_on_market.year, 1.0)
                })
            except Exception as e:
                print(f"Error generating property {i}: {str(e)}")
                continue

        return pd.DataFrame(properties)

    def generate_property_specs(self, property_type, region):
        bedroom_ranges = {
            'Apartment': (1, 3),
            'House': (2, 5),
            'Commercial': (0, 2),
            'Land': (0, 0)
        }

        size_ranges = {
            'Apartment': {
                'Greater Accra': (400, 1500),
                'Ashanti': (350, 1200),
                'default': (300, 1000)
            },
            'House': {
                'Greater Accra': (800, 3000),
                'Ashanti': (700, 2500),
                'default': (600, 2000)
            },
            'Commercial': {
                'Greater Accra': (1000, 5000),
                'Ashanti': (800, 4000),
                'default': (500, 3000)
            },
            'Land': {
                'Greater Accra': (2000, 10000),
                'Ashanti': (1500, 8000),
                'default': (1000, 5000)
            }
        }

        min_bedrooms, max_bedrooms = bedroom_ranges[property_type]
        bedrooms = random.randint(min_bedrooms, max_bedrooms)

        size_range = size_ranges[property_type].get(region, size_ranges[property_type]['default'])
        size_sqft = random.randint(*size_range)

        return bedrooms, size_sqft

    def generate_school_rating(self, region, town):
        base_rating = {
            'Greater Accra': 7,
            'Ashanti': 6,
            'Western': 5,
            'Central': 5,
            'Eastern': 5,
            'Bono': 4,
            'Bono East': 4,
            'Ahafo': 4,
            'Brong Ahafo': 4,
            'Northern': 3
        }.get(region, 4)
        
        if town in ['Accra', 'Kumasi', 'Sekondi-Takoradi', 'Cape Coast', 'Koforidua', 'Sunyani', 'Techiman', 'Goaso', 'Tamale']:
            base_rating += 1
        
        return min(max(int(np.random.normal(base_rating, 1)), 1), 10)

    def generate_crime_rate(self, region, town):
        base_rate = {
            'Greater Accra': 60,
            'Ashanti': 55,
            'Western': 50,
            'Central': 45,
            'Eastern': 40,
            'Bono': 35,
            'Bono East': 35,
            'Ahafo': 30,
            'Brong Ahafo': 35,
            'Northern': 40
        }.get(region, 40)
        
        if town in ['Accra', 'Kumasi', 'Sekondi-Takoradi', 'Cape Coast', 'Koforidua', 'Sunyani', 'Techiman', 'Tamale']:
            base_rate += 10
        elif town in ['Tema', 'Obuasi', 'Tarkwa', 'Nkawkaw', 'Bibiani', 'Nkoranza']:
            base_rate += 5
        
        return min(max(int(np.random.normal(base_rate, 10)), 0), 100)

    def generate_transport_distance(self, region, town, property_type):
        base_distance = {
            'Greater Accra': 2,
            'Ashanti': 3,
            'Western': 4,
            'Central': 4,
            'Eastern': 5,
            'Bono': 5,
            'Bono East': 6,
            'Ahafo': 6,
            'Brong Ahafo': 5,
            'Northern': 6
        }.get(region, 5)
        
        if property_type == 'Commercial':
            base_distance -= 1
        elif property_type == 'Land':
            base_distance += 2
        
        if town in ['Accra', 'Kumasi', 'Sekondi-Takoradi', 'Cape Coast', 'Koforidua', 'Sunyani', 'Techiman', 'Tamale']:
            base_distance -= 1
        
        return max(round(np.random.normal(base_distance, 1), 1), 0.1)

    def generate_all_data(self):
        return {
            'regions': self.generate_region_data(),
            'towns': self.generate_town_data(),
            'property_types': self.generate_property_type_data(),
            'sales_types': self.generate_sales_type_data(),
            'buyers': self.generate_buyer_data(),
            'sellers': self.generate_seller_data(),
            'property_details': self.generate_property_details()
        }

# Base parameters
base_params = {
    'avg_property_price': 180500,  # in GHS
    'yearly_price_growth': {
        'Greater Accra': 0.08,
        'Ashanti': 0.06,
        'Western': 0.05,
        'Central': 0.04,
        'Eastern': 0.04,
        'Bono': 0.04,
        'Bono East': 0.035,
        'Ahafo': 0.03,
        'Brong Ahafo': 0.035,
        'Northern': 0.03
    },
    'economic_growth_rate': 0.05,  # 5% yearly economic growth
    'price_volatility': 0.02,  # 2% standard deviation in price variations
    'min_days_on_market': 26,
    'max_days_on_market': 250,
    'rent_to_price_ratio': {
        'Apartment': 0.04,  # 4% annual rent for apartments
        'House': 0.03,      # 3% annual rent for houses
        'Commercial': 0.06, # 6% annual rent for commercial properties
        'Land': 0.02        # 2% annual rent for land (rare, but possible)
    },
    'region_price_factors': {
        'Greater Accra': 1.5,
        'Ashanti': 1.2,
        'Western': 1.1,
        'Central': 0.9,
        'Eastern': 0.8,
        'Bono': 1.0,
        'Bono East': 0.95,
        'Ahafo': 0.9,
        'Brong Ahafo': 0.95,
        'Northern': 0.85
    },
    'property_type_price_factors': {
        'Apartment': 1.2,
        'House': 1.5,
        'Land': 0.8,
        'Commercial': 2.0
    },
    'seasonal_factors': [
        0.95, 0.97, 1.0, 1.02, 1.05, 1.08,  # Jan to Jun
        1.10, 1.12, 1.08, 1.05, 1.02, 1.0   # Jul to Dec
    ],
    'inflation_rate': 0.09,  # 9% annual inflation
    'interest_rate': 14.5,  # 14.5% interest rate
    'employment_growth_rate': 0.02,  # 2% annual employment growth
    'urbanization_rate': {
        'Greater Accra': 0.03,
        'Ashanti': 0.025,
        'Western': 0.02,
        'Central': 0.015,
        'Eastern': 0.015,
        'Bono': 0.01,
        'Bono East': 0.01,
        'Ahafo': 0.005,
        'Brong Ahafo': 0.01,
        'Northern': 0.015
    },
    'office_space_demand': {
        2018: 1.0,
        2019: 1.05,
        2020: 0.7,  # Decrease due to pandemic
        2021: 0.85,
        2022: 0.9,
        2023: 0.95,
        2024: 0.96
    },
    'new_projects_per_year': {
        2018: 50,
        2019: 60,
        2020: 40,
        2021: 45,
        2022: 55,
        2023: 65,
        2024: 75
    }
}

# Generate data
generator = GhanaRealEstateDataGenerator(
    start_date=datetime(2018, 1, 1),
    end_date=datetime(2024, 7, 31),
    base_params=base_params
)

all_data = generator.generate_all_data()

# Set pandas options to display more columns and rows
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', 10)

# Print sample data
for key, df in all_data.items():
    print(f"\n{key.capitalize()} Data:")
    print(df.head())
    print(f"\nColumns in {key}: {df.columns.tolist()}")
    print(f"Shape of {key}: {df.shape}")

# Save data to CSV files
for key, df in all_data.items():
    df.to_csv(f'ghana_real_estate_{key}_data.csv', index=False)

print("\nData generation complete. CSV files have been created.")