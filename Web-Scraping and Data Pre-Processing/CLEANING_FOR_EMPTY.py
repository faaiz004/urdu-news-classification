import pandas as pd
import re

def remove_english_characters(text):
    if pd.isna(text):  
        return text
    return re.sub(r'[a-zA-Z]', '', text)


file_path = 'stop_cleaned_data.csv'  
df = pd.read_csv(file_path)


df['title'] = df['title'].apply(remove_english_characters)
df['content'] = df['content'].apply(remove_english_characters)
df = df.dropna(subset=['title', 'content'])
df = df[df['title'].str.strip() != '']
df = df[df['content'].str.strip() != '']


df.reset_index(drop=True, inplace=True)
df['id'] = df.index  

output_path = 'Batch_2.csv'
df.to_csv(output_path, index=False)

print(f"Processing complete. Cleaned data saved to {output_path}")
