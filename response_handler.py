import json
import re
import time
from selenium.webdriver.common.by import By


def get_and_save_response(driver):

    print("Waiting for Gemini response...")

    time.sleep(30) 

    try:

        responses = driver.find_elements(
            By.TAG_NAME,
            "message-content"
        )

        if not responses:
            print("No Gemini response found")
            return

        response_text = responses[-1].text

        match = re.search(
            r"```json\s*(.*?)\s*```",
            response_text,
            re.DOTALL
        )

        if match:
            json_text = match.group(1)
        else:
            json_text = response_text

        data = json.loads(json_text)

        with open(
            "optimized_resume.json",
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

        print("✅ optimized_resume.json saved")

    except Exception as e:
        print(f"❌ Error: {e}")