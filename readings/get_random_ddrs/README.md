# Get a curated random set of data

The scope of this spike is to gather a set of data with curated tags that can serve as a baseline.
The dataset should cover all available categories and it has to be as randomly distributed as possible.
Data is now extracted from the `WellboreData` container in the database, more specifically the `comment`, `phase`, `operation.SubCode` fields.

## Decisions taken for this spike

- Data is initially extracted from DDRs.
- Both scenarios are considered: when tags are present and when they are absent (i.e., an empty array).
- Data is collected from all categories.
- Records are split into percentiles based on comment length. We randomly select data from three different percentiles (0 to 33, 33 to 66, and 66 to 100). Additionally, several other randomly chosen records are included.
- The data is then sent for curation with the following questions:
  - For tagged records, validate whether the tags are correct, and if they aren't, specify the correct tags.
  - For untagged records, validate whether tags should indeed be absent, and if not, specify the appropriate tags. This will help ensure that the model doesn't mistakenly assign tags in the future.

## Spike results

- 18 tags have been identified, and we extracted 1265 records with tags, and 200 records without tags for review.

## Follow-up items

- Get a baseline for records that are not `ddr's`.
- Get the curated information for these records.

## Running the spike

To run the script, you must follow the steps:

- Create an `.env` file using the [example](./.env.example) provided.
- Make sure you have access to the CosmosDB database and add your IP to the [firewall](https://learn.microsoft.com/azure/cosmos-db/how-to-configure-firewall#requests-from-your-current-ip).
- Create and activate a python [environment](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments)

```sh
python -m venv venv
```

```sh
.\venv\Scripts\Activate.ps1
```

- Install the [requirements](./requirements.txt)

```sh
pip install -r requirements.txt
```

> Note: Outputs are saved in an output folder

- Run the [script](./extract_random_distributed_data_with_tags.py) to get a sample of records with tags.

```sh
python.exe .\extract_random_distributed_data_with_tags.py randomly_distributed_data_with_tags.csv
```

The script outputs the location of the output csv file.
The output CSV file should contain the following fields for DDR records: "id", "Text", "phase", "code", "subCode", "commentLength", "label", "tags", and "auto tags". All categories ("shallowwater", "shallowgas", "holecleaning", "dheqfailure","wellborebreathing", "highrop", "boulders", "surfeqfailure","dircontrol", "stuckpipe", "wellcontrol", "harddrilling","wellborestability", "packoff", "tighthole", "lowrop", "lostcirculation", "wait") must be represented, with the comment lengths distributed randomly in each category.

- Run the [script](./extract_random_distributed_data_without_tags.py) to get a sample of records without tags.

```sh
python.exe .\extract_random_distributed_data_without_tags.py randomly_distributed_data_without_tags.csv
```

The script outputs the location of the output csv file.
The output CSV file should contain the following fields for DDR records: "id", "Text", "phase", "code", "subCode", "commentLength", "label", "tags", and "auto tags". Text lengths should be distributed randomly.
