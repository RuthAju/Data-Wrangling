import pandas as pd

# To read csv file
df = pd.read_csv("Original Product_data.csv")

# To check if there are missing cells
# print(pd.isna(df))

# Drop all rows with missing cells
df.dropna(inplace= True)

# To check for duplicate rolls
# df1 = df.duplicated()

# To drop all duplicate rolls
df.drop_duplicates(inplace= True)

# Standardizing column name
Rename = {"PRODUCTID": "PRODUCT_ID", "PRODUCTTYPEID": "PRODUCT_TYPE_ID", "ProductLength": "PRODUCT_LENGTH"}
df.rename(columns= Rename, inplace=True)

# Round Product_Length to whole number and ensure a consistent format
if "PRODUCT_LENGTH" in df.columns:
    df["PRODUCT_LENGTH"] = df["PRODUCT_LENGTH"].apply(lambda x: str(round(float(x))))


# Clean and create short titles using lambda function
if "Title" in df.columns:
    redundant_words = {"includes", "set", "of", "features", "for", "with", "and", "|", "door", "window", "room", "fabric", "tie", "back", "canvas"}
    
    df["Short_Title"] = df["Title"].apply(lambda title: " ".join(
        word for word in title.split() if word.lower() not in redundant_words)[:50].strip()
    )

df.to_csv("Modified Product_data.csv", index= False)
print("Cleaned CSV file saved as Modified Product_data.csv")


