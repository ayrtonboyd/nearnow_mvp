# NearNow — Local AI Concierge (MVP)

**Tagline:** Be a local, anywhere.  
**Status:** Early MVP · Kendal-only demo

NearNow is a friendly AI concierge that helps you find cafés and pubs based on what you’re in the mood for — starting with Kendal in the Lake District.

This MVP focuses on:

- Using a **curated local dataset** (Kendal cafés & pubs)
- A **strict, dataset-only AI prompt** (no hallucinated venues)
- A clean, simple **web UI** for natural-language search

---

## ✨ Features (MVP)

- 🔍 **Natural-language search**  
  Ask things like _“Cosy café open for lunch”_ or _“Dog-friendly pub for a quiet pint”_.

- 📍 **Kendal-only curated dataset**  
  ~20 cafés and ~20 pubs, each with type, opening hours, tags, and descriptions.

- 🧠 **Strict, rule-based AI behaviour**  
  The system prompt forces the model to:
  - Use only the provided dataset  
  - Never invent venues  
  - Return 2–3 best matches with clear trade-offs

- 💬 **Friendly concierge tone**  
  Responses read like a helpful Kendal local, not a robot.

- 🧪 **Tested prompt**  
  Prompt tuned via “golden question” families (atmosphere, features, price, etc.) to reach high consistency.

- 🖥 **Simple, clean UI**  
  - Logo + tagline  
  - Friendly greeting (“How can I help you today?”)  
  - Embedded search bar with send icon  
  - Rotating suggested questions (20-question pool, 3 shown per load)  
  - Typewriter-style answer display with smooth auto-scroll

---

## 🧱 Tech Stack

**Backend**

- [FastAPI](https://fastapi.tiangolo.com/) — API layer  
- [OpenAI](https://platform.openai.com/) — `gpt-4o-mini` (via API)  
- [LangChain](https://www.langchain.com/) — prompt + LLM integration  
- JSON data files for locations and tags

**Frontend**

- [Next.js](https://nextjs.org/) (App Router)  
- React + TypeScript  
- TailwindCSS for styling  
- `react-icons` for the send button

---

## 📂 Project Structure

```txt
nearnow_mvp/
  backend/
    app/
      data/
        locations.json      # curated Kendal cafés & pubs
        tags.json           # tag dictionary (atmosphere, features, dietary, etc.)
      routes/
        recommend.py        # /api/recommend endpoint
      services/
        llm.py              # builds prompt + calls OpenAI
        data_loader.py      # loads JSON data
      prompts/
        system_prompt.txt   # NearNow v3.x system message (NOT committed to Git)
    requirements.txt
    .env.example

  frontend/
    app/
      page.tsx             # main NearNow UI
    public/
      logo.png             # NearNow logo
    package.json
    tailwind.config.js
