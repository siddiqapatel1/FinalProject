import pandas as pd
import matplotlib.pyplot as plt

# Path to the dataset
data_path = './data/Food_Prices_For_Nutrition.xlsx'

# Load the dataset
try:
    # Load the dataset into a DataFrame
    df = pd.read_excel(data_path, sheet_name='Data')

    # Extract relevant columns for the pie chart
    pie_chart_data = df[['Cost of fruits', 'Cost of starchy staples', 'Cost of vegetables',
                         'Cost of animal-source foods', 'Cost of legumes, nuts and seeds', 
                         'Cost of oils and fats']]

    # Calculate the average cost contribution for each food group globally
    average_contributions = pie_chart_data.mean()

    # Convert contributions to percentages
    total_cost = average_contributions.sum()
    percentage_contributions = (average_contributions / total_cost) * 100

    # Print the calculated percentages for verification
    print("Percentage Contributions of Each Food Group:\n", percentage_contributions)

    # Labels for the pie chart
    labels = ['Fruits', 'Starchy Staples', 'Vegetables', 'Animal-Source Foods', 
              'Legumes, Nuts and Seeds', 'Oils and Fats']

    # Create the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(percentage_contributions, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Set3.colors)

# Add a title
    plt.title('Average Percentage Contribution of Each Food Group to the Cost of a Healthy Diet', fontsize=14)

# Add a detailed caption
    plt.gcf().text(
    0.5, -0.05,  # Position (centre horizontally, slightly below the figure)
    "Figure 1: Average Percentage Contribution of Each Food Group to the Global Cost of a Healthy Diet (2017 USD). "
    "This pie chart illustrates the proportion of costs contributed by different food groups to the overall cost "
    "of a healthy diet. Animal-source foods contribute the largest share at 31%, followed by vegetables (23%) and fruits (21%).",
    wrap=True, horizontalalignment='center', fontsize=10
)


    # Save the figure
    plt.savefig('./figures/pie_chart_cost_contributions.png', bbox_inches='tight')
    print("Pie chart saved to './figures/pie_chart_cost_contributions.png'")

    # Show the plot (optional)
    plt.show()

except Exception as e:
    print(f"Error loading or processing the dataset: {e}")
