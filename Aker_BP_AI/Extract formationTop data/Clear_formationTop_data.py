import json
import os

def filter_json_data(input_file, output_file):
    # 1. Read the JSON file
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 2. Filter the data to keep only the specified fields
    filtered_data = []
    for record in data:
        filtered_record = {
            "name": record.get("name", "Unknown"),
            "description": record.get("description", "N/A"),
            "mdRkb": record.get("mdRkb", "N/A"),
            "lithostratigraphy": record.get("lithostratigraphy", "N/A"),
            "bottom": record.get("bottom", {}).get("mdRkb", "N/A"),
            "wellbore": record.get("wellbore", {}).get("name", "N/A")
        }
        filtered_data.append(filtered_record)
    
    # 3. Write the filtered data to the output JSON file
    with open(output_file, 'w', encoding='utf-8') as out:
        json.dump(filtered_data, out, indent=4)

if __name__ == "__main__":
    # Provide the paths to your JSON and output JSON file
    base_dir = os.path.dirname(__file__)
    input_path = os.path.join(base_dir, "input.json")
    output_path = os.path.join(base_dir, "filtered_output.json")
    filter_json_data(input_path, output_path)