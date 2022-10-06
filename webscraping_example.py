import requests
from bs4 import BeautifulSoup

class Scraper():
	def __init__(self) -> None:
		self.session = self._get_session()

	def _get_session(self):
		session = requests.Session()
		session.headers = {
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
		}

		return session

	def get_latest_title(self):
		response = self.session.get('https://store.steampowered.com/explore/new/')
		soup = BeautifulSoup(response.text, 'html.parser')

		top_seller_divs = soup.findAll(class_='peeking_carousel store_horizontal_autoslider store_capsule_container_scrolling bucket_contents')

		for div in top_seller_divs:
			hyperlinks = div.findAll('a')
			print(f'{len(hyperlinks)} New Top Sellers\n')

			for elem in hyperlinks:
				price = elem.find('div', {'class': 'discount_final_price'}).text
				print(f"{elem['href']} - {price}")

scraper = Scraper()
scraper.get_latest_title()
