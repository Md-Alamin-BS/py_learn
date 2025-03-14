import json
import os

def extract_tops_and_bottoms(input_file, output_file):
    # 1. Read the JSON file
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 2. Open the output text file in write mode
    with open(output_file, 'w', encoding='utf-8') as out:
        # 3. Iterate over each record in the JSON list
        for index, record in enumerate(data, start=1):
            name = record.get("name", "Unknown")
            top_md = record.get("mdRkb", "N/A")
            # Safely get the bottom.mdRkb
            bottom_info = record.get("bottom", {})
            bottom_md = bottom_info.get("mdRkb", "N/A")
            
            # 4. Write the extracted information in the desired format
            out.write(f"{index}. Name: {name}. Top: {top_md}, Bottom: {bottom_md}\n")

if __name__ == "__main__":
    # Provide the paths to your JSON and output text file
    base_dir = os.path.dirname(__file__)
    input_path = os.path.join(base_dir, "input.json")
    output_path = os.path.join(base_dir, "output.txt")
    extract_tops_and_bottoms(input_path, output_path)
