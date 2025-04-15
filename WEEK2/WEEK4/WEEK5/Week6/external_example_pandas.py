import pandas as pd

jsMammies = {
    'Name': ['Everlyne', 'Annie', 'Martha'],
    'Age': [24, 30, 22],
    'height': [5.4, 5.6, 5.5],
    'Score': [85, 90, 95]
}

girlfriends_table = pd.DataFrame(jsMammies)
# print("DataFrame:\n", df)

# print("Names:", df['Age'])
print(girlfriends_table)