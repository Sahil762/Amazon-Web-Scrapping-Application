import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel('amazon_shoes_data.xlsx')


print(df.head())


def parse_price(price):
    try:
        return float(price.replace('₹', '').replace(',', '').strip())
    except ValueError:
        return None

df['Price'] = df['Price'].apply(parse_price)


df = df.dropna(subset=['Price'])


plt.figure(figsize=(12, 6))
sns.histplot(df['Price'], bins=20, kde=True)
plt.title('Distribution of Shoe Prices')
plt.xlabel('Price (INR)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


plt.figure(figsize=(12, 6))
sns.boxplot(x=df['Price'])
plt.title('Boxplot of Shoe Prices')
plt.xlabel('Price (INR)')
plt.grid(True)
plt.show()

