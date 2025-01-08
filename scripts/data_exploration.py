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

    plt.figure(figsize=(10, 6))
    sns.boxplot(
        data=filtered_data,
        x='Income Group',
        y='Cost',
        hue='Diet Type',
        palette='colorblind'  
    )

    plt.title('Cost of Diets by Income Group', fontsize=18)
    plt.xlabel('Country Income Group', fontsize=14)
    plt.ylabel('Cost (USD, 2022)', fontsize=14)
    plt.legend(title='Diet Type', fontsize=12)
    plt.xticks(rotation=30)
    plt.tight_layout()

    # Save the figure
    plt.savefig('./figures/cost_by_income_group.png')
    print("\nVisualization saved to './figures/cost_by_income_group.png'.")

except KeyError as e:
    print(f"KeyError: {e}. Check column names in the dataset.")
except Exception as e:
    print(f"Error: {e}")
