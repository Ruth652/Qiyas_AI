# Qiyas AI - Data Science & Machine Learning Repository

A structured learning repository covering Python fundamentals, data manipulation, exploratory data analysis (EDA), and end-to-end Machine Learning workflows.

---

## 📁 Repository Structure

```text
Qiyas_AI/
│
├── .gitignore                  # Git ignore rules for environments, cache & checkpoints
├── requirements.txt            # Python dependencies
├── README.md                   # Repository documentation
│
├── Qiyas-learning-path/        # Main Machine Learning curriculum & projects
│   ├── data/                   # Datasets used in notebooks
│   │   └── Mall_Customers.csv
│   └── notebooks/              # Interactive Jupyter Notebooks (.ipynb)
│       ├── 01_library_check.ipynb
│       ├── 02_numpy_practice.ipynb
│       ├── 03_load&explore_dataset.ipynb
│       ├── 04_value_salesPrediction.ipynb
│       ├── 06_classification_analysis.ipynb
│       ├── 07_spam_detection.ipynb
│       ├── 08_customer_churn_model_comparision.ipynb
│       ├── 09_Mall_Customer_Segmentation.ipynb
│       ├── 0_oil_sales.ipynb
│       ├── house_price_prediction.ipynb
│       ├── models/             # Exported model artifacts (.pkl, .json)
│       └── *.png               # Generated evaluation plots & charts
│
└── exercises/                  # Standalone Python scripts & practice tasks
    ├── ethiopian_news.csv      # News dataset for scraping & NLP exercises
    ├── analysis.py
    ├── data_cleaning&Wrangling.py
    ├── data_visualization.py
    ├── data_wrangling_exercises.py
    ├── datavisualization_exercise1.py
    ├── missing_values.py
    ├── news_scraper.py
    ├── news_scraper2.py
    ├── number_analyzer.py
    ├── numpy_exercise2.py
    ├── pandas_exercise.py
    ├── pandas_exercise2.py
    ├── sql_db_exercises.py
    ├── student_analytics.py
    └── student_performance_analysis.py
```

---

## 🚀 Getting Started

### 1. Environment Setup

This repository uses a virtual environment located in `.venv`.

**To activate in PowerShell:**
```powershell
.\.venv\Scripts\Activate.ps1
```

**To activate in Command Prompt (`cmd`):**
```cmd
.venv\Scripts\activate.bat
```

**To install / update dependencies:**
```powershell
pip install -r requirements.txt
```

---

## 📓 Running Jupyter Notebooks

1. Open any notebook in `Qiyas-learning-path/notebooks/` using VS Code.
2. In the top-right corner, click **Select Kernel** -> **Python Environments...** -> select **`.venv`** (or **`Python (Qiyas_AI)`**).
3. Execute cells using <kbd>Shift</kbd> + <kbd>Enter</kbd>.

---

## 🐍 Running Standalone Scripts

The `.py` files in `exercises/` are standalone scripts designed to execute end-to-end from the terminal:

```powershell
cd exercises
python pandas_exercise.py
python news_scraper.py
```
