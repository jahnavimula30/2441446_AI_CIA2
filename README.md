# 🧠 AI Game Arena

Interactive quiz game for **DSC401-6 Artificial Intelligence (Units I & II)**, built with Python + Streamlit.

* **63 questions** · 11 topics · 7 formats (MCQ, True/False, Assertion-Reason, Fill in the Blanks, Match the Following, Scenario, Problem-solving)
* 12 real-world scenario questions · 21 search / state-space questions
* **Features:** random questions · Easy/Medium/Hard levels · per-question timer · progress bar · instant feedback with explanations · lifelines (💡 Hint, ✂️ 50-50, ⏭️ Skip) · streak counter · topic-wise analysis · leaderboard · CSV download · built-in question bank viewer

## Project structure

```
ai-quiz-arena/
├── app.py                         # Streamlit app (UI + game logic)
├── questions.py                   # the question bank (edit/add questions here)
├── requirements.txt               # dependencies for Streamlit Cloud
├── scripts/export_question_bank.py# validates assignment rules, regenerates docs/
├── docs/QUESTION_BANK.md          # question bank with correct answers (generated)
├── docs/question_bank.csv         # same, spreadsheet-friendly (generated)
├── docs/REPORT.md                 # report template for submission
├── .streamlit/config.toml         # theme
├── Dockerfile                     # optional, for container hosts
└── data/                          # leaderboard.csv is created here at runtime
```

## Run locally

```bash
python -m venv .venv && source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Put it on GitHub

1. Create an empty **public** repository on github.com (e.g. `ai-quiz-arena`), with no README or .gitignore.
2. In this folder run:

```bash
git init
git add .
git commit -m "AI Game Arena for DSC401-6"
git branch -M main
git remote add origin https://github.com/<your-username>/ai-quiz-arena.git
git push -u origin main
```

## Deploy free on Streamlit Community Cloud

1. Go to <https://share.streamlit.io> and sign in with your GitHub account.
2. Click **Create app** → *Deploy a public app from GitHub*.
3. Choose your repository, branch `main`, and main file path `app.py`.
4. (Optional) pick a custom subdomain, e.g. `your-name-ai-quiz`.
5. Click **Deploy**. After a minute you get a public link like `https://your-name-ai-quiz.streamlit.app`.

Every `git push` to `main` redeploys automatically. Free apps go to sleep after a period of inactivity. Open the link
beforehand (or click *Wake up*) before your class demo. Free-tier limits change, so check the current terms on Streamlit's site.

> **Leaderboard note:** the leaderboard is a CSV file on the server's disk. On free hosting it can reset when the app
> restarts or redeploys. That is fine for a class demo. For permanent storage, connect a free database
> (e.g. Google Sheets or Supabase) in `save_score()` / `load_lb()`.

### Other free hosts
The included `Dockerfile` works on container platforms (Render, Hugging Face Spaces *Docker* SDK, Google Cloud Run, Fly.io).
These platforms have their own free-tier rules and setup steps, so check their docs.

## Updating questions

Add a call in `questions.py` (`mcq`, `tf`, `ar`, `fill`, `match`), then run:

```bash
python scripts/export_question_bank.py
```

This re-checks the assignment rules (≥ 50 questions, ≥ 10 real-world, ≥ 5 search, all formats and topics) and refreshes `docs/`.
