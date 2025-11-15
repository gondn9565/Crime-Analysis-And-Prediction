<!-- .github/copilot-instructions.md -->
# Copilot / AI contributor guidance — Crime Analysis & Prediction repo

This file gives concise, actionable guidance to an AI coding assistant working on this repository.

1. Big picture
   - Purpose: a small data science + web frontend project to analyze an India crime dataset and expose a minimal Flask API (`backend/app.py`) used by the `frontend/` UI.
   - Key components:
     - `maincode.ipynb`: primary data-processing and analysis class (`CrimeAnalysis`) with methods for preprocessing, EDA, hotspot identification, prediction, precision-matrix analysis and policy recommendations. Treat this notebook as the canonical data pipeline / algorithmic reference.
     - `backend/app.py`: minimal Flask backend exposing `/api/upload` and `/api/stats`. It expects CSV uploads and returns JSON stats; use it for integration tests and to mock API behavior.
     - `frontend/`: UI code (not inspected in detail). Changes in API shape must be coordinated with this folder.

2. Developer workflows (what to run)
   - Notebook-first: open `maincode.ipynb` to iterate on preprocessing and models. Use a Jupyter environment with pandas, scikit-learn, matplotlib, seaborn installed.
   - Run backend locally: `python backend/app.py` (Flask default on port 5000). It uses CORS and returns dummy stats; update only if adding new endpoints.
   - When modifying the API payloads, update `frontend/` to match and test via the browser or curl.

3. Project-specific conventions & patterns
   - The data-processing logic lives in a single class `CrimeAnalysis` inside `maincode.ipynb`. New data features or encoders should be added as class attributes (e.g., `self.encoders`) so subsequent methods can reuse them.
   - Date parsing uses dayfirst=True for `Date Reported` / `Date of Occurrence` — assume dd-mm-yyyy input. If adding CSV reading elsewhere, preserve the same assumptions.
   - Target creation: violent crime is derived from `Crime Domain` into `Violent_Crime` (binary). Keep downstream models aligned to that column name.
   - Missing-value handling: the notebook often fills or imputes in-place before modeling. Mirror that behavior in any standalone scripts (avoid silently dropping rows unless the notebook does so and logs counts).

4. Integration points & dependencies
   - External libs used in notebook: pandas, numpy, matplotlib, seaborn, scikit-learn. The `GraphicalLasso` usage may require scikit-learn >= 0.24.
   - Backend: Flask + flask_cors. The backend accepts multipart file uploads and returns a small JSON stats object. When extending, respect existing route names `/api/upload` and `/api/stats`.

5. Concrete examples and quick edits
   - If you add a new feature column in `maincode.ipynb`, also update the `feature_columns` list in `predict_crime_occurrence()` — the code relies on an explicit list to build models.
   - When extracting hour from `Time of Occurrence`, the notebook first tries pd.to_datetime(...).dt.hour and falls back to string splitting. Keep both strategies when making robust changes.
   - Precision matrix flows: `calculate_precision_matrix()` expects at least 1000 non-null rows per numeric feature before including it; preserve or document any change to this threshold.

6. Safe edits & tests
   - Non-destructive edits: prefer adding helper functions (in the notebook or new module) rather than rewriting `CrimeAnalysis` in place. Add unit-like notebook cells that run small end-to-end checks on a sample CSV.
   - When changing API responses in `backend/app.py`, keep the existing keys in `/api/stats` (e.g., `totalCrimes`, `monthlyTrend`) or make frontend-coordinated changes.

7. Files to inspect when troubleshooting
   - `maincode.ipynb` — data logic and ML code (primary source of truth)
   - `backend/app.py` — Flask endpoints and upload handling
   - `crime_dataset_india.csv` — sample data expected by the notebook (if absent, use a small synthetic CSV while testing)

If anything here is unclear or you want the instructions to cover a specific workflow (tests, packaging, CI), tell me which parts to expand and I will iterate.
