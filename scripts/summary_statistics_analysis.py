import pandas as pd

# Step 1: Load the data
data_path = './data/Food_Prices_For_Nutrition.xlsx'

try:
    # Load the main data sheet
    main_data = pd.read_excel(data_path, sheet_name='Data')
    
    # Load the country metadata sheet for income group and region
    country_metadata = pd.read_excel(data_path, sheet_name='Country - Metadata')
    
    # Merge the main dataset with country metadata
    merged_data = pd.merge(
        main_data,
        country_metadata,
        left_on='Country Name',
        right_on='Table Name',
        how='left'
    )

    # Display the first few rows to confirm data is loaded correctly
    print("Data loaded successfully:")
    print(merged_data.head())

except Exception as e:
    print(f"Error loading data: {e}")
