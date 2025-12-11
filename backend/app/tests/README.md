# NearNow Automated Test Suite (v1)

This folder contains the automated evaluation system for the NearNow AI backend.

## Purpose
To ensure consistent, accurate, and high-quality behaviour from the LLM by validating:
- Tone
- Length constraints
- Structure
- Dataset-only reasoning
- Tag + type + hours matching
- Opening/closing variation
- Smooth conversational flow
- Honest handling of uncertainty
- Avoidance of invented details

## How it works
1. The FastAPI endpoint `/api/run_tests` loads `questions.txt`.
2. Each question is passed through the LLM.
3. The response is evaluated using a series of validators.
4. A test report is returned and also saved under `app/tests/results/`.

## Files
- `questions.txt` — The list of test questions.
- `results/` — Automatically generated JSON reports.
- `validators/` — Logical modules that score tone, structure, accuracy, etc.

## Running the test suite
Start the server:

