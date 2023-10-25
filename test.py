# Import Pandas
import pandas as pd

# Import tabulate just for better view :))
from tabulate import tabulate

# Load Movies Metadata
metadata = pd.read_csv('movies_metadata.csv',low_memory=False)

# Print the first three rows

C = metadata['vote_average'].mean()
print(C)