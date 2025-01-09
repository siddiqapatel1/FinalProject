# Test Descriptions

This document provides an overview of the key unit tests included in the repository to validate the analysis and visualisations.

## Summary Statistics Tests

- **test_required_columns_exist**:
  Verifies that the dataset contains all the required columns for calculating summary statistics, such as diet costs and affordability percentages.

- **test_summary_statistics_calculations**:
  Confirms that the summary statistics, such as mean values, are calculated correctly using a mock dataset.

- **test_cost_ratios**:
  Validates the correct calculation of cost ratios for diet types (e.g., healthy diet vs energy sufficient diet).

- **test_output_files**:
  Ensures that the CSV files containing the summary statistics are saved in the expected directory.

## Pie Chart Tests

- **test_percentage_contributions_sum**:
  Ensures that the percentage contributions of food groups in the pie chart sum to 100%, validating the accuracy of the visualisation.

- **test_pie_chart_saved**:
  Checks that the pie chart image is successfully saved in the expected location.

## Boxplot Tests

- **test_critical_columns_exist**:
  Verifies that all required columns for creating the boxplot exist in the merged dataset.

- **test_boxplot_data_validity**:
  Ensures that the filtered data used for the boxplot contains no missing values and includes all diet types.

- **test_cost_values_within_expected_range**:
  Validates that cost values in the boxplot dataset fall within a reasonable range.

## Affordability Bar Chart Tests

- **test_required_columns_exist**:
  Ensures that the dataset contains all the required columns for affordability analysis.

- **test_data_filtering**:
  Verifies that rows with null income group values are properly filtered out during data preparation.
  
- **test_figure_saved**:
  Checks that the affordability bar chart image is saved successfully in the expected location.
