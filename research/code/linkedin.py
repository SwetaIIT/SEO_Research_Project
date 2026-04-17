#The code is syntactically fine But it is NOT reliable for data extraction, as linkedin keep blocking extraction

!apt-get update
!apt-get install -y \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2

!pip install playwright
!playwright install chromium


import nest_asyncio
nest_asyncio.apply()

from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox"]
        )

        page = await browser.new_page()
        await page.goto("https://example.com")

        content = await page.content()
        print(content)

        await browser.close()

await run()
