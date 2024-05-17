import asyncio
import aiohttp
from bs4 import BeautifulSoup
from textblob import TextBlob


async def fetch_page(session, url):
    """Fetch the content of a page using aiohttp.

    :param session: the aiohttp session
    :param url: the URL to fetch
    :return: the content of the page
    """

    async with session.get(url) as response:
        return await response.text()


async def parse_content(html):
    """Parse the content of a page using BeautifulSoup.

    :param html: The HTML page
    :return: the parsed data
    """

    soup = BeautifulSoup(html, 'html.parser')
    # this might change per website check the actual div structure
    review_texts = [review.text for review in soup.find_all('div', class_='text show-more__control')]
    return review_texts


async def analyze_text(texts):
    """Analyze the sentiment of a list of texts using TextBlob.

    :param texts: The parsed data to pass to TextBlob
    :return: a dict including the average polarity and subjectivity, and the detailed sentiments
    """

    sentiments = [TextBlob(text).sentiment for text in texts]
    average_polarity = sum([s.polarity for s in sentiments]) / len(sentiments) if sentiments else 0
    average_subjectivity = sum([s.subjectivity for s in sentiments]) / len(sentiments) if sentiments else 0
    return {
        'average_polarity': average_polarity,
        'average_subjectivity': average_subjectivity,
        'detailed_sentiments': sentiments
    }


async def crawl(url):
    """Crawl a page, parse its content, and analyze the sentiment of the text.

    :param url: the actual url to crawl
    """

    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        texts = await parse_content(html)
        analysis = await analyze_text(texts)
        print(f"Analysis results for {url}: {analysis}")


async def main():
    """Gather all the tasks in the event loop."""

    urls = [
        'URLS_1', 'URLS_2', 'URLS_3'
    ]
    tasks = [crawl(url) for url in urls]
    await asyncio.gather(*tasks)


asyncio.run(main())
