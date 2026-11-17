"""NeuroHydro - Flask version of the site."""
import csv
import re
from datetime import datetime, timezone
from pathlib import Path

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
ASSET_BASE = "https://neurohydro.vercel.app"  # images/video are hosted on the live site
WAITLIST_FILE = Path("waitlist.csv")
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

LAYERS = [
    ("Protective Waterproof Film", "A breathable, semi-permeable barrier that shields the electronics from external water and contaminants while allowing sweat vapor to pass through."),
    ("PET Sensing Layer", "Flexible polyethylene terephthalate circuit board housing the electrochemical sensing electrodes that detect sodium, potassium, and pH levels."),
    ("Microfluidic Section", "Precision-engineered SU-8 photoresist channels utilize capillary action to passively transport sweat to the sensing electrodes without pumps."),
    ("Hydrophilic Filler Layer", "A specialized porous hydrophilic interface that rapidly wicks sweat from skin pores, ensuring consistent analyte delivery to the microfluidics."),
    ("Flexible Skin Adhesive", "Skin-safe, flexible bio-adhesive designed for conformal skin contact, minimizing motion artifacts and ensuring reliable signal acquisition during activity."),
]
APP_FEATURES = [
    "Live alerts when your electrolyte balance drops",
    "Hydration trends mapped against mood & focus",
    "A recovery summary after every workout",
]
BENEFITS = [
    ("benefit_performance.webp", "Physical Performance", "Losing just 2% of your body's water measurably reduces strength, speed, and endurance, often before you even feel thirsty."),
    ("benefit_cognitive.webp", "Cognitive Function", "Research links even mild dehydration to slower reaction times, weaker concentration, and lower mood."),
    ("benefit_recovery.webp", "Muscular Recovery", "Restoring the sodium, potassium, and fluid you lose in sweat is a key part of how your muscles recover after hard efforts."),
]
TEAM = [
    ("Celine Ding", "Cross country captain, Middlesex School", "celine_photo.webp"),
    ("Bingchen Hu", "Youth Advisory Board Leader", "bingchen_photo.webp"),
    ("Kerun Li", "Research Intern, MGH/Harvard", "kerun_photo.webp"),
    ("Sophie Liu", "Dance Company Member, Madeira School", "sophie_photo.webp"),
    ("Ethan Huang", "Competitive fencer and musician", "ethan_photo.webp"),
]
STORY = [
    "Mild dehydration is a silent performance killer. A small drop shows up as fatigue, irritability, slower thinking, and weaker focus. Most people still rely on thirst, and thirst arrives late.",
    "NeuroHydro started as a student-built solution to a real daily pattern we kept seeing in ourselves and our peers: intense training, packed academic schedules, and long days, followed by unexplained dips in energy and mood.",
    "We realized hydration wasn't just \"physical.\" It was cognitive. So we built a wearable sweat patch that tracks electrolyte and pH trends in real time, then turns that data into clear, actionable guidance through a mobile app.",
    "Our goal is simple: make hydration visible, measurable, and actionable, so students, athletes, and outdoor workers can protect their focus, stabilize mood, and perform at their best before dehydration becomes a problem.",
]
VALUES = [
    ("Scientific Precision", "reliable sensing, signal quality, and meaningful interpretation of sweat data."),
    ("Human-Centered Care", "insights designed to feel encouraging, actionable, and easy to follow in real life."),
    ("Long-Term Engagement", "habits over hype, tracking hydration, mood, and focus trends over time."),
]


@app.route("/")
def index():
    return render_template(
        "index.html", layers=LAYERS, features=APP_FEATURES,
        benefits=BENEFITS, team=TEAM, story=STORY, values=VALUES,
        asset_base=ASSET_BASE,
    )


@app.route("/waitlist", methods=["POST"])
def waitlist():
    data = request.get_json(silent=True) or request.form
    if data.get("website"):  # honeypot: bots fill this hidden field
        return jsonify(ok=True)
    name = (data.get("name") or "").strip()[:100]
    email = (data.get("email") or "").strip()[:200]
    if not EMAIL_RE.match(email):
        return jsonify(ok=False, error="Please enter a valid email address."), 400

    is_new = not WAITLIST_FILE.exists()
    with WAITLIST_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if is_new:
            writer.writerow(["timestamp", "name", "email"])
        writer.writerow([datetime.now(timezone.utc).isoformat(), name, email])
    return jsonify(ok=True)


if __name__ == "__main__":
    app.run(debug=True)
