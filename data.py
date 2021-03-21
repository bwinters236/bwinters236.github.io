import pandas as pd

# Reads csv
df = pd.read_csv('Resources/cities.csv')

# Save to html file
df.to_html('data.html', index=False)

# save html data in a variable
table = df.to_html()
print(table)