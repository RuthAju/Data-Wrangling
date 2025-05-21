import pandas as pd
import os

os.chdir(r"C:\Users\USER\Desktop\E-Commerce")
df = pd.read_csv("submissions.csv")
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
df.to_csv("Cleaned_submissions.csv", index=False)
print("Check E-commerce folder for the cleaned csv file")