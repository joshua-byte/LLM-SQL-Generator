# 🧠 Gemini-Powered Natural Language to SQL Generator

This project is a full-stack AI tool that converts natural language prompts into SQL queries using Google's Gemini 1.5 Flash. It supports schema-aware prompting and includes a simple frontend built with static HTML, CSS, and JavaScript.

---

## 🚀 Features

- 🔍 **Natural Language → SQL** using Gemini 1.5 Flash
- 📄 **Schema-Aware**: Paste or upload custom table schemas
- 💡 **Prompt-Based Querying**: Type your question like “List customers who spent over $1000 last month”
- 🧾 **Formatted SQL Output**: Optimized, clean, standard SQL
- 🔐 **Secure API Key Handling** (no hardcoded secrets)
- 🌐 **Simple Web UI** (no frameworks — pure HTML/CSS/JS)

---

## 📂 Project Structure

```
gemini-sql-generator/
├── backend/
│   ├── app.py              # FastAPI or Flask backend
│   └── requirements.txt    # Python dependencies
├── frontend/
│   └── index.html          # UI to enter prompt + schema
├── sample_schema.json      # Example schema for testing
├── README.md
└── .gitignore
```

---

## 🛠️ Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/joshua-byte/LLM-SQL-Generator.git
cd LLM-SQL-Generator
```

### 2. Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 3. Set Your API Key

Add your Gemini API key as an environment variable:

```bash
export GEMINI_API_KEY=your-api-key-here  # Linux/macOS

# OR on Windows:
set GEMINI_API_KEY=your-api-key-here
```

### 4. Run the Backend

```bash
python app.py
```

By default, it runs on:  
`http://localhost:8000/generate-sql`

---

### 5. Open the Frontend

In a browser, open:

```
frontend/index.html
```

Use the UI to:
- Paste your schema
- Type your prompt
- Click “Generate SQL”
- View and copy the output

---

## 🔐 Environment & API Key Security

This app uses the `GEMINI_API_KEY` environment variable to protect your key.  
**⚠️ Never commit `.env` or your actual key to GitHub.**

---

## 📦 Dependencies

- Python 3.10+
- `google-generativeai`
- (Optional) `python-dotenv` if using `.env` files
- No JS frameworks — vanilla frontend only

---

## 💡 Example Prompts

| Prompt | What It Does |
|--------|---------------|
| “List all customers who ordered in the last 30 days” | Time-based filtering |
| “Show names and emails of users with >3 orders” | Joins + aggregation |
| “Get total sales grouped by product” | `GROUP BY` and `SUM()` |


## 🧠 Credits

- Built by Joshua Jesuraj Sanctus
- Powered by [Gemini 1.5 Flash](https://makersuite.google.com/)

---

## 🧪 Future Enhancements

- [ ] SQL execution + result table display
- [ ] Add dialect selection (SQLite, MySQL, etc.)
- [ ] Save prompt history
- [ ] Deploy on Replit/Hugging Face Spaces

---

## 📜 License

MIT License
