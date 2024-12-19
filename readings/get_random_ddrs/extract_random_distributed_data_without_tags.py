import argparse
from azure.cosmos import CosmosClient, exceptions
import pandas as pd
from dotenv import load_dotenv
import os
import csv

def main(csv_file_name, num_per_range=60, num_random=20):
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

    # Query to select all records without any tags
    untagged_query = """
    SELECT
        c.id,
        c.comment as Text,
        c.phase,
        c.operation.code,
        c.operation.subCode,
        LENGTH(c.comment) as commentLength,
        'notag' as label,
        c.tags,
        c.metadata.auto.tags as auto
    FROM 
        c
    WHERE c.docType = 'ddr' 
        AND c.comment != ''    
        AND (c.tags = [] OR NOT IS_DEFINED(c.tags))
    """

    untagged_items = list(container.query_items(query=untagged_query, enable_cross_partition_query=True))
    
    # Create a DataFrame from the query results and calculate the percentiles
    untagged_df = pd.DataFrame(untagged_items)

    if not untagged_df.empty:
        # Calculate percentiles for untagged records
        percentile_100 = untagged_df['commentLength'].quantile(1.0)
        percentile_66 = untagged_df['commentLength'].quantile(0.66)
        percentile_33 = untagged_df['commentLength'].quantile(0.33)
        percentile_0 = untagged_df['commentLength'].quantile(0.0)

        # Get records for each range for untagged data
        untagged_between_100_and_66 = untagged_df[(untagged_df['commentLength'] < percentile_100) & (untagged_df['commentLength'] >= percentile_66)].head(num_per_range)
        untagged_between_66_and_33 = untagged_df[(untagged_df['commentLength'] < percentile_66) & (untagged_df['commentLength'] >= percentile_33)].head(num_per_range)
        untagged_between_33_and_0 = untagged_df[(untagged_df['commentLength'] < percentile_33) & (untagged_df['commentLength'] >= percentile_0)].head(num_per_range)

        # Get random records from the untagged dataset
        untagged_random_items = untagged_df.sample(n=min(num_random, len(untagged_df)), random_state=42)

        # Combine the records for untagged data
        untagged_combined_df = pd.concat([untagged_between_100_and_66, untagged_between_66_and_33, untagged_between_33_and_0, untagged_random_items]).drop_duplicates(subset=['id', 'Text']).reset_index(drop=True)

        # Ensure the output directory exists
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)

        # Full path for the output CSV file
        output_file_path = os.path.join(output_dir, csv_file_name)

        # Write the combined DataFrame to the specified CSV file
        untagged_combined_df.to_csv(output_file_path, index=False, quoting=csv.QUOTE_ALL)

        print(f"Results for untagged records have been written to {output_file_path}")
    else:
        print("No untagged records found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query Cosmos DB for untagged records and select records based on comment length ranges.")
    parser.add_argument('csv_file_name', type=str, help="The output CSV file name (e.g., 'untagged_range_results.csv').")
    parser.add_argument('--num_per_range', type=int, default=60, help="Number of records to retrieve for each percentile range (default: 60).")
    parser.add_argument('--num_random', type=int, default=20, help="Number of random records to retrieve (default: 20).")
    
    args = parser.parse_args()
    
    # Pass the arguments to the main function
    main(args.csv_file_name, args.num_per_range, args.num_random)
