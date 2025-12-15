# How NearNow Works

NearNow is designed to feel less like a search engine and more like a local concierge.

This document explains **how NearNow thinks**, **why it behaves the way it does**, and **the principles behind its design**.

---

## 1. NearNow is Dataset-First, Not Web-First

NearNow does **not** browse the internet or scrape live results.

Instead, it relies on:
- A **curated local dataset** of cafés and pubs
- Structured attributes (opening hours, features, atmosphere, price)
- Human-written descriptions

This ensures:
- No hallucinated venues
- No outdated recommendations
- Predictable, testable responses
- Full control over quality and tone

If a venue is not in the dataset, NearNow will not invent it.

---

## 2. Deterministic Behaviour Over “Magic”

NearNow is intentionally **not** a free-roaming chatbot.

Every response is governed by:
- A strict system prompt
- A fixed dataset
- Clear behavioural constraints

This allows:
- Consistent recommendations
- Honest uncertainty when data is incomplete
- Reliable testing and scoring

The goal is trust, not surprise.

---

## 3. A Concierge-Style Conversation Model

NearNow speaks like a **friendly local who knows the area well**.

Design choices include:
- Warm, natural language
- Short, mobile-friendly responses
- Confident suggestions without sounding salesy
- No references to “data”, “tags”, or internal logic

The user should feel guided, not analysed.

---

## 4. Best-Fit First, Always

When a user asks a question, NearNow:
1. Interprets the intent (e.g. cosy, dog-friendly, open for lunch)
2. Filters venues using only known data
3. Orders results by **best match first**
4. Returns 2–3 venues when possible

If fewer venues match:
- NearNow responds confidently
- It does not apologise or explain scarcity
- It never pads results with poor matches

---

## 5. Honest Uncertainty

NearNow does not guess.

If something is unclear (for example:
- kitchen closing time
- exact menu cut-offs
- conditional availability),

It will:
- Phrase uncertainty naturally
- Avoid hard claims
- Maintain a helpful, human tone

This builds credibility over time.

---

## 6. Designed for Mobile Reading

All responses are shaped for phone screens:
- Clear structure
- Short paragraphs
- Tight word limits
- No information overload

NearNow respects the user’s attention.

---

## 7. Local First, Scalable by Design

This demo version is focused on **Kendal**.

However, the system is built to scale by:
- Adding new locations as structured data
- Reusing the same prompt and logic
- Maintaining local tone per region

Scaling does not require changing how NearNow thinks — only what it knows.

---

## 8. Why This Matters

NearNow is not trying to replace search engines.

It exists to answer a different question:

> “Where should I go right now, based on how I feel?”

By combining:
- curated data
- controlled AI behaviour
- and a human-first tone,

NearNow aims to become a trusted local companion — not just another AI interface.

---

*This document reflects the current MVP design and may evolve as NearNow grows.*
