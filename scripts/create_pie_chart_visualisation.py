import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Define the data for the pie chart
# Food groups and their percentage contributions to the cost of a healthy diet
food_groups = [
    'Fruits', 
    'Starchy Staples', 
    'Vegetables', 
    'Animal-Source Foods', 
    'Legumes, Nuts and Seeds', 
    'Oils and Fats'
]
contributions = [19.0, 15.9, 20.9, 28.6, 10.7, 4.8]  # Percentage contributions for each food group

# Step 2: Set up the figure and chart aesthetics
# Create the figure with a square layout for balanced visual proportions
plt.figure(figsize=(8, 8))
# Use a consistent and visually appealing color palette
colors = sns.color_palette("Set2", n_colors=len(contributions))

# Step 3: Highlight the most important food group
explode = [0, 0, 0, 0.05, 0, 0]

# Step 4: Create the pie chart
plt.pie(
    contributions, 
    labels=None,  # Labels removed from the slices; legend will be used instead
    autopct='%1.1f%%',  # Display percentages inside the slices
    startangle=90,  # Align the first slice starting at 90 degrees
    colors=colors,  # Apply the defined color palette
    explode=explode,  # Separate the "Animal-Source Foods" slice
    wedgeprops={'edgecolor': 'white', 'linewidth': 1.5},  # Add white borders for better slice visibility
    textprops={'fontsize': 12, 'fontweight': 'bold'}  # Set smaller font size for percentages
)

# Step 5: Add a title with proper formatting
# Title is split across two lines for better readability
plt.title(
    'Average Percentage Contribution of Each Food Group\n to the Cost of a Healthy Diet', 
    fontsize=15, fontweight='bold', pad=20  # Set font size, weight, and padding
)

# Step 6: Add the legend to the right of the chart
# Legend is placed vertically to the right for consistency with report style
plt.legend(
    food_groups,  # Labels for the legend
    loc='center left',  # Position the legend vertically to the left of the chart
    bbox_to_anchor=(1, 0.5),  # Adjust the legend position
    fontsize=12,  # Set font size for readability
    frameon=False  # Remove legend border for a cleaner look
)

# Step 7: Adjust layout and save the chart
# Ensure there is enough spacing around all elements
plt.tight_layout(pad=2.5)
# Save the final figure to the "figures" directory
plt.savefig('./figures/food_group_pie_chart.png', bbox_inches='tight')

# Step 8: Display the chart
# Show the pie chart in the output
plt.show()
