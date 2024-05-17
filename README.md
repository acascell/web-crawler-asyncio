# web-crawler-asyncio
A web crawler using asyncio and NLP


🚀 Overview
The application uses asyncio with the support of aiohttp to crawl web pages asynchronously.
It implements NLP library like textblob to process the content of the web pages using basic NLP models
while parsing the data using BeautifulSoup. TextBlob can determine the polarity and subjectivity of a text. 
The polarity score ranges from -1 (very negative) to 1 (very positive), while the subjectivity score ranges from 0 (very objective) to 1 (very subjective).
The application returns an analysis for the given url proving the polarity and subjectivity of the content.

🔎 TODO
- Enhance using different models like Transformer providing a more sophisticated analysis
- May want to provide a dashboard to display the dta

