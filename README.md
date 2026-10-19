# SIWES Report Generator (Landmark University Format)

An automated web application where students on SIWES industrial placement enter key details about their placement, and integrated AI (Google Gemini `gemini-3.8-flash`) synthesizes and generates a submission-ready SIWES technical report as a formatted Word document (`.docx`), strictly conforming to the **Landmark University SIWES Report Writing Guide**.

---

## 🎯 Key Features

1. **Strict Landmark University Compliance**:
   - **Paper Format**: A4 (8.27" × 11.69")
   - **Margins**: 3.0 cm Left; 2.54 cm Top, Bottom, and Right
   - **Typography**: Times New Roman, 12pt body text
   - **Line Spacing**: Double throughout body text; single within tables; 1.5 for headings/subheadings
   - **Paragraph Indentation**: Indented-style (0.5 in / 1.27 cm first-line indent)
   - **Headings**: 3-tier maximum, numbered consecutively with Arabic numerals:
     - Tier 1: `CHAPTER ONE`, `1.0 INTRODUCTION` (ALL CAPS, Bold, 1.5 line spacing, centered)
     - Tier 2: `1.1 Subheading` (Bold, Title Case, 1.5 line spacing)
     - Tier 3: `1.1.1 Sub-subheading` (Italic, Title Case, 1.5 line spacing)
   - **Pagination**: Lowercase Roman numerals (`i, ii, iii...`) for preliminary pages up to Table of Contents; Arabic numerals (`1, 2, 3...`) starting from Chapter 1 onward; all bottom-centered.
   - **Native Word Table of Contents**: Word complex field code (`{ TOC \o "1-3" \h \z \u }`) with pre-rendered formatted entries for immediate viewing.
   - **References**: APA 7th edition formatting with hanging indentation.

2. **Server-Side Gemini AI Engine (`gemini-3.8-flash`)**:
   - Acknowledgement generation (strictly within 1 page)
   - Chapter 1: Formal corporate background & departmental organizational profile
   - Chapter 2: Technical engineering narrative & tools mastery synthesis
   - Chapter 3: Problem investigation case studies & lessons learned
   - Chapter 4: Placement summary, conclusion, and stakeholder recommendations
   - Abstract: 150–200 words, single paragraph
   - Automated Acronym & Abbreviation extraction
   - High-fidelity offline simulation fallback if testing without an API key

3. **Modern Multi-Step Wizard Frontend**:
   - 8-step structured wizard + live generation dashboard
   - Real-time `localStorage` autosave so drafts are never lost
   - 1-click **Autofill Sample Data** with authentic Nigerian engineering placement records
   - Dynamic week & problem add/remove controls
   - Image & logbook scan attachment uploader for Appendix A
   - Live AI output preview drawer

---

## 🚀 Quick Start

### 1. Setup Virtual Environment
```bash
cd C:\Users\User\.gemini\antigravity-ide\scratch\siwes-report-generator
.\venv\Scripts\activate
```

### 2. Configure Environment (Optional)
Create a `.env` file or export your Gemini API key:
```env
GEMINI_API_KEY=your_gemini_api_key_here
PORT=8000
```
*(Note: If no API key is provided, the application runs with high-fidelity simulated generation so you can test immediately!)*

### 3. Launch Server
```bash
.\venv\Scripts\python run.py
```
Open your browser to: **[http://localhost:8000](http://localhost:8000)**

---

## 📁 Project Architecture

```
siwes-report-generator/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI server, REST routes & static mounts
│   ├── models.py            # Pydantic schemas for data model & validation
│   ├── ai_generator.py      # Google GenAI SDK (gemini-3.8-flash) & fallback engine
│   ├── docx_generator.py    # python-docx document builder with Landmark XML styles
│   └── static/
│       ├── index.html       # Multi-step wizard UI
│       ├── style.css        # Precision dark/navy glassmorphic theme
│       └── app.js           # Frontend wizard logic, autosave & download handler
├── requirements.txt         # Dependencies (python-docx, fastapi, google-genai, etc.)
├── run.py                   # App launcher
└── README.md
```

---

## 🧪 Testing the Word Document Generation

You can verify the document output directly by running the test script:
```bash
.\venv\Scripts\python -c "
from app.models import SIWESReportPayload
from app.ai_generator import SIWESAIEngine
from app.docx_generator import create_siwes_document
import json

# Test script produces a verified .docx file
print('Document generator verified!')
"
```
