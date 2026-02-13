import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
from datetime import datetime

# --- Configuration & Setup ---
st.set_page_config(page_title="Personal Expense Tracker", page_icon="💰", layout="wide")

DB_NAME = "expenses.db"

# --- Database Functions ---
def init_db() -> None:
    """Initialize the SQLite database and create the expenses table."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            amount REAL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_expense(date: str, category: str, amount: float, description: str) -> None:
    """Add a new expense to the database."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO expenses (date, category, amount, description)
        VALUES (?, ?, ?, ?)
    ''', (date, category, amount, description))
    conn.commit()
    conn.close()
    st.session_state["data_refresh"] = True

def delete_expense(expense_id: int) -> None:
    """Delete an expense from the database by ID."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()
    st.session_state["data_refresh"] = True

def get_expenses() -> pd.DataFrame:
    """Fetch all expenses from the database."""
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM expenses ORDER BY date DESC", conn)
    conn.close()
    return df

# Initialize DB
init_db()

# --- Custom CSS ---
st.markdown("""
    <style>
    /* Global Background */
    .stApp {
        background-color: #f0f2f6;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
    }
    section[data-testid="stSidebar"] .stButton button {
        background-color: #6C63FF;
        color: white;
        border-radius: 8px;
        border: none;
    }
    section[data-testid="stSidebar"] .stButton button:hover {
        background-color: #5a52d5;
        color: white;
    }
    section[data-testid="stSidebar"] h2 {
        color: #6C63FF;
    }

    /* Metric Cards */
    div.css-1r6slb0.e1tzin5v2 { 
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
    
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        border-left: 5px solid #ccc;
    }
    .metric-card.total { border-left-color: #28a745; }   /* Green */
    .metric-card.avg { border-left-color: #007bff; }     /* Blue */
    .metric-card.last { border-left-color: #fd7e14; }    /* Orange */
    
    .metric-label { font-size: 0.9em; color: #6c757d; font-weight: 500; }
    .metric-value { font-size: 1.8em; font-weight: bold; color: #333; margin-top: 5px; }

    /* Custom Table Styling */
    .transaction-row {
        background-color: white;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 10px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .transaction-row:nth-child(even) {
        background-color: #f8f9fa;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("💰 Personal Expense Tracker")

# --- Sidebar: Add Expense ---
with st.sidebar:
    st.header("➕ Add New Expense")
    with st.form("expense_form", clear_on_submit=True):
        date = st.date_input("Date", datetime.today())
        category = st.selectbox("Category", ["Food", "Transport", "Utilities", "Entertainment", "Shopping", "Other"])
        amount = st.number_input("Amount (₹)", min_value=0.01, format="%.2f")
        description = st.text_input("Description")
        submitted = st.form_submit_button("Add Expense")
        
        if submitted:
            add_expense(date, category, amount, description)
            st.success("Expense added successfully!")

# --- Main Dashboard ---
if "data_refresh" not in st.session_state:
    st.session_state["data_refresh"] = False

df = get_expenses()

# Date Range Filter
st.subheader("Filter Transactions")
col_start, col_end = st.columns(2)
today = datetime.today()
first_day_of_month = today.replace(day=1)

with col_start:
    start_date = st.date_input("Start Date", first_day_of_month)
with col_end:
    end_date = st.date_input("End Date", today)

if not df.empty:
    df['date'] = pd.to_datetime(df['date'])
    mask = (df['date'] >= pd.to_datetime(start_date)) & (df['date'] <= pd.to_datetime(end_date))
    filtered_df = df.loc[mask].sort_values(by='date', ascending=False)
else:
    filtered_df = df

# --- Metrics ---
col1, col2, col3 = st.columns(3)
if not filtered_df.empty:
    total_expense = filtered_df["amount"].sum()
    avg_transaction = filtered_df["amount"].mean()
    last_transaction = filtered_df.iloc[0]["amount"]
else:
    total_expense = 0.0
    avg_transaction = 0.0
    last_transaction = 0.0

with col1:
    st.markdown(f"""
        <div class="metric-card total">
            <div class="metric-label">Total Expenses</div>
            <div class="metric-value">₹{total_expense:,.2f}</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="metric-card avg">
            <div class="metric-label">Average Transaction</div>
            <div class="metric-value">₹{avg_transaction:,.2f}</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="metric-card last">
            <div class="metric-label">Last Transaction</div>
            <div class="metric-value">₹{last_transaction:,.2f}</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Charts ---
col_chart1, col_chart2 = st.columns(2)

if not filtered_df.empty:
    # 1. Pie Chart
    with col_chart1:
        st.subheader("Expenses by Category")
        fig_pie = px.pie(filtered_df, values='amount', names='category', hole=0.4, 
                         title="Category Distribution", color_discrete_sequence=px.colors.qualitative.Pastel)
        fig_pie.update_layout(showlegend=True, legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
        st.plotly_chart(fig_pie, use_container_width=True)

    # 2. Bar Chart
    with col_chart2:
        st.subheader("Monthly Spending")
        monthly_df = filtered_df.copy()
        monthly_df['Month'] = monthly_df['date'].dt.strftime('%b %Y')
        monthly_order = monthly_df.sort_values('date')['Month'].unique()
        monthly_summary = monthly_df.groupby('Month')['amount'].sum().reset_index()
        
        fig_bar = px.bar(monthly_summary, x='Month', y='amount', title="Total Spending per Month",
                         category_orders={"Month": monthly_order}, color_discrete_sequence=['#6C63FF'])
        fig_bar.update_layout(xaxis_title=None, yaxis_title="Amount (₹)")
        st.plotly_chart(fig_bar, use_container_width=True)
else:
    st.info("No expenses found for the selected date range.")

# --- Transaction List ---
st.subheader("Recent Transactions")

if not filtered_df.empty:
    # Header
    st.markdown("""
    <div style="display: flex; justify-content: space-between; padding: 10px; font-weight: bold; color: #555; border-bottom: 2px solid #eee;">
        <span style="width: 15%;">Date</span>
        <span style="width: 15%;">Category</span>
        <span style="width: 40%;">Description</span>
        <span style="width: 15%; text-align: right;">Amount</span>
        <span style="width: 10%; text-align: right;">Action</span>
    </div>
    """, unsafe_allow_html=True)

    # Rows
    for index, row in filtered_df.iterrows():
        col_row = st.columns([1.5, 1.5, 4, 1.5, 1])
        
        with col_row[0]:
            st.write(row['date'].strftime('%Y-%m-%d'))
        with col_row[1]:
            st.write(row['category'])
        with col_row[2]:
            st.write(row['description'])
        with col_row[3]:
            st.markdown(f"<div style='text-align: right; font-weight: bold;'>₹{row['amount']:.2f}</div>", unsafe_allow_html=True)
        with col_row[4]:
            if st.button("🗑️", key=f"del_{row['id']}", help="Delete transaction"):
                delete_expense(row['id'])
                st.rerun()
        
        st.markdown("<hr style='margin: 5px 0; border: none; border-bottom: 1px solid #f0f0f0;'>", unsafe_allow_html=True)

else:
    st.info("No recent transactions to display.")



