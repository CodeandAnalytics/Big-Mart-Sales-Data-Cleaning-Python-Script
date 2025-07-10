# Big-Mart-Sales-Data-Cleaning-Python-Script

Hello there!!

Welcome to my data-cleaning script – a small but powerful part of a bigger story.
This project began with one simple question:

    What’s hiding inside the messy sales data of a retail giant like Big Mart?"

As I opened the Excel file, I realized – like every real-world dataset – it had its share of problems:
❌ Missing values
❌ Zero entries that shouldn’t be zero
❌ Inconsistent labels
❌ And a few quirks that only a data lover could spot

📂 What's in This Project?
File: project_1.py
Purpose: Clean and prep the raw Big_mart.xlsx dataset into a well-structured .csv file you can actually work with.

What Does the Script Do?

🗂️ Step 1: Reading the Raw Data
I loaded the Excel sheet using pandas, setting the stage for transformation.


🕳️ Step 2: Filling the Gaps
🧪 Item Weights were missing?so, I filled them in using the median — a fair and robust estimate.

🏬 Outlet Size was unknown in some rows. I marked them as "NA" — better than pretending we know.

🚫 Step 3: Fixing the Oddities
- 0 Item Visibility? That’s just wrong — replaced those with the median again.
- Then I added a twist: labeled each product as "Low" or "High" visibility — making it human-readable.

🧹 Step 4: Tidying Up
- Rounded values in Item_MRP, Item_Outlet_Sales, and Item_Visibility for cleaner presentation.
- Standardized confusing entries in Item_Fat_Content. (Goodbye "LF" and "reg", hello "Low Fat" and "Regular")

🕵️‍♀️ Step 5: Duplicate Detection
I also checked for repeated Item_Identifier values — just to make sure we're not counting the same thing twice.

💾 Step 6: Saving the Clean Version
Finally, I exported the polished data to csv.

✨ Final Thoughts
This project may look simple, but it's the first building block in turning raw, chaotic data into meaningful insights.

Whether you're predicting sales or building a dashboard, clean data is your best friend.
