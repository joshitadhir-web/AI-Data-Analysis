# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load Excel file
df = pd.read_excel(r"C:/Users/Joshita Goonj Dhir/OneDrive/Desktop/RESEARCH PAPER/final_doc.xlsx")

# Step 2: Rename columns for consistency
df.rename(columns={
    'MONTH': 'Date',
    'AVERAGE CALL RATE': 'CallRate',
    'USD/INR EXCHANGE RATE': 'USDINR',
    'GOLD PRICING ( per 10 grams)': 'GoldPrice'
}, inplace=True)

# Step 3: Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Step 4: Ensure numeric values (fix anomalies like "117475..90")
df['GoldPrice'] = pd.to_numeric(df['GoldPrice'], errors='coerce')
df['USDINR'] = pd.to_numeric(df['USDINR'], errors='coerce')
df['CallRate'] = pd.to_numeric(df['CallRate'], errors='coerce')

# Step 5: Drop rows with missing values in key columns
df = df.dropna(subset=['Date', 'GoldPrice', 'USDINR', 'CallRate'])

# Step 6: Generate descriptive statistics
print("Summary Statistics:")
print(df.describe())

# Step 7: Plot Gold Prices
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['GoldPrice'], color='gold')
plt.title("Gold Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Gold Price (per 10 grams)")
plt.grid(True)
plt.show()

# Step 8: Plot USD/INR Exchange Rate
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['USDINR'], color='blue')
plt.title("USD/INR Exchange Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Exchange Rate")
plt.grid(True)
plt.show()

# Step 9: Plot Average Call Rate
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['CallRate'], color='green')
plt.title("Average Call Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Call Rate (%)")
plt.grid(True)
plt.show()

# Step 10: Normalize values for comparability (index to 100 at first valid value)
df['Gold_norm'] = df['GoldPrice'] / df['GoldPrice'].iloc[0] * 100
df['USDINR_norm'] = df['USDINR'] / df['USDINR'].iloc[0] * 100
df['CallRate_norm'] = df['CallRate'] / df['CallRate'].iloc[0] * 100

# --- Plot all three normalized together ---
plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Gold_norm'], color='gold', label='Gold Price (Indexed)')
plt.plot(df['Date'], df['USDINR_norm'], color='blue', label='USD/INR (Indexed)')
plt.plot(df['Date'], df['CallRate_norm'], color='green', label='Call Rate (Indexed)')
plt.title("Normalized Comparison of Gold Price, USD/INR, and Call Rate")
plt.xlabel("Date")
plt.ylabel("Index (Base = 100)")
plt.legend()
plt.grid(True)
plt.show()

# --- Plot Gold vs USD/INR normalized ---
plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Gold_norm'], color='gold', label='Gold Price (Indexed)')
plt.plot(df['Date'], df['USDINR_norm'], color='blue', label='USD/INR (Indexed)')
plt.title("Gold Price vs USD/INR (Normalized)")
plt.xlabel("Date")
plt.ylabel("Index (Base = 100)")
plt.legend()
plt.grid(True)
plt.show()

# --- Plot Gold vs Call Rate normalized ---
plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Gold_norm'], color='gold', label='Gold Price (Indexed)')
plt.plot(df['Date'], df['CallRate_norm'], color='green', label='Call Rate (Indexed)')
plt.title("Gold Price vs Call Rate (Normalized)")
plt.xlabel("Date")
plt.ylabel("Index (Base = 100)")
plt.legend()
plt.grid(True)
plt.show()

# --- Plot USD/INR vs Call Rate normalized ---
plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['USDINR_norm'], color='blue', label='USD/INR (Indexed)')
plt.plot(df['Date'], df['CallRate_norm'], color='green', label='Call Rate (Indexed)')
plt.title("USD/INR vs Call Rate (Normalized)")
plt.xlabel("Date")
plt.ylabel("Index (Base = 100)")
plt.legend()
plt.grid(True)
plt.show()


# Step 11: Create Prompt Template for AI Explanation
prompt = f"""
You are a financial analyst.
Explain the trends in this dataset step by step:
Call Rate Summary: {df['CallRate'].describe()}
USD/INR Summary: {df['USDINR'].describe()}
Gold Price Summary: {df['GoldPrice'].describe()}
"""
print("\nGenerated Prompt for AI:\n")
print(prompt)
