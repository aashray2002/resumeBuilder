from prompt_generator import prompt_generate
from gemini_sender import send_to_gemini
from render_resume import render_resume
from generate_pdf import html_to_pdf


def main():

    print("=" * 50)
    print("STEP 1: Generating Prompt")
    print("=" * 50)

    prompt_generate()

    print("=" * 50)
    print("STEP 2: Sending Prompt To Gemini")
    print("=" * 50)

    send_to_gemini()

    # IMPORTANT
    # send_to_gemini() ke andar hi:
    # 1. Gemini response wait karo
    # 2. JSON copy karo
    # 3. optimized_resume.json save karo

    print("=" * 50)
    print("STEP 3: Rendering Resume HTML")
    print("=" * 50)

    render_resume()

    print("=" * 50)
    print("STEP 4: Generating PDF")
    print("=" * 50)

    html_to_pdf()

    print("=" * 50)
    print("✅ COMPLETE PROCESS FINISHED")
    print("=" * 50)
    print("Output Files:")
    print("1. optimized_resume.json")
    print("2. final_resume.html")
    print("3. resume.pdf")
    print("=" * 50)


if __name__ == "__main__":
    main()