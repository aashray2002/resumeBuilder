from playwright.sync_api import sync_playwright
import os


def html_to_pdf():

    html_path = os.path.abspath("final_resume.html")
    pdf_path = os.path.abspath("resume.pdf")

    with sync_playwright() as p:

        browser = p.chromium.launch()

        page = browser.new_page()

        page.goto(
            f"file:///{html_path.replace('\\', '/')}"
        )

        page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True
        )

        browser.close()

    print("✅ PDF Generated")