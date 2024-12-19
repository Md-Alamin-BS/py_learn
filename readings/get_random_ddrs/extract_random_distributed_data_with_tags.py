import argparse
from azure.cosmos import CosmosClient, exceptions
import pandas as pd
from dotenv import load_dotenv
import os
import csv

def main(tags, csv_file_name, num_per_range=60, num_random=20):
    # Load environment variables
    load_dotenv()

    # Cosmos DB credentials
    endpoint = os.getenv('COSMOS_URL')
    key = os.getenv('COSMOS_KEY')
    database_name = os.getenv('DATABASE_NAME')
    container_name = os.getenv('CONTAINER_NAME')

    # Initialize the Cosmos client
    client = CosmosClient(endpoint, key)
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)

    # Create an empty list to collect all the data for each tag
    combined_data = []

    for tag in tags:
        # Query to select all records with the given tag
        query = f"""
        SELECT
            c.id,
            c.comment as Text,
            c.phase,
            c.operation.code,
            c.operation.subCode,
            LENGTH(c.comment) as commentLength,
            '{tag}' as label,
            c.tags,
            c.metadata.auto.tags as auto
        FROM 
            c
        WHERE c.docType = 'ddr' 
            AND c.comment != ''    
            AND ARRAY_CONTAINS(c.tags, '{tag}')
        """

        items = list(container.query_items(query=query, enable_cross_partition_query=True))
        
        # Create a DataFrame from the query results
        df = pd.DataFrame(items)

        if df.empty:
            print(f"No items found for tag: {tag}")
            continue

        # Calculate percentiles
        percentile_100 = df['commentLength'].quantile(1.0)
        percentile_66 = df['commentLength'].quantile(0.66)
        percentile_33 = df['commentLength'].quantile(0.33)
        percentile_0 = df['commentLength'].quantile(0.0)

        # Get records for each range
        between_100_and_66 = df[(df['commentLength'] < percentile_100) & (df['commentLength'] >= percentile_66)].head(num_per_range)
        between_66_and_33 = df[(df['commentLength'] < percentile_66) & (df['commentLength'] >= percentile_33)].head(num_per_range)
        between_33_and_0 = df[(df['commentLength'] < percentile_33) & (df['commentLength'] >= percentile_0)].head(num_per_range)

        # Get random records from the dataset
        random_items = df.sample(n=min(num_random, len(df)), random_state=42)

        # Combine the records for this tag
        tag_combined_df = pd.concat([between_100_and_66, between_66_and_33, between_33_and_0, random_items]).drop_duplicates(subset=['id', 'Text']).reset_index(drop=True)

        # Append the combined data for this tag to the list
        combined_data.append(tag_combined_df)

    # Combine all tags data into a single DataFrame
    final_combined_df = pd.concat(combined_data).reset_index(drop=True)

    # Drop duplicates based on the 'id' column to ensure no duplicates across tags
    final_combined_df = final_combined_df.drop_duplicates(subset=['id']).reset_index(drop=True)

    # Ensure the output directory exists
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Full path for the output CSV file
    output_file_path = os.path.join(output_dir, csv_file_name)

    # Write the combined DataFrame to the specified CSV file
    final_combined_df.to_csv(output_file_path, index=False, quoting=csv.QUOTE_ALL)

    print(f"Results for all tags have been written to {output_file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query Cosmos DB based on a list of tags and select records based on comment length ranges.")
    parser.add_argument('csv_file_name', type=str, help="The output CSV file name (e.g., 'tagged_range_results.csv').")
    parser.add_argument('--num_per_range', type=int, default=20, help="Number of records to retrieve for each percentile range (default: 20).")
    parser.add_argument('--num_random', type=int, default=20, help="Number of random records to retrieve (default: 20).")
    
    args = parser.parse_args()
    
    # List of tags to process
    tags = [
        "shallowwater", "shallowgas", "holecleaning", "dheqfailure", 
        "wellborebreathing", "highrop", "boulders", "surfeqfailure", 
        "dircontrol", "stuckpipe", "wellcontrol", "harddrilling", 
        "wellborestability", "packoff", "tighthole", "lowrop", 
        "lostcirculation", "wait"
    ]
    
    # Pass the arguments and the list of tags to the main function
    main(tags, args.csv_file_name, args.num_per_range, args.num_random)
