import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def send_to_gemini():

    driver = webdriver.Chrome()

    driver.get("https://gemini.google.com/app")

    wait = WebDriverWait(driver, 60)

    # Prompt textbox
    textbox = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                '//*[@id="app-root"]/main/side-navigation-v2/bard-sidenav-container/bard-sidenav-content/div/div/div/chat-window/div/input-container/fieldset/input-area-v2/div/div/div[1]/div/div/div/rich-textarea/div[1]/p'
            )
        )
    )

    textbox.click()

    time.sleep(2)

    # Clipboard se prompt paste
    textbox.send_keys(Keys.CONTROL, "v")

    time.sleep(2)

    textbox.send_keys(Keys.ENTER)

    print("✅ Prompt sent to Gemini")

    # Response generate hone do
    print("⏳ Waiting for Gemini response...")
    time.sleep(45)

    try:

        code_blocks = driver.find_elements(By.TAG_NAME, "code")

        print(f"Found {len(code_blocks)} code blocks")

        if len(code_blocks) == 0:
            raise Exception("No code block found in Gemini response")

        # Largest code block choose karo
        json_text = max(
            [block.text for block in code_blocks],
            key=len
        )

        # Validate JSON
        parsed_json = json.loads(json_text)

        with open(
            "optimized_resume.json",
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(
                parsed_json,
                f,
                indent=4,
                ensure_ascii=False
            )

        print("✅ optimized_resume.json saved successfully")

    except Exception as e:

        print("❌ JSON extraction failed")
        print(e)

        # Debug purpose
        with open(
            "gemini_page_source.html",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(driver.page_source)

        print("⚠ Saved page source to gemini_page_source.html")

    return driver