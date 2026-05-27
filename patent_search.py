import pandas as pd

# Load patent metadata
metadata_df:pd.DataFrame = pd.read_parquet("/kaggle/input/uspto-explainable-ai/patent_metadata.parquet")
# >>> len(metadata_df.index)
# >>> 13307751
# This Process takes quite long.




# Define function for publication search
def search_publication(publication_number: str) -> pd.DataFrame:
    publication_info = metadata_df[metadata_df["publication_number"] == publication_number]
    if not publication_info.empty:
        return publication_info
    else:
        print(f"Publication not found for {publication_number}")
        null_data = {
            'publication_number': [None],
            'publication_date': [None],
            'filing_date': [None],
            'family_id': [None],
            'cpc_codes': [None]
        }
        null_df = pd.DataFrame(null_data)
        return null_df





# Example search
publication_number1 = "US-2017082634-A1"
publication_number2 = "US-2022408153-A1"


result1 = search_publication(publication_number1)
result2 = search_publication(publication_number2)

print("Result for", publication_number1)
print(result1)

print("\nResult for", publication_number2)
print(result2)


# >>> print(metadata_df.columns)
# >>> Index(['publication_number', 'publication_date', 
# >>> 'filing_date', 'family_id',
# >>> 'cpc_codes'], dtype='object')