{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "439bc7bc-4203-4a57-91ec-060ed52bd615",
   "metadata": {},
   "source": [
    "# E-commerce Sales Analysis\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "163ff87a-790d-4664-ae32-6c4ae71d5fdd",
   "metadata": {},
   "source": [
    "## Project Overview\r\n",
    "This project analyzes sales data from an e-commerce platform to uncover insights into product performance, category trends, and pricing strategies. The goal is to provide actionable recommendations to optimize revenue and inventory management. The dataset, containing 100 sales transactions, includes product details, quantities, prices, and total sales."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c06aa2b-b0e1-4aa2-aaec-3d084ff3eaf3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Importing required libraries\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b8d8b959-3cf1-4633-ac7e-16ecc0b9e99f",
   "metadata": {},
   "source": [
    "### Dataset Overview\n",
    "This dataset contains 100 records of sales transactions from an e-commerce platform. The columns include:\n",
    "\n",
    "- Order_ID: Unique identifier for each order.\n",
    "- Product: Name of the product sold.\n",
    "- Category: Category of the product.\n",
    "- Quantity: Quantity of the product sold.\n",
    "- Price_per_Unit: Price of one unit of the product.\n",
    "- Total_Sale: Total sale amount for the product.\r\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ccf18e57-75c6-42c3-9fb4-46884974863f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Loading dataset\n",
    "df = pd.read_csv('../data/ecommerce_sales.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63be7550-37d6-41c4-8c36-308e0b714e91",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Initial preview of data\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e20bbc38-6ae3-40a5-bc12-65fed2d7bd13",
   "metadata": {},
   "source": [
    "## Data Cleaning "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a0578e46-a6b4-42c1-98b9-ecb795fb9a81",
   "metadata": {},
   "source": [
    "#### This section focuses on cleaning the data by removing duplicates, handling missing values, and correcting incorrect formats. The aim is to ensure the dataset is accurate and ready for analysis..\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3bd3463d-2dda-4abc-a45a-00e7f2649a7b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Knowing the data\n",
    "df.info()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63368fb6-1b28-4c11-985d-a7c5e063e6ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Summary statistics of the DataFrame\n",
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "72065f0e-c9da-4530-bd34-8d830da56e6b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Checking for missing values\n",
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "68885b49-0e7a-4b0b-b69e-87fd3a097e0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Checking for and dropping duplicates\n",
    "df.duplicated().sum()\n",
    "df = df.drop_duplicates()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5817e651-91fd-47ac-89ed-eaee9234f993",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Checking for negative quantities and removing them\n",
    "df = df[df['Quantity'] > 0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "45f8e925-74f5-47e7-98d9-d06ec5b97b67",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Ensuring numeric columns are correctly typed\n",
    "df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')\n",
    "df['Price_per_Unit'] = pd.to_numeric(df['Price_per_Unit'], errors='coerce')\n",
    "df['Total_Sale'] = pd.to_numeric(df['Total_Sale'], errors='coerce')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a889590a-a020-4764-8908-636352f5afbd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dropping rows that failed to convert\n",
    "df = df.dropna(subset=['Quantity', 'Price_per_Unit', 'Total_Sale'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ac018254-127c-4644-a632-947c72ee6fde",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Verifying Total_Sale calculation\n",
    "df['Calculated_Total'] = df['Quantity'] * df['Price_per_Unit']\n",
    "discrepancies = df[df['Total_Sale'] != df['Calculated_Total']]\n",
    "if discrepancies.empty:\n",
    "    print(\"All Total_Sale values are correct.\")\n",
    "else:\n",
    "    print(\"Found discrepancies in Total_Sale:\")\n",
    "    print(discrepancies[['Order_ID', 'Quantity', 'Price_per_Unit', 'Total_Sale', 'Calculated_Total']])\n",
    "df = df.drop(columns=['Calculated_Total'])\n",
    "\n",
    "print(f\"Number of duplicates removed: {100 - len(df)}\")\n",
    "print(f\"Number of rows with negative quantities removed: {100 - len(df[df['Quantity'] > 0])}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b5be0dec-08f3-47be-99fc-e9ddb4cbace1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Final check\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "76134aff-d7aa-4e7f-9054-9a18a37e3b83",
   "metadata": {},
   "source": [
    "## Exploratory Data Analysis"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fb0ceb1d-3845-48a6-aa98-865ac9556a0b",
   "metadata": {},
   "source": [
    "#### This section explores key performance metrics from the e-commerce dataset, focusing on sales volume, revenue, and pricing across products and categories. The goal is to identify top performers, popular products, and pricing trends.\r\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c4ce8005-7e30-4a06-93e9-0e1b2ffe4e0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Identifying which products have generated the most revenue overall.\n",
    "product_revenue = df.groupby('Product')['Total_Sale'].sum().sort_values(ascending=False)\n",
    "product_revenue.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "32ffe72c-9488-49f8-83f7-9c2f31616ee2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Identifying which product categories contribute most to the business's total revenue.\n",
    "category_revenue = df.groupby('Category')['Total_Sale'].sum().sort_values(ascending=False)\n",
    "category_revenue"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d195a2e-96bf-4f35-ac41-397e8878fddc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Identifying which products are purchased most frequently, regardless of their price?\n",
    "top_quantity = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)\n",
    "top_quantity.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "98d7a85c-0fb2-456e-9599-dc100e631ddf",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Understanding the pricing levels across different categories.\n",
    "avg_price = df.groupby('Category')['Price_per_Unit'].mean().sort_values(ascending=False)\n",
    "avg_price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c381567d-9bc1-4721-a281-d488b0aa7f19",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Finding revenue per order\n",
    "order_revenue = df.groupby('Order_ID')['Total_Sale'].sum().sort_values(ascending=False)\n",
    "order_revenue.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "995905a9-5fd1-41f3-bbde-4088037fd1c2",
   "metadata": {},
   "source": [
    "## Visualizations"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a7bdb49f-9d15-4e45-9bd3-d7ecd248585f",
   "metadata": {},
   "source": [
    "#### This section presents key visualizations from the e-commerce dataset, highlighting sales trends, product performance, and category-wise revenue distribution. The goal is to provide clear insights into product popularity, sales patterns, and pricing strategies."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2bc23c84-f0d0-43f8-b1c4-755a37efe528",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visualizing the products by revenue to identify the highest-performing products\n",
    "plt.figure(figsize=(8, 4)) \n",
    "sns.barplot(x=product_revenue.values, y=product_revenue.index, hue=product_revenue.index, palette='viridis', legend=False)\n",
    "plt.title('Total Revenue by Product', fontsize=12, weight='bold')\n",
    "plt.xlabel('Total Revenue ($)', fontsize=10)\n",
    "plt.ylabel('Product', fontsize=10)\n",
    "plt.grid(axis='x', linestyle='--', alpha=0.7)\n",
    "plt.tight_layout()\n",
    "plt.savefig('../visuals/top_products_by_revenue.png')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bb675d52-d7c3-4ff8-8e48-8e0a601c96ef",
   "metadata": {},
   "source": [
    "###### This bar chart shows which products generate the most revenue. Laptops lead, followed by Headphones, Tablets, and Smartphones. This suggests Laptops are a key driver of sales."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "413558c4-977a-4243-897e-805ed0a908f1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visualizing revenue distribution across different categories to understand category-wise performance\n",
    "plt.figure(figsize=(6, 4))\n",
    "sns.barplot(x=category_revenue.values, y=category_revenue.index, hue=category_revenue.index, palette='magma', legend=False)\n",
    "plt.title('Total Revenue by Category', fontsize=12, weight='bold')\n",
    "plt.xlabel('Total Revenue ($)', fontsize=10)\n",
    "plt.ylabel('Category', fontsize=10)\n",
    "plt.grid(axis='x', linestyle='--', alpha=0.7)\n",
    "plt.tight_layout()\n",
    "plt.savefig('../visuals/revenue_distribution_by_category.png')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8e844af2-3016-4c02-bd2d-2823e66f2e7e",
   "metadata": {},
   "source": [
    "###### This bar chart shows revenue by category. Electronics slightly outperforms Accessories, but both are important for the business."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2c9c0efb-833c-4356-b30f-96389b3b78a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visualizing the top products by quantity sold to identify the most popular products\n",
    "plt.figure(figsize=(8, 4))\n",
    "sns.barplot(x=top_quantity.values, y=top_quantity.index, hue=top_quantity.index, palette='crest', legend=False)\n",
    "plt.title('Total Quantity Sold by Product', fontsize=12, weight='bold')\n",
    "plt.xlabel('Total Quantity Sold', fontsize=10)\n",
    "plt.ylabel('Product', fontsize=10)\n",
    "plt.grid(axis='x', linestyle='--', alpha=0.7)\n",
    "plt.tight_layout()\n",
    "plt.savefig('../visuals/top_products_by_quantity_sold.png')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e3150d89-3a31-4beb-8e40-4da48a215feb",
   "metadata": {},
   "source": [
    "###### This bar chart shows how many units of each product were sold. Laptops are the most popular, followed by Headphones, Tablets, and Smartphones. This means customers buy Laptops the most."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "59ccf055-605c-4083-90d6-449b5fa17374",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visualizing the average price per unit across different categories to understand pricing trends\n",
    "plt.figure(figsize=(6, 4))  \n",
    "sns.barplot(x=avg_price.values, y=avg_price.index, hue=avg_price.index, palette='rocket', legend=False)  \n",
    "plt.title('Average Price per Unit by Category', fontsize=12, weight='bold')  \n",
    "plt.xlabel('Average Price per Unit ($)', fontsize=10)  \n",
    "plt.ylabel('Category', fontsize=10)  \n",
    "plt.grid(axis='x', linestyle='--', alpha=0.7)  \n",
    "plt.tight_layout()  \n",
    "plt.savefig('../visuals/average_price_per_unit_by_category.png')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c280d3d0-8812-41db-996b-049f6cd2dbee",
   "metadata": {},
   "source": [
    "###### This bar chart shows the average price of products in each category. Electronics products are a little more expensive than Accessories. This might explain why Electronics make a bit more money."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1ce8a94a-add9-4a2a-9672-7653b8b450bc",
   "metadata": {},
   "source": [
    "## Summary and Recommendations\n",
    "\n",
    "This analysis of e-commerce sales data reveals key insights:\n",
    "\n",
    "*Top Products: Laptops generate the most revenue (AUD 162,098) and are the most popular (150 units sold), making them a flagship product.\n",
    "\n",
    "*Category Performance: Electronics (AUD 258,523) and Accessories (AUD 253,860) contribute nearly equally to revenue, with Electronics slightly ahead due to higher average prices (AUD 1070.86) compared to Accessories (AUD 1019.24).\n",
    "\n",
    "*Pricing Trends: Electronics products are priced slightly higher, which boosts their revenue despite similar sales volumes to Accessories.\n",
    "\n",
    "### Recommendations\n",
    "\n",
    "*Promote Laptops: Increase marketing for Laptops, as they drive both revenue and popularity.\n",
    "\n",
    "*Balance Inventory: Maintain stock for both Electronics and Accessories, as both are critical to sales.\n",
    "\n",
    "*Price Optimization: Consider slight price adjustments for Accessories to boost their revenue, given their strong sales volume.\n",
    "\n",
    "These strategies can help the business maximize revenue and customer satisfaction.s)."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "19a96905-09a5-4044-9bb4-2c75990e50bd",
   "metadata": {},
   "source": [
    "### Limitations and Future Work\n",
    "\n",
    "*Small Dataset: The dataset contains only 100 records, limiting the generalizability of insights.\n",
    "\n",
    "*Lack of Temporal Data: Without timestamps, trends over time (e.g., seasonality) cannot be analyzed.\n",
    "\n",
    "*Future Work: Incorporate customer demographics or time-series data to refine recommendations and explore predictive modeling (e.g., forecasting sales)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7c3e78d0-eae9-4ad0-9176-90407cfa1aa3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
