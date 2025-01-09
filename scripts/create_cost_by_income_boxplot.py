import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the file path for the dataset
data_path = r'C:/Users/patel\DAT5902_lab/FinalProject\data/Food_Prices_For_Nutrition.xlsx'

try:
    # Step 1: Load the main data sheet containing diet costs for various countries
    main_data = pd.read_excel(data_path, sheet_name='Data')
    
    # Step 2: Load metadata sheet containing country income groups and regions
    country_metadata = pd.read_excel(data_path, sheet_name='Country - Metadata')
    
    # Step 3: Merge the main data with country metadata on the country name
    # This ensures that income groups and regions are added to the dataset
    merged_data = pd.merge(
        main_data, 
        country_metadata, 
        left_on='Country Name', 
        right_on='Table Name', 
        how='left'
    )
    
    # Step 4: Transform the dataset to create a long format suitable for plotting
    # Each row represents the cost of a specific diet type for a particular income group
    filtered_data = merged_data.melt(
        id_vars=['Income Group'],  # Keep the income group as an identifier
        value_vars=[
            'Cost of an energy sufficient diet',
            'Cost of a nutrient adequate diet',
            'Cost of a healthy diet'
        ],
        var_name='Diet Type',  # Create a column for diet types
        value_name='Cost'  # Create a column for corresponding costs
    )

    # Step 5: Replace long column names with shorter, more readable labels for visualisation
    filtered_data['Diet Type'] = filtered_data['Diet Type'].replace({
        'Cost of an energy sufficient diet': 'Energy sufficient diet',
        'Cost of a nutrient adequate diet': 'Nutrient adequate diet',
        'Cost of a healthy diet': 'Healthy diet'
    })

    # Step 6: Drop rows where the Income Group is missing, as these cannot be categorised
    filtered_data = filtered_data.dropna(subset=['Income Group'])

    # Step 7: Set up the figure and styling for the plot
    plt.figure(figsize=(12, 8))  # Define the figure size
    sns.set_style("whitegrid")  # Apply a clean white grid style

    # Step 8: Define a custom colour palette with 3 distinct colours for the diet types
    palette = sns.color_palette("Set2", n_colors=3)

    # Step 9: Create a boxplot to visualise the distribution of diet costs by income group
    sns.boxplot(
        data=filtered_data,
        x='Income Group',
        y='Cost',
        hue='Diet Type',  # Differentiate costs by diet type
        palette=palette,  # Apply the custom colour palette
        width=0.6  # Adjust box width for better spacing
    )

    # Step 10: Customise x-axis labels for better readability
    # Multi-line labels are used to avoid crowding
    plt.xticks(
        ticks=[0, 1, 2, 3],  # Positions of the labels
        labels=['Upper\nmiddle income', 'Lower\nmiddle income', 'High\nincome', 'Low\nincome'], 
        fontsize=14, 
        fontweight='bold'
    )

    # Step 11: Add gridlines to improve readability of the plot
    plt.grid(visible=True, which='major', linestyle='--', linewidth=0.7, alpha=0.7)

    # Step 12: Set axis labels and title with increased font size and bold styling
    plt.xlabel('Country Income Group', fontsize=16, fontweight='bold', labelpad=20)  # Add space below x-axis label
    plt.ylabel('Cost (USD, 2021)', fontsize=16, fontweight='bold', labelpad=20)  # Add space to the left of y-axis label
    plt.title('Cost of Diets by Income Group', fontsize=18, fontweight='bold')  # Add a title

    # Step 13: Customise the legend to stretch horizontally and improve readability
    plt.legend(
        fontsize=14,  # Increase font size for legend items
        title_fontsize=16,  # Increase font size for the legend title
        loc='upper center',  # Position the legend at the top center
        bbox_to_anchor=(0.5, -0.25),  # Adjust position to stretch horizontally below the plot
        ncol=3,  # Arrange legend items in a single row
        frameon=False  # Remove the legend border
    )

    # Step 14: Remove unnecessary spines for a cleaner look
    sns.despine(left=True, bottom=True)

    # Step 15: Adjust layout to ensure all elements fit well within the figure
    plt.tight_layout(pad=2)  # Add padding around the plot for better spacing

    # Step 16: Save the final figure as a PNG file in the figures directory
    plt.savefig('./figures/cost_by_income_boxplot.png', bbox_inches='tight')
    print("\nVisualization saved to './figures/cost_by_income_boxplot.png'.")

    # Step 17: Display the plot
    plt.show()

except KeyError as e:
    # Handle missing column errors in the dataset
    print(f"KeyError: {e}. Check column names in the dataset.")
except Exception as e:
    # Handle any other unexpected errors
    print(f"Error: {e}")
