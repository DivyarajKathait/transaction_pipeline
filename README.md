
# Transaction Pipeline

A real-time transaction monitoring and analytics pipeline that simulates, stores, and visualizes streaming financial data.

## 🧩 Project Structure

```
transaction_pipeline/
├── dashboard/        # Streamlit dashboard for data visualization
├── data/             # Raw data files (not pushed to Git)
├── db/               # SQLite DB storing transaction data (ignored in Git)
├── scripts/          # Scripts for simulating and ingesting transactions
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

## ⚙️ Features

- Simulates real-time financial transaction data
- Stores data in a lightweight SQLite database
- Visualizes transaction trends using Streamlit
- Modular design with clear separation of concerns

## 🚀 Setup Instructions

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/transaction_pipeline.git
cd transaction_pipeline
```

2. **Create and activate a virtual environment**:

```bash
# On Linux/macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Run the dashboard**:

```bash
streamlit run dashboard/dashboard.py
```

## 📁 Notes

- The `venv/`, `transactions.json`, and database files are **not tracked** in Git.
- Add your own simulated data or transaction sources in the `scripts/` directory.
- Modify or extend the dashboard as needed using Streamlit.

## 📄 License

This project is for educational purposes and does not process real financial data.
