import pandas as pd
from datetime import datetime

# File paths
before_file = 'data_transformation/excel_files/before_sorting.xlsx'
output_file = 'data_transformation/excel_files/file_output_subcolumns.xlsx'

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

    # Debug: Print identified tags
    print("Normal Tags:", tags)
    print("Average Tags:", avg_tags)

    metrics = ['Precision', 'Recall', 'F1']

    # Prepare the after sorting format
    data = []

    def add_data(tag, metric, before_data):
        """Helper function to add data for a specific tag and metric."""
        before_col = f"{tag} {metric.lower()}"
        after_col = f"{tag} {metric.lower()}"

        # Append the values to the data structure
        before_value = before_data[before_col].iloc[0] if before_col in before_data.columns else ''
        after_value = before_data[after_col].iloc[1] if after_col in before_data.columns else ''

        return before_value, after_value

    # Process normal tags
    for tag in tags:
        row = {'Tag': tag}
        for metric in metrics:
            before_value, after_value = add_data(tag, metric, before_data)
            row[(metric, 'Before')] = before_value
            row[(metric, 'After')] = after_value
        data.append(row)

    # Add a blank row before avg tags
    data.append({'Tag': '', ('Precision', 'Before'): '', ('Precision', 'After'): '',
                 ('Recall', 'Before'): '', ('Recall', 'After'): '', ('F1', 'Before'): '', ('F1', 'After'): ''})

    # Process avg tags
    for tag in avg_tags:
        row = {'Tag': tag}
        for metric in metrics:
            if metric.lower() in tag.lower():  # Only add data for relevant metric
                before_col = [col for col in before_data.columns if tag in col and metric.lower() in col.lower()]
                if before_col:
                    before_value = before_data[before_col[0]].iloc[0]
                    after_value = before_data[before_col[0]].iloc[1]
                else:
                    before_value, after_value = '', ''
                row[(metric, 'Before')] = before_value
                row[(metric, 'After')] = after_value
            else:
                row[(metric, 'Before')] = ''
                row[(metric, 'After')] = ''
        data.append(row)

    # Create a DataFrame in the desired format with multi-level columns
    df = pd.DataFrame(data)

    # Separate 'Tag' column and create MultiIndex for the remaining columns
    tag_column = df.pop('Tag')
    df.columns = pd.MultiIndex.from_tuples(df.columns)

    # Save the output to an Excel file
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        workbook = writer.book
        worksheet = workbook.add_worksheet('Sheet1')
        writer.sheets['Sheet1'] = worksheet

        # Write the 'Tag' column header manually
        worksheet.write(0, 0, 'Tag')

        # Write the multi-level headers for the remaining columns
        header_top = [col[0] for col in df.columns]
        header_sub = [col[1] for col in df.columns]

        current_top = None
        start_col = 1

        for col_num, (top, sub) in enumerate(zip(header_top, header_sub), start=1):
            if top != current_top:
                if current_top is not None:
                    worksheet.merge_range(0, start_col, 0, col_num - 1, current_top)
                current_top = top
                start_col = col_num

            worksheet.write(1, col_num, sub)

        # Merge the final group
        if current_top is not None:
            worksheet.merge_range(0, start_col, 0, len(header_top), current_top)

        # Write the data starting from row 2
        worksheet.write_column(2, 0, tag_column)
        for row_num, row_data in enumerate(df.values, start=2):
            for col_num, cell_value in enumerate(row_data, start=1):
                worksheet.write(row_num, col_num, cell_value)
                
    print(f"File successfully created at: {output_file}")

# Process the data
process_excel(before_file, output_file)