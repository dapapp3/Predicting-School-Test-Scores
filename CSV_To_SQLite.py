import sqlite3
import pandas as pd

# Load CSV
df = pd.read_csv('/content/exams.csv')

# Create db
conn = sqlite3.connect('/content/exams.db')

# Load data to db
df.to_sql('exams', conn, if_exists='replace', index=False)

# Close connection
conn.close()