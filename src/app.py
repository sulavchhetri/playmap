import time
import re
import uvicorn
from playwright.async_api import async_playwright
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src import logger
from src.utils import success_return


playwright = None
browser = None

logger.info("Starting the fastapi app.. ")

app = FastAPI()
app.has_browser = False


async def set_browser_instance():
    global playwright
    playwright = await async_playwright().start()
    global browser
    browser = await playwright.chromium.launch(headless=True)
    logger.info("Browser instance and playwright instance is created.")


def identify_google_map_url(url):
    """
        This function is used to identify the network url from the
        various other urls generated by google map
    """
    regex = r'/search\?tbm=map&[.]*'
    pattern = re.compile(regex)
    if bool(re.search(pattern, url)):
        return url
    return None


async def get_map_response_body(response, final_list):
    """
        This function is used to get the response of the request
    """
    if not final_list['url']:
        if url := identify_google_map_url(response.url):
            logger.info("Found from map from playwright")
            final_list['url'] = url
            logger.info("The url is {}", url)
            body = await response.body()
            final_list['response'] = body.decode()


async def process_map(url):
    """
        This function is used to return the response and map response url
        using playwright
    """
    if not app.has_browser:
        logger.info("Entered inside to create a browser instance")
        app.has_browser = True
        await set_browser_instance()
    response_dict = {
        'url': None,
        'response': None
    }
    close_time = 15 + time.time()
    page = await browser.new_page()
    logger.info("The url is received and playwright is opened")
    await page.goto(url)
    def listener_func(response): return get_map_response_body(
        response, response_dict)
    page.on(
        "response", listener_func)
    await page.wait_for_selector('div[role="feed"]')
    while True:
        if response_dict['url']:
            logger.info("Exited after map response from playwright page")
            break

        if time.time() > close_time:
            logger.info("Exited due to time from playwright page")
            break
        time.sleep(0.1)
        await page.evaluate(
            """document.querySelector('div[role="feed"]').scroll(0,70000);""")
    page.remove_listener("response", listener_func)
    await page.close()
    return response_dict


@app.get('/process')
async def process(
    q: str
):
    """
        This function is used to process the queue task
    """
    logger.info("The url receieved from queue handler is {}", q)
    response_data = await process_map(url=q)
    return JSONResponse(content=success_return(response_data))


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True, host="0.0.0.0", port=5000)
