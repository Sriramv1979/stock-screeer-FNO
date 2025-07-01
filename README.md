# Stock Screener App

This app identifies F&O breakout/breakdown patterns using ICICI Breeze API.

## 🚀 Getting Started

### 📦 Install dependencies

#### Backend
```bash
cd backend
cp .env.example .env  # Fill with your Breeze credentials
pip install -r requirements.txt
uvicorn backend_main:app --reload --port 8000
```

#### Frontend (Streamlit)
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🌐 API
- Endpoint: `GET /screener`
- Returns list of stocks matching any of the 6 breakout/breakdown patterns

## ☁️ GitHub Upload

```bash
git init
git add .
git commit -m "Initial commit"
gh repo create stock-screener --public
git push -u origin main
```

You’re done!
