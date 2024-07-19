#-------------------------------Import Libraries-----------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import smartsheet
import streamlit as st

#CO5 WINTERSTEIGER NEW

##------------------------OIL------------------------------------

API_TOKEN  = "4jPmJP29lZilsAf60FllSXAeX4A0uR29MXaSc"
smartsheet_client = smartsheet.Smartsheet(API_TOKEN)

c05_oil = "4062998129758084"
sheet_oil = smartsheet_client.Sheets.get_sheet(c05_oil)

# Extract data and column names
columns_oil = [col.title for col in sheet_oil.columns]
data_oil = []

for row in sheet_oil.rows:
    row_data = {}
    for cell, col in zip(row.cells, columns_oil):
        row_data[col] = cell.value
    data_oil.append(row_data)

# Convert to DataFrame
df_oil = pd.DataFrame(data_oil)

df_oil = df_oil.dropna(subset = ['Measured Oil'])
df_oil["Date Created"] = pd.to_datetime(df_oil["Date Created"])
df_oil = df_oil.sort_values("Date Created")



##-------------------PROTEIN------------------------------
c05_protein = "6368329476296580"
sheet_protein = smartsheet_client.Sheets.get_sheet(c05_protein)

#print(sheet)
# Extract data and column names
columns_protein = [col.title for col in sheet_protein.columns]
data_protein = []

for row in sheet_protein.rows:
    row_data = {}
    for cell, col in zip(row.cells, columns_protein):
        row_data[col] = cell.value
    data_protein.append(row_data)

# Convert to DataFrame
df_protein = pd.DataFrame(data_protein)

df_protein['Measured Protein'] = df_protein['Measured Protein'].replace(['N/A', 'NA'], pd.NA)

# Filter out rows with NaN values in 'Measured Oil' column
df_protein = df_protein.dropna(subset=['Measured Protein'])
#df_protein = df_filtered[df_filtered['Date'].dt.year == 2024]

df_protein = df_protein[df_protein["Measured Protein"] > 35]

df_protein["Date Created"] = pd.to_datetime(df_protein["Date Created"])
df_protein = df_protein.sort_values("Date Created")

#########------------------------------OIL----------------
#print(df.head())
# Streamlit app title
st.title('Measured Oil Over Time')

# Display the DataFrame
st.write('### Data', df_oil)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df_oil['Date Created'], df_oil['Measured Oil'], marker='o', linestyle='-', color='g')


#mean
plt.axhline(y=19.028, color='black', linestyle='--', linewidth=1)
#2SD+
plt.axhline(y=19.605739, color='orange', linestyle='-.', linewidth=1)
#3SD+
plt.axhline(y=19.894609, color='r', linestyle='-.', linewidth=1)
#2SD-
plt.axhline(y=18.450261, color='orange', linestyle='-.', linewidth=1)
#3SD-
plt.axhline(y=18.161391, color='r', linestyle='-.', linewidth=1)


plt.title('Oil - C05 Wintersteiger [New]', fontsize = 16)
plt.xlabel('Date Analyzed', fontsize = 16)
plt.ylabel('Measured Oil', fontsize = 16)
plt.grid(False)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


##------------------------------PROTEIN-----------------------

#print(df.head())
# Streamlit app title
st.title('Measured Protein Over Time')

# Display the DataFrame
st.write('### Data', df_protein)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df_protein['Date Created'], df_protein['Measured Protein'], marker='o', linestyle='-', color='g')


#mean
plt.axhline(y=44.74867, color='black', linestyle='--', linewidth=1)
#2SD+
plt.axhline(y=45.69376, color='orange', linestyle='-.', linewidth=1)
#3SD+
plt.axhline(y=46.1663, color='r', linestyle='-.', linewidth=1)
#2SD-
plt.axhline(y=43.80358, color='orange', linestyle='-.', linewidth=1)
#3SD-
plt.axhline(y=43.33103, color='r', linestyle='-.', linewidth=1)


plt.title('Protein - C05 Wintersteiger [New]', fontsize = 16)
plt.xlabel('Date Analyzed', fontsize = 16)
plt.ylabel('Measured Protein', fontsize = 16)
plt.grid(False)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


##-------------------------------END-----------------------------------------
