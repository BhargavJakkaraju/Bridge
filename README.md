# Bridge

This platform is a personalized research discovery tool where users select a domain of interest and specify their AI expertise, and the system retrieves recent academic papers sitting at that intersection and delivers them as a multi-modal short-form content feed including text summaries, narrated videos, and interactive applets. It includes full user authentication and persistent profiles so that search history and preferences are saved across sessions, backed by a FastAPI Python backend handling the retrieval and orchestration pipeline and a Next.js TypeScript frontend serving the UI.

## Project Structure

- `backend/`: FastAPI + SQLAlchemy + Supabase JWT validation
- `frontend/`: React + TypeScript (Vite) + Supabase client auth hook

### 1) Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python -m uvicorn app.main:app --reload --port 8000
```

Health check:
- `GET http://localhost:8000/health`

### 2) Frontend

```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```
