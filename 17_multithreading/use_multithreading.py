'''
Read-world example of using multithreading in Python. I/O-bound tasks.
scenario: web scraping, file I/O, network operations.
web scraping: fetching data from multiple web pages concurrently.
These tasks are I/O bound, meaning they spend a lot of time waiting for external resources.
Multithreading can help improve performance by allowing other threads to run while one thread is waiting for I/O operations to complete.
improve the performance by alllowing multiple web pages to be fetched concurrently.


'''

import requests
import threading
url1 = "https://python.langchain.com/docs/introduction/"
url2="https://python.langchain.com/docs/tutorials/"
url3="https://python.langchain.com/docs/how_to/"

# Add a custom User-Agent so Wikipedia allows access
headers = {"User-Agent": "Mozilla/5.0"}
response1 = requests.get(url1, headers=headers)
response2 = requests.get(url2, headers=headers)
response3 = requests.get(url3, headers=headers)
from bs4 import BeautifulSoup

responses=[response1, response2, response3]
def fetch_content(responses):
    for response in responses:
        soup= BeautifulSoup(response.content, "html.parser")
        print(f"Fetched {len(soup.text)} characters from {response.url}")
        print(f"Title: {soup.title.string}")
        
        
        
threads=[]
for response in responses:
    thread=threading.Thread(target=fetch_content, args=([response],))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
#fetch_content(responses)
#fetch_content(responses)
print("All content fetched.")            
