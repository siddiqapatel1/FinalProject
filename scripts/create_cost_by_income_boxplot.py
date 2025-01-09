import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_path = r'C:/Users/patel\DAT5902_lab/FinalProject\data/Food_Prices_For_Nutrition.xlsx'

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
    
    filtered_data = merged_data.melt(
        id_vars=['Income Group'],
        value_vars=[
            'Cost of an energy sufficient diet',
            'Cost of a nutrient adequate diet',
            'Cost of a healthy diet'
        ],
        var_name='Diet Type',
        value_name='Cost'
    )

    # Replace long column names with shorter labels for visualisation
    filtered_data['Diet Type'] = filtered_data['Diet Type'].replace({
        'Cost of an energy sufficient diet': 'Energy sufficient diet',
        'Cost of a nutrient adequate diet': 'Nutrient adequate diet',
        'Cost of a healthy diet': 'Healthy diet'
    })

    # Drop rows with missing Income Group
    filtered_data = filtered_data.dropna(subset=['Income Group'])

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create the boxplot
    sns.boxplot(
        data=filtered_data,
        x='Income Group',
        y='Cost',
        hue='Diet Type',
        palette='colorblind',
        ax=ax
    )

    # Add gridlines
    ax.grid(visible=True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

    # Customize the plot
    ax.set_title('Cost of Diets by Income Group', fontsize=18)
    ax.set_xlabel('Country Income Group', fontsize=14)
    ax.set_ylabel('Cost (USD, 2022)', fontsize=14)
    ax.legend(title='Diet Type', fontsize=12)
    plt.xticks(rotation=30)

    fig.text(
    0.5, 0.01, 
    "Figure 1: This shows the distribution of diet costs across income groups. Healthy diets are consistently the most expensive option.",
    wrap=True, horizontalalignment='center', fontsize=10
    )
    plt.tight_layout(rect=[0, 0.04, 1, 1])  

    # Save the figure
    plt.savefig('./figures/cost_by_income_boxplot.png', bbox_inches='tight')
    print("\nVisualization saved to './figures/cost_by_income_boxplot.png'.")

except KeyError as e:
    print(f"KeyError: {e}. Check column names in the dataset.")
except Exception as e:
    print(f"Error: {e}")
