import asyncio
from pyppeteer import launch
async def intercept_network_response(response):
    # In this example, we only care about HTML responses!
    if "text/html" in response.headers.get("content-type", ""):
        # Print some info about the responses
        print("URL:", response.url)
        print("Method:", response.request.method)
        print("Response headers:", response.headers)
        print("Request Headers:", response.request.headers)
        print("Response status:", response.status)
        # Print the content of the response
        print("Content: ", await response.json())
        # NOTE: Use await response.json() if you want to get the JSON directly
async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36')
    await page.goto('https://www.woolworths.com.au')

    page.on('response', lambda response: asyncio.ensure_future(intercept_network_response(response)))
            
    await page.goto('https://www.woolworths.com.au/shop/productdetails/339939')
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())