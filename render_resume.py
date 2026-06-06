import json


def generate_education(data):
    html = ""

    for edu in data.get("education", []):

        duration = edu.get(
            "duration",
            edu.get("year", "")
        )

        html += f"""
        <div class="education-item">

            <div class="education-header">

                <div class="education-title">
                    {edu.get("institution", "")}
                </div>

                <div class="date-location">
                    {duration}
                </div>

            </div>

            <div class="education-subtitle">
                {edu.get("degree", "")}
            </div>

        </div>
        """

    return html


def generate_experience(data):

    html = ""

    for exp in data.get("experience", []):

        bullets = ""

        for item in exp.get("responsibilities", []):

            bullets += f"<li>{item}</li>"

        html += f"""
        <div class="experience-item">

            <div class="experience-header">

                <div class="company-role">
                    <strong>{exp.get("company", "")}</strong>,
                    {exp.get("designation", "")}
                </div>

                <div class="date-location">
                    {exp.get("duration", "")} |
                    {exp.get("location", "")}
                </div>

            </div>

            <ul class="experience-list">
                {bullets}
            </ul>

        </div>
        """

    return html


def generate_skills(data):

    html = ""

    skills = data.get("skills", {})

    for category, values in skills.items():

        category_name = (
            category
            .replace("_", " ")
            .title()
        )

        html += f"""
        <div class="skill-category">

            <div class="skill-title">
                {category_name}
            </div>

            <div class="skill-content">
                {" • ".join(values)}
            </div>

        </div>
        """

    return html


def generate_projects(data):

    html = ""

    for project in data.get("projects", []):

        bullets = ""

        for item in project.get("description", []):

            bullets += f"<li>{item}</li>"

        html += f"""
        <div class="project-item">

            <div class="project-title">
                {project.get("name", "")}
            </div>

            <div class="project-tech">
                {" | ".join(project.get("technologies", []))}
            </div>

            <ul>
                {bullets}
            </ul>

        </div>
        """

    return html


def generate_courses(data):

    html = ""

    for course in data.get("certifications", []):

        html += f"""
        <li>
            {course.get("name", "")}
            ({course.get("issuer", "")})
        </li>
        """

    return html


def generate_achievements(data):

    html = ""

    for achievement in data.get("achievements", []):

        html += f"""
        <li>
            <strong>{achievement.get("title", "")}</strong>
            - {achievement.get("event", "")}
        </li>
        """

    return html


def generate_highlights(data):

    html = ""

    for item in data.get("highlights", []):

        html += f"<li>{item}</li>"

    return html


def render_resume():

    with open(
        "optimized_resume.json",
        "r",
        encoding="utf-8"
    ) as f:

        data = json.load(f)

    with open(
        "resume.html",
        "r",
        encoding="utf-8"
    ) as f:

        html = f.read()

    # PERSONAL INFO

    html = html.replace(
        "{{fullName}}",
        data["personal_info"]["name"]
    )

    html = html.replace(
        "{{jobTitle}}",
        data["personal_info"]["title"]
    )

    html = html.replace(
        "{{email}}",
        data["personal_info"]["email"]
    )

    html = html.replace(
        "{{phone}}",
        data["personal_info"]["phone"]
    )

    html = html.replace(
        "{{location}}",
        data["personal_info"]["location"]
    )

    html = html.replace(
        "{{linkedin}}",
        ""
    )

    # SUMMARY

    html = html.replace(
        "{{professionalSummary}}",
        data.get("summary", "")
    )

    # EDUCATION

    html = html.replace(
        "{{education}}",
        generate_education(data)
    )

    # EXPERIENCE

    html = html.replace(
        "{{experience}}",
        generate_experience(data)
    )

    # SKILLS

    html = html.replace(
        "{{skills}}",
        generate_skills(data)
    )

    # PROJECTS

    html = html.replace(
        "{{projects}}",
        generate_projects(data)
    )

    # COURSES

    html = html.replace(
        "{{courses}}",
        generate_courses(data)
    )

    # ACHIEVEMENTS

    html = html.replace(
        "{{achievements}}",
        generate_achievements(data)
    )

    # HIGHLIGHTS

    html = html.replace(
        "{{highlights}}",
        generate_highlights(data)
    )

    with open(
        "final_resume.html",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(html)

    print(
        "✅ final_resume.html generated successfully"
    )


if __name__ == "__main__":

    render_resume()