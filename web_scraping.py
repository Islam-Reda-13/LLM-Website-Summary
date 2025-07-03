import requests
from bs4 import BeautifulSoup


class website:
    def __init__(self, url: str):
        self.url = url
        response = requests.get(url)
        self.body = response.content
        soup = BeautifulSoup(self.body, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(['script', 'style','input', 'img']):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator='\n', strip=True)


    def get_content(self) -> str:
        return f"website title:\n {self.title}\n webpage content: \n {self.text}\n\n"    