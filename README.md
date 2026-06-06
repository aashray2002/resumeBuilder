# resumeBuilder
# AI Resume Optimizer

An end-to-end Resume Optimization System that automatically tailors a resume according to a Job Description (JD), generates an ATS-friendly resume JSON, renders a professional HTML resume, and exports it as a PDF.

---

## Features

* Upload/Paste Job Description
* Existing Resume JSON Support
* ATS Optimization using Gemini AI
* Automatic Resume Enhancement
* HTML Resume Generation
* PDF Resume Export
* Dynamic Skills, Projects, Experience Rendering
* Fully Automated Workflow

---

## Project Workflow

```text
Resume JSON
      +
Job Description
      ↓
Prompt Generator
      ↓
Gemini AI
      ↓
Optimized Resume JSON
      ↓
HTML Renderer
      ↓
PDF Generator
      ↓
Final Resume PDF
```

---

## Project Structure

```text
resume-optimizer/

│
├── app.py
├── main.py
│
├── prompt_generator.py
├── gemini_sender.py
├── response_handler.py
├── render_resume.py
├── generate_pdf.py
│
├── resume.html
├── resume.css
│
├── resume.json
├── optimized_resume.json
│
├── job_description.txt
│
├── final_resume.html
├── resume.pdf
│
└── README.md
```

---

## Requirements

### Python Version

```bash
Python 3.10+
```

### Install Dependencies

```bash
pip install selenium
pip install pyperclip
pip install streamlit
pip install playwright
```

Install Playwright Browser:

```bash
playwright install
```

---

## Input Files

### resume.json

Base Resume in JSON format.

Example:

```json
{
  "personal_info": {
    "name": "Aashray",
    "title": "QA Automation Engineer"
  }
}
```

---

### job_description.txt

Paste complete Job Description.

Example:

```text
Automation Test Engineer

Skills:
Python
Pytest
API Testing
Selenium
```

---

## Running the Application

### Streamlit UI

Start UI:

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

### Command Line Workflow

```bash
python main.py
```

---

## Automation Flow

### Step 1

Generate AI Prompt

```python
prompt_generate()
```

---

### Step 2

Open Gemini

```python
send_to_gemini()
```

Actions:

* Open Gemini
* Paste Prompt
* Submit Prompt
* Wait for Response
* Extract Resume JSON
* Save optimized_resume.json

---

### Step 3

Generate Resume HTML

```python
render_resume()
```

Output:

```text
final_resume.html
```

---

### Step 4

Generate PDF

```python
html_to_pdf()
```

Output:

```text
resume.pdf
```

---

## Generated Files

### optimized_resume.json

ATS Optimized Resume

---

### final_resume.html

Rendered Resume Template

---

### resume.pdf

Final Downloadable Resume

---

## Dynamic Sections

The following sections are rendered dynamically:

* Personal Information
* Summary
* Education
* Experience
* Skills
* Projects
* Certifications
* Achievements
* Highlights

No manual HTML editing is required.

---

## Technologies Used

### Backend

* Python

### Automation

* Selenium
* Playwright

### Frontend

* HTML
* CSS
* Streamlit

### AI

* Gemini

### Data Format

* JSON

---

## Future Enhancements

* OpenAI API Integration
* Multiple Resume Templates
* Dark Theme Resume
* Resume Preview Before Download
* Cover Letter Generation
* LinkedIn Profile Import
* Resume Scoring Dashboard
* Multi-Language Resume Support

---

## Author

Aashray Dhiman

QA Automation Engineer | Python & API Testing Specialist
