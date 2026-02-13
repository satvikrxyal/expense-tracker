# 💰 Personal Expense Tracker

A clean, responsive personal finance web app built with **Python** and **Streamlit**. Log your daily expenses, visualize spending patterns with interactive charts, filter by date range, and manage transactions — all in one place, with no sign-up required.

![App Screenshot](assets/screenshot.png)
![App Screenshot 2](assets/screenshot1.png)

---

## ✨ Features

- ➕ **Add Expenses** — log transactions with date, category, amount, and description via a clean sidebar form
- 🗑️ **Delete Transactions** — remove any entry directly from the transaction list
- 📅 **Date Range Filter** — filter all metrics and charts by a custom date range
- 📊 **Category Pie Chart** — interactive donut chart showing spending breakdown by category
- 📈 **Monthly Bar Chart** — track total spending trends month by month
- 🧮 **Summary Metrics** — at-a-glance cards for total spend, average transaction, and last transaction
- 💾 **Persistent Storage** — all data stored locally in a SQLite database
- 🎨 **Custom UI** — light theme with purple accents, colored metric cards, and a styled transaction list

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/satvikrxyal/expense-tracker.git
   cd expense-tracker
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run app.py
   ```

4. Open your browser at `http://localhost:8501` 🎉

---

## 📁 Project Structure

```
expense-tracker/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Pinned Python dependencies
├── .gitignore              # Git ignore rules
├── .streamlit/
│   └── config.toml         # Streamlit theme configuration
├── assets/
│   └── screenshot.png      # App preview image
└── README.md
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| [Python](https://python.org) | Core language |
| [Streamlit](https://streamlit.io) | Web UI framework |
| [SQLite](https://sqlite.org) | Local persistent storage |
| [Pandas](https://pandas.pydata.org) | Data manipulation |
| [Plotly](https://plotly.com) | Interactive charts |

---

## 📦 Dependencies

```
streamlit==1.32.0
pandas==2.2.1
plotly==5.20.0
```

---

## 🗂️ Expense Categories

| Category | |
|----------|-|
| 🍔 Food | 🚗 Transport |
| 💡 Utilities | 🎬 Entertainment |
| 🛍️ Shopping | 📦 Other |

---

## 🔮 Roadmap

- [ ] Export transactions to CSV
- [ ] Budget limits and alerts per category
- [ ] Multi-currency support
- [ ] Monthly spending goals
- [ ] Dark mode toggle
- [ ] Modular code structure (components, database layer)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">
  Made with ❤️ by <a href="https://github.com/satvikrxyal">satvikrxyal</a>
</div>
