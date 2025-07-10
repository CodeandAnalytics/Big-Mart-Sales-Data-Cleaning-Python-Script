# Big-Mart-Sales-Data-Cleaning-Python-Script


Welcome to the real-world data cleaning using Python and pandas.  
This is where I learned that **raw data is just the beginning**, and how powerful even a few lines of cleaning code can be in making messy Excel files analysis-ready.

---

## 📦 Project Summary

- **📁 File:** `project_1.py`  
- **📊 Dataset:** `Big_mart.xlsx` (Retail sales data)  
- **🎯 Goal:** Clean and prepare the raw data for further analysis or machine learning  

---

## 🧠 The Data Cleaning Journey (Step by Step)

### 📥 1. Reading the Raw Data

- I loaded the Excel sheet using pandas, setting the stage for transformation.

  🕳️ Step 2: Filling the Gaps
  
- Item Weights were missing so, I filled them in using the median — a fair and robust estimate.
- Outlet Size was unknown in some rows. I marked them as "NA" — better than pretending we know.


🔁 3. Fix Invalid and Inconsistent Values
- Replaced 0s in Item_Visibility with its median
- Categorized Item_Visibility into "Low" and "High" for readability
- Standardized values in Item_Fat_Content like "LF" → "Low Fat", "reg" → "Regular"


🧹 Step 4: Round Off Numeric Columns

- Rounded values in Item_MRP, Item_Outlet_Sales, and Item_Visibility for cleaner presentation.



💾 Step 5: Saving the Clean Version

- Saved the final cleaned data into a new CSV file you can now use for modeling, analysis, or dashboard building.




