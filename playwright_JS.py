from playwright.sync_api import sync_playwright

def log_request(request):
    print(f"Request: {request.method} {request.url}")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.on("request", log_request)

    page.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login',
        wait_until='networkidle',
        timeout=60000
    )

    new_text = 'meow'
    page.evaluate(
        """
        (text) => {
        const title = document.getElementById('authentication-ui-course-title-text')
        title.textContent = text
        }
        """,
        new_text
    )
