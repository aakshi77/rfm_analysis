# %%
# CELL 1: IMPORT LIBRARIES AND LOAD DATA
# =================================================================
# This cell imports the necessary libraries and loads your dataset into a pandas DataFrame.

import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from the Excel file in the same folder
print("Step 1: Loading data...")
df = pd.read_excel('Online Retail.xlsx')
print("Data loaded successfully!")
print("\nFirst 5 rows of the dataset:")
print(df.head())


# %%
# CELL 2: DATA CLEANING AND PREPARATION
# =================================================================
# Real-world data is messy. This cell cleans it up for analysis.

print("\nStep 2: Cleaning data...")
# Remove transactions without a CustomerID
df.dropna(subset=['CustomerID'], inplace=True)

# Ensure CustomerID is an integer
df['CustomerID'] = df['CustomerID'].astype(int)

# Remove any duplicate transaction rows
df.drop_duplicates(inplace=True)

# Filter out canceled orders (InvoiceNo starts with 'C') and returns (negative Quantity)
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
df = df[df['Quantity'] > 0]

# Create a 'TotalPrice' column for our Monetary calculation
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
print("Data cleaning complete.")


# %%
# CELL 3: CALCULATE RFM VALUES
# =================================================================
# This is the core of RFM. We calculate Recency, Frequency, and Monetary value for each customer.

print("\nStep 3: Calculating RFM values...")
# Set a 'snapshot_date' to calculate recency from. We'll use the day after the last transaction.
snapshot_date = df['InvoiceDate'].max() + dt.timedelta(days=1)

# Group by each customer and calculate RFM values
rfm_data = df.groupby('CustomerID').agg({
    # Recency: How many days ago was their last purchase?
    'InvoiceDate': lambda date: (snapshot_date - date.max()).days,
    # Frequency: How many unique purchases have they made?
    'InvoiceNo': 'nunique',
    # Monetary: What is their total spending?
    'TotalPrice': 'sum'
})

# Rename the columns to be more descriptive
rfm_data.rename(columns={'InvoiceDate': 'Recency',
                         'InvoiceNo': 'Frequency',
                         'TotalPrice': 'MonetaryValue'}, inplace=True)

print("RFM values calculated. Here's a sample:")
print(rfm_data.head())


# %%
# =============================================================================
# 4. CREATE RFM SCORES
# =============================================================================
print("\nScoring RFM values...")

# We will score each customer from 1 to 5 for each metric.
r_labels = range(5, 0, -1)
f_labels = range(1, 6)
m_labels = range(1, 6)

# Use rank(method='first') to handle ties in the data, which prevents the ValueError
# This ensures that even if many customers have the same value, they get a unique rank
rfm_data['R_Score'] = pd.qcut(rfm_data['Recency'].rank(
    method='first'), q=5, labels=r_labels).astype(int)
rfm_data['F_Score'] = pd.qcut(rfm_data['Frequency'].rank(
    method='first'), q=5, labels=f_labels).astype(int)
rfm_data['M_Score'] = pd.qcut(rfm_data['MonetaryValue'].rank(
    method='first'), q=5, labels=m_labels).astype(int)

print("RFM scores assigned. Here's a sample with scores:")
print(rfm_data.head())

# %%
# CELL 5: SEGMENT CUSTOMERS
# =================================================================
# Now we combine the scores to create meaningful customer segments.

print("\nStep 5: Segmenting customers...")
# Combine R and F scores into a string to easily map to segments
rfm_data['Segment'] = rfm_data['R_Score'].astype(
    str) + rfm_data['F_Score'].astype(str)

# Define segment names based on R and F score combinations
# Define segments based on R and F scores
# This dictionary uses regex to match R and F score combinations to a segment name
segment_map = {
    r'[1-2][1-2]': 'Hibernating',
    r'[1-2][3-4]': 'At Risk',
    r'[1-2]5': 'Can\'t Lose Them',
    r'3[1-2]': 'About to Sleep',
    r'33': 'Need Attention',
    r'[3-4][4-5]': 'Loyal Customers',
    r'41': 'Promising',  # A more specific name for R=4, F=1
    r'51': 'New Customers',
    # This new rule now covers 42, 43, 52, and 53
    r'[4-5][2-3]': 'Potential Loyalists',
    r'5[4-5]': 'Champions'
}

# Apply the mapping to create the final 'Segment' column
rfm_data['Segment'] = rfm_data['Segment'].replace(segment_map, regex=True)
print("Customer segmentation complete.")
print("\nFinal data with segments:")
print(rfm_data.head())


# %%
# CELL 6: ANALYZE AND VISUALIZE THE SEGMENTS
# =================================================================
# The final step is to analyze the segments and create a visual report.

print("\nStep 6: Analyzing and visualizing segments...")
# Calculate the size and average value of each segment
segment_summary = rfm_data.groupby('Segment').agg(
    Customer_Count=('MonetaryValue', 'count'),
    Avg_Monetary_Value=('MonetaryValue', 'mean')
).round(1).sort_values(by='Customer_Count', ascending=False)

print("\nSegment Summary:")
print(segment_summary)

# Create a bar plot to visualize the number of customers in each segment
plt.figure(figsize=(12, 8))
sns.countplot(y='Segment', data=rfm_data,
              order=rfm_data['Segment'].value_counts().index, palette='viridis')
plt.title('Distribution of Customer Segments', fontsize=16)
plt.xlabel('Number of Customers', fontsize=12)
plt.ylabel('Segment', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

print("\nAnalysis complete!")

# %%
