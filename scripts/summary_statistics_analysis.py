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

# Step 2: Calculate summary statistics
try:
    # Select columns for diet costs and affordability
    diet_costs = merged_data[['Cost of an energy sufficient diet', 'Cost of a nutrient adequate diet', 'Cost of a healthy diet']]
    
    affordability = merged_data[['Percent of the population who cannot afford sufficient calories', 'Percent of the population who cannot afford nutrient adequacy', 'Percent of the population who cannot afford a healthy diet']]
    
    # Calculate summary statistics for diet costs
    diet_cost_stats = diet_costs.describe()  # Mean, median, std, etc.
    print("\nSummary Statistics for Diet Costs:")
    print(diet_cost_stats)

    # Calculate summary statistics for affordability
    affordability_stats = affordability.describe()
    print("\nSummary Statistics for Affordability:")
    print(affordability_stats)

    # Save summary statistics to CSV files
    diet_cost_stats.to_csv('./summary_stats_results/diet_cost_summary.csv', index=True)
    affordability_stats.to_csv('./summary_stats_results/affordability_summary.csv', index=True)
    print("\nSummary statistics saved to './summary_stats_results/' folder.")

except Exception as e:
    print(f"Error calculating summary statistics: {e}")
