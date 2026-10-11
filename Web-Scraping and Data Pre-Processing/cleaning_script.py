import pandas as pd

cleaned_data_path = 'Batch_2.csv' 
stopwords_path = 'stopwords-ur.txt' 

# Load the cleaned data
df_cleaned = pd.read_csv(cleaned_data_path)

with open(stopwords_path, 'r', encoding='utf-8') as f:
    stopwords = set(f.read().splitlines())

def remove_stopwords(text):
    words = text.split()
    cleaned_text = ' '.join(word for word in words if word not in stopwords)
    return cleaned_text

df_cleaned['content'] = df_cleaned['content'].apply(remove_stopwords)
df_cleaned['title'] = df_cleaned['title'].apply(remove_stopwords)

final_cleaned_path = 'final_dataset.csv'  
df_cleaned.to_csv(final_cleaned_path, index=False)

print("Final cleaned dataset saved to:", final_cleaned_path)