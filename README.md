# Personal Expense Tracker

A professional Streamlit-based expense tracker application.

## Features
-   **Add Expenses**: Easy usage sidebar form to add new transactions.
-   **Dashboard**: View total expenses, average transaction size, and last transaction amount.
-   **Visualizations**: Interactive Pie chart (Category distribution) and Bar chart (Monthly spending).
-   **Filtering**: Filter transactions by date range.
-   **Management**: Delete transactions directly from the list.
-   **Database**: SQLite backend for persistent storage.

## Project Structure
-   `app.py`: Main application file containing all logic.
-   `assets/`: Static resources.
-   `requirements.txt`: Project dependencies.


## Installation

1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the app:
    ```bash
    python -m streamlit run app.py
    ```

## Dependencies
-   streamlit
-   pandas
-   plotly
