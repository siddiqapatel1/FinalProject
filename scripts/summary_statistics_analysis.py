import pandas as pd
from scipy.stats import pearsonr

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

# Step 2: Calculate necessary summary statistics
try:
    # Select columns for diet costs and affordability
    diet_costs = merged_data[['Cost of an energy sufficient diet', 
                              'Cost of a nutrient adequate diet', 
                              'Cost of a healthy diet']]
    
    affordability = merged_data[['Percent of the population who cannot afford sufficient calories', 
                                  'Percent of the population who cannot afford nutrient adequacy', 
                                  'Percent of the population who cannot afford a healthy diet']]
    
    # Calculate summary statistics for diet costs
    diet_cost_stats = diet_costs.describe()
    print("\nSummary Statistics for Diet Costs:")
    print(diet_cost_stats)

    # Calculate summary statistics for affordability
    affordability_stats = affordability.describe()
    print("\nSummary Statistics for Affordability:")
    print(affordability_stats)

    # Calculate cost ratios (Healthy vs Energy Sufficient and Nutrient Adequate)
    merged_data['Healthy vs Energy Sufficient'] = (
        merged_data['Cost of a healthy diet'] / merged_data['Cost of an energy sufficient diet']
    )
    merged_data['Healthy vs Nutrient Adequate'] = (
        merged_data['Cost of a healthy diet'] / merged_data['Cost of a nutrient adequate diet']
    )
    cost_ratio_stats = merged_data[['Healthy vs Energy Sufficient', 'Healthy vs Nutrient Adequate']].describe()
    print("\nSummary Statistics for Cost Ratios:")
    print(cost_ratio_stats)

    # Save summary statistics to CSV files
    diet_cost_stats.to_csv('./summary_stats_results/diet_cost_summary.csv', index=True)
    affordability_stats.to_csv('./summary_stats_results/affordability_summary.csv', index=True)
    cost_ratio_stats.to_csv('./summary_stats_results/cost_ratios_summary.csv', index=True)
    print("\nSummary statistics saved to './summary_stats_results/' folder.")

except Exception as e:
    print(f"Error calculating summary statistics: {e}")

# Step 3: Perform correlation analysis
try:
    # Drop rows with missing values for relevant columns
    correlation_columns = ['Cost of a healthy diet', 'Cost of fruits', 'Cost of vegetables',
                           'Cost of animal-source foods', 'Cost of legumes, nuts and seeds', 
                           'Cost of oils and fats']
    clean_data = merged_data.dropna(subset=correlation_columns)

    # Correlation between cost of a healthy diet and affordability
    cost_healthy_diet = clean_data['Cost of a healthy diet']
    percent_cannot_afford = clean_data['Percent of the population who cannot afford a healthy diet']
    corr_cost_afford, p_value_afford = pearsonr(cost_healthy_diet, percent_cannot_afford)
    print(f"\nCorrelation between cost of a healthy diet and affordability:")
    print(f"Pearson correlation coefficient: {corr_cost_afford:.2f}, P-value: {p_value_afford:.4f}")

    # Correlation between components and total cost of a healthy diet
    print("\nCorrelation of Healthy Diet Components with Total Cost of a Healthy Diet:")
    for component in correlation_columns[1:]:  # Skip 'Cost of a healthy diet'
        corr, p_val = pearsonr(clean_data[component], cost_healthy_diet)
        print(f"{component}: Pearson r = {corr:.2f}, P-value = {p_val:.4f}")

except Exception as e:
    print(f"Error calculating correlation coefficients: {e}")


# Step 4: Calculate cost of a healthy diet by income group
try:
    # Group the data by Income Group and calculate the mean cost of a healthy diet
    income_group_cost = merged_data.groupby('Income Group')['Cost of a healthy diet'].mean()

    # Display the results
    print("\nAverage Cost of a Healthy Diet by Income Group:")
    print(income_group_cost)

    # Save the results to a CSV file
    income_group_cost.to_csv('./summary_stats_results/healthy_diet_cost_by_income_group.csv', index=True)
    print("\nCost by income group saved to './summary_stats_results/healthy_diet_cost_by_income_group.csv'")

except Exception as e:
    print(f"Error calculating cost by income group: {e}")
