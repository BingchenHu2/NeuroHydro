# NeuroHydro
# NeuroHydro

A student-built biosensing sweat patch that turns sweat into real-time hydration and electrolyte insight. This repo is the Python (Flask) version of the NeuroHydro website, including a working waitlist signup.

Live prototype site: https://neurohydro.vercel.app/

## Features
- Single-page site: product layers, app overview, the problem, team, story
- Working waitlist form (name optional, email validated, spam honeypot)
- Signups saved to `waitlist.csv` on the server
- Responsive layout with light/dark mode

## Media
Images and the demo video load from the live site (https://neurohydro.vercel.app). To self-host them, copy the files into `static/images/` and `static/videos/` and change the `asset_base` URLs in `templates/index.html` back to `url_for('static', ...)`.

## Run it locally
```bash
git clone <your-repo-url>
cd neurohydro-python
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Then open http://127.0.0.1:5000.

## Project structure
```
app.py              Flask app, page content, /waitlist endpoint
templates/index.html
static/css/style.css
static/images/      site images
static/videos/      demo video
```

## Disclaimer
NeuroHydro is a student-built prototype developed at Pomfret School. It is not a medical device and does not provide medical or health advice.
