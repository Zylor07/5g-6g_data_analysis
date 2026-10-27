# From 4G to 6G — Python dashboard

A calm, low-colour interactive website built with **Python + Streamlit**. No JavaScript knowledge is needed to customize the dashboard.

## Files
- `5G_6G_analysis.ipynb` — your original Jupyter notebook; the main research source.
- `app.py` — the website/dashboard code.
- `requirements.txt` — Python packages used by the dashboard.

## Run it in VS Code

1. Install Python 3.10 or newer and VS Code's Python extension.
2. Extract the project ZIP and open the `5g6g-python-dashboard` folder in VS Code.
3. Open the VS Code terminal (**Terminal → New Terminal**).
4. Create a virtual environment:
   - Windows: `python -m venv .venv` then `.venv\\Scripts\\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
5. Install dependencies: `python -m pip install -r requirements.txt`
6. Start the website: `python -m streamlit run app.py`
7. Your browser will open a local page, usually `http://localhost:8501`. Keep the terminal open while using it.

## Data note
The dashboard's KPI, city-tier, peak-hour, and latency-threshold tables reproduce summary values visible in the notebook's saved outputs. The notebook describes its dataset as synthetic, 6G as simulated, and latency thresholds as assumptions. This dashboard does **not** connect to a live telecom network. If you later provide `5G_6G_network_dataset.csv`, the dashboard can be upgraded to calculate all charts directly from that full dataset instead of summary values.
