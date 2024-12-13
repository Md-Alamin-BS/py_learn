import pandas as pd
from datetime import datetime

# File paths
before_file = 'data_transformation/excel_files/before_sorting.xlsx'
output_file = 'data_transformation/excel_files/file_output.xlsx'

def process_excel(before_file, output_file):
    # Load the before sorting data
    before_data = pd.read_excel(before_file, sheet_name='in')

    # Extract all unique tags dynamically from the column names
    tags = set()
    avg_tags = set()

    for col in before_data.columns:
        if any(metric in col.lower() for metric in ['precision', 'recall', 'f1']):
            if 'avg' in col.lower():
                tag = col.split()[0]  # Extract the tag for avg columns
                avg_tags.add(tag)
            else:
                tag = ' '.join(col.split()[:-1])  # Extract the tag for normal columns
                tags.add(tag)

    tags = sorted(tags)
    avg_tags = sorted(avg_tags)

    metrics = ['Precision', 'Recall', 'F1']

    # Prepare the after sorting format
    after_data = {'Tag': [], 'Precision Before': [], 'Precision After': [],
                  'Recall Before': [], 'Recall After': [], 'F1 Before': [], 'F1 After': []}

    def add_data(tag, metric, before_data):
        """Helper function to add data for a specific tag and metric."""
        before_col = f"{tag} {metric.lower()}"
        after_col = f"{tag} {metric.lower()}"

        # Append the values to the after_data structure
        before_value = before_data[before_col].iloc[0] if before_col in before_data.columns else ''
        after_value = before_data[after_col].iloc[1] if after_col in before_data.columns else ''

        return before_value, after_value

    # Process normal tags
    for tag in tags:
        after_data['Tag'].append(tag)

        for metric in metrics:
            before_value, after_value = add_data(tag, metric, before_data)
            after_data[f'{metric} Before'].append(before_value)
            after_data[f'{metric} After'].append(after_value)

    # Add a blank row before avg tags
    after_data['Tag'].append('')
    for metric in metrics:
        after_data[f'{metric} Before'].append('')
        after_data[f'{metric} After'].append('')

    # Process avg tags
    for tag in avg_tags:
        after_data['Tag'].append(tag)

        for metric in metrics:
            if metric.lower() in tag.lower():  # Only add data for relevant metric
                before_col = [col for col in before_data.columns if tag in col and metric.lower() in col.lower()]
                if before_col:
                    before_value = before_data[before_col[0]].iloc[0]
                    after_value = before_data[before_col[0]].iloc[1]
                else:
                    before_value, after_value = '', ''
            else:
                before_value, after_value = '', ''

            after_data[f'{metric} Before'].append(before_value)
            after_data[f'{metric} After'].append(after_value)

    # Create a DataFrame in the desired format
    after_df = pd.DataFrame(after_data)

    # Save the output to an Excel file
    after_df.to_excel(output_file, index=False, sheet_name='Sheet1', float_format="%.15g")
    
    print(f"File successfully created at: {output_file}")

# Process the data
process_excel(before_file, output_file)
