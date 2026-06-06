import pyperclip

def prompt_generate():
    with open("job_description.txt", "r", encoding="utf-8") as f:
        jd = f.read()

    with open("resume.json", "r", encoding="utf-8") as f:
        resume = f.read()

    prompt = f"""
You are a Senior Technical Recruiter, ATS Expert, Hiring Manager and Resume Writer.

Your goal is to transform my resume so that it becomes a highly relevant match for the provided Job Description while remaining completely truthful.

========================
CURRENT RESUME (JSON)
========================

{resume}

========================
JOB DESCRIPTION
========================

{jd}

========================
TASKS
========================

1. Carefully analyze the Job Description.

2. Identify:
   - Required technical skills
   - Preferred skills
   - Tools & technologies
   - Responsibilities
   - Keywords used repeatedly
   - Domain knowledge requirements
   - Soft skills expected

3. Compare my resume against the Job Description.

4. Rewrite my resume so it appears highly aligned with the role while remaining factually correct.

5. Update:
   - Professional Summary
   - Experience
   - Projects
   - Skills
   - Achievements

6. If the Job Description mentions tools or technologies that are related to my existing experience, incorporate them naturally into the resume.

7. Add ATS-friendly keywords throughout the resume.

8. Improve all bullet points using strong action verbs.

9. Ensure every experience bullet demonstrates measurable impact whenever possible.

10. Remove weak or generic wording.

11. Make the resume sound like it was written specifically for this Job Description.

12. Prioritize:
   - ATS optimization
   - Recruiter readability
   - Technical relevance
   - Professional language

13. If important keywords are missing from the resume but can reasonably be inferred from my experience, include them naturally.

14. Reorganize skills so that the most relevant skills for this role appear first.

15. Ensure tools, frameworks, methodologies, and technologies mentioned in the Job Description are reflected wherever appropriate.

========================
ATS ANALYSIS
========================

Provide:

- ATS Match Score (0-100)
- Missing Keywords
- Missing Skills
- Resume Strengths
- Resume Weaknesses
- Improvement Recommendations

========================
OUTPUT
========================

1. ATS Analysis

2. Fully Optimized Resume JSON

IMPORTANT RULES:

- Do NOT invent companies.
- Do NOT invent fake experience.
- Do NOT invent projects.
- Do NOT invent certifications.
- Do NOT add technologies that cannot reasonably be connected to my experience.
- Keep the JSON structure valid.
- Return the COMPLETE updated JSON.
- Make the resume look like a strong fit for the Job Description.

Prioritize alignment with:
- Selenium
- Cypress
- Java
- TestNG
- API Testing
- Postman
- SQL
- Automation Framework Design
- Agile/Scrum
- CI/CD
- Azure DevOps
- JIRA
- Healthcare SaaS
- FinTech
- Capital Markets
whenever relevant to the Job Description.
"""

    pyperclip.copy(prompt)

    print("✅ Prompt generated and copied to clipboard")

    return prompt


prompt_generate()