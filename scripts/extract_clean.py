import pandas as pd
print('Pipeline started...')
data = {'name': ['Jazzy', 'Tobi', 'Sola'], 'score': [90, 85, None]}
df = pd.DataFrame(data)
print('Raw:')
print(df)
df['score'] = df['score'].fillna(0)
print('Cleaned:')
print(df)
df.to_csv('data/processed/cleaned.csv', index=False)
print('Saved to data/processed/cleaned.csv - Done!')
