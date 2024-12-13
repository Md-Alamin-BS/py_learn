import pandas as pd
import xlsxwriter

def process_excel(before_file, output_file):
    # Load the data
    df = pd.read_excel(before_file)

    # Create a new Excel file and add a worksheet
    workbook = xlsxwriter.Workbook(output_file)
    worksheet = workbook.add_worksheet()

    # Define formats
    light_red = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'})
    light_green = workbook.add_format({'bg_color': '#C6EFCE', 'font_color': '#006100'})

    # Write data to worksheet
    for row_num, row_data in enumerate(df.values):
        worksheet.write_row(row_num + 1, 0, row_data)

    # Apply conditional formatting
    for row in range(len(df)):
        after_col = 1  # Assuming after_col is column B (index 1)
        before_col = 0  # Assuming before_col is column A (index 0)
        worksheet.conditional_format(row + 1, after_col, row + 1, after_col, {
            'type': 'cell',
            'criteria': '>',
            'value': f'=${chr(65 + after_col)}{row + 2}',
            'format': light_red
        })
        worksheet.conditional_format(row + 1, before_col, row + 1, before_col, {
            'type': 'cell',
            'criteria': '>',
            'value': f'=${chr(65 + before_col)}{row + 2}',
            'format': light_green
        })

    # Adjust column widths
    worksheet.set_column(0, 0, 15)  # Tag column
    worksheet.set_column(1, len(df.columns), 12)  # Data columns

    # Close the workbook
    workbook.close()

    print(f"File successfully created at: {output_file}")

# Process the data
before_file = 'path_to_before_file.xlsx'
output_file = 'path_to_output_file.xlsx'
process_excel(before_file, output_file)