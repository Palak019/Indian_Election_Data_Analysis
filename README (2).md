
# 🇮🇳 Indian Election Data Analysis

## 📊 Project Overview

The **Indian Election Data Analysis** project aims to clean and visualize Indian election data to gain insights into voting trends, candidate demographics, party performance, and constituency characteristics over the years. This end-to-end analysis involves data preprocessing using Python and visualization using Tableau.

---

## 📁 Project Structure

```
indian_election_data_analysis/
│
├── Election_Data_Cleaning.py       # Python script to clean raw election data
├── Indian_Election_Dashboard.twb   # Tableau dashboard for data visualization
├── election_clean_data.csv         # Cleaned dataset generated from the script
├── Indian_election_dataset.csv     # (Assumed) Raw dataset used in preprocessing
└── README.md                       # Project documentation
```

---

## 🔧 Data Cleaning (Python)

**Script**: `Election_Data_Cleaning.py`

### Key Cleaning Steps:
- Loaded dataset: `Indian_election_dataset.csv`
- Removed unnecessary columns: `partyabbre`, `pc_name`, `pc_no`
- Renamed key columns for clarity:
  - `st_name` → `State`
  - `pc_type` → `Constituency_Type`
  - `cand_name` → `Candidate_Name`
  - `cand_sex` → `Candidate_Gender`
  - `totvotpoll` → `Votes_Polled`
- Removed duplicate records.
- Dropped rows with null values in essential columns: `State`, `year`, `Candidate_Name`, `partyname`, `Candidate_Gender`.
- Imputed missing values for:
  - `electors` and `Votes_Polled` with median values
  - `Constituency_Type` with `'Other'`
- Standardized column data types using `.astype()`.
- Replaced gender code `'F'` with `'Female'`.

**Output File**: `election_clean_data.csv`

---

## 📊 Data Visualization (Tableau)

**Dashboard File**: `Indian_Election_Dashboard.twb`

### Dashboard Highlights:

- **State-wise Voter Turnout**: A heatmap or bar chart showing total votes polled across states.
- **Party-wise Performance**: Visualization of the most successful political parties over the years.
- **Gender Representation**: Breakdown of male vs. female candidates per year or state.
- **Constituency Type Trends**: Comparison of general vs. reserved constituency participation.
- **Time Series Analysis**: Trend of voter turnout and candidate participation over multiple election years.

---

## 🚀 How to Run the Project

1. **Prepare Environment**:
   ```bash
   pip install pandas
   ```

2. **Clean the Data**:
   ```bash
   python Election_Data_Cleaning.py
   ```

3. **Visualize in Tableau**:
   - Open `Indian_Election_Dashboard.twb` in Tableau Desktop or Tableau Public.
   - Make sure `election_clean_data.csv` is in the same directory or update the data source path in Tableau.

---

## 🧠 Insights You Can Explore

- Which political party has been dominant over the years?
- Are there states with consistent voter engagement?
- How has gender participation in elections evolved?
- Do reserved constituencies show different trends compared to general ones?

---

## 🛠️ Tools Used

- **Python (Pandas)** – for data cleaning and preprocessing
- **Tableau** – for interactive visualizations
- **CSV** – for data storage and import/export

---

## 📌 Future Improvements

- Add predictive modeling for future elections using logistic regression or classification algorithms.
- Integrate more demographic or socioeconomic data for richer analysis.
- Develop a web dashboard using Plotly Dash or Streamlit for interactive public access.

---

## 📬 Contact

For questions or feedback, feel free to reach out.
