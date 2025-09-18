# RFM Customer Segmentation for Strategic Marketing 🛍️

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-1.5-blue?style=for-the-badge&logo=pandas)
![Seaborn](https://img.shields.io/badge/Seaborn-0.12-blue?style=for-the-badge&logo=seaborn)

## 1. Project Overview

This project presents an end-to-end data analysis of transactional data to segment customers based on their purchasing behavior. Using the RFM (Recency, Frequency, Monetary) model, this analysis transforms raw sales data into actionable business insights, enabling a more targeted and effective marketing approach.

---

## 2. Business Objective

The primary goal of this project is to move away from a "one-size-fits-all" marketing strategy. By identifying distinct customer groups, the business can:
* ✅ Identify the most valuable customers (**Champions**).
* ✅ Recognize customers at risk of churning (**At Risk**).
* ✅ Nurture **New Customers** to increase their lifetime value.
* ✅ Optimize marketing spend by focusing on high-potential segments.

---

## 3. Key Findings & Visualization

The analysis successfully grouped customers into nine distinct segments. The distribution below shows that while **Hibernating** customers form the largest group by count, a smaller group of **Champions** and **Loyal Customers** are the most critical for the business's revenue.


*(To add your image, upload it to your GitHub repo and replace the tag above with `![Chart](filename.png)`)*

### Key Insights:
* **High-Value Concentration**: A minority of customers in the 'Champions' and 'Loyal Customers' segments drive a majority of the revenue.
* **Significant Churn Risk**: A substantial group of previously valuable customers are now 'At Risk', requiring immediate attention to prevent churn.
* **Growth Opportunity**: The 'New Customers' and 'Potential Loyalists' segments represent a key opportunity for future growth if nurtured correctly.

---

## 4. Actionable Recommendations

Based on the segments identified, the following targeted strategies are recommended:

| Segment | Recommendation | Business Goal |
| :--- | :--- | :--- |
| 🏆 **Champions** | Reward with loyalty programs, exclusive access, and solicit reviews. | **Retain & Advocate** |
| ❤️ **Loyal Customers** | Engage with upselling opportunities and loyalty programs. | **Upsell & Retain** |
| 😟 **At Risk** | Launch personalized win-back campaigns with special offers. | **Reactivate & Prevent Churn** |
| 🌱 **New Customers** | Provide a smooth onboarding experience and an incentive for a second purchase. | **Convert & Nurture** |
| 💤 **Hibernating** | Send a final, low-cost promotional offer before reducing marketing spend. | **Win-back or Archive** |

---

## 5. Methodology

The analysis was conducted in the following steps:
1.  **Data Cleaning**: Handled missing `CustomerID`s, removed duplicate transactions, and filtered out canceled orders/returns.
2.  **Feature Engineering**: Created a `TotalPrice` column from `Quantity` and `UnitPrice`.
3.  **RFM Calculation**: For each customer, calculated **Recency** (days since last purchase), **Frequency** (total unique purchases), and **Monetary** (total spend).
4.  **Scoring & Segmentation**: Scored each RFM metric on a 1-5 scale using quintiles. Resolved `ValueError` from non-unique bin edges by using `.rank(method='first')`. Customers were then grouped into named segments based on their R and F scores.

---

## 6. Technical Stack

* **Language**: Python
* **Libraries**:
    * **Pandas**: For data cleaning, manipulation, and analysis.
    * **Matplotlib & Seaborn**: For data visualization.
* **Environment**: VS Code with Jupyter extension

---

## 7. How to Run This Project

To replicate this analysis, please follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)[YourUsername]/[YourRepoName].git
    cd [YourRepoName]
    ```

2.  **Install the required libraries:**
    *It is recommended to create a virtual environment first.*
    ```bash
    pip install -r requirements.txt
    ```
    *(To create the `requirements.txt` file, run `pip freeze > requirements.txt` in your terminal)*

3.  **Add the dataset:**
    Download the dataset from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/online+retail) and place the `Online Retail.xlsx` file in the project's root directory.

4.  **Run the analysis:**
    Open the `rfm_analysis.py` file in VS Code and run the cells sequentially.

---

## 8. Author

* **[Your Name]**
* **LinkedIn**: [Link to your LinkedIn profile]
* **GitHub**: [Link to your GitHub profile]
