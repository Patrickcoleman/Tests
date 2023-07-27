import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://google.com')
    await page.screenshot({'path': 'C:/Users/sirpa/Documents/Code/GitRepos/Tests/Webscraper/Screenshots/example.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())