import pandas as pd

sales = pd.read_csv("sales.csv", encoding = "latin-1")
products = pd.read_csv("products.csv", encoding = "latin-1")

file = pd.merge(sales, products, left_on = "product_id", right_on = "Product_ID", how = "left")

file.to_csv("Updated Apple Sales and Product File.csv", index = False)


print(file.head())


Updated_File = pd.read_csv("Updated Apple Sales and Product File.csv", encoding = "latin-1")

new_Updated_File = Updated_File.dropna()

Updated_File_duplicates = new_Updated_File.drop_duplicates()

Top_products = Updated_File.groupby("Product_Name")["quantity"].sum()

Top_product = Top_products.sort_values(ascending=False)

print(Updated_File_duplicates)
print(Top_product)
