import requests
from bs4 import BeautifulSoup

class Scraper():
	def __init__(self) -> None:
		self.session = self._get_session()

	def _get_session(self):
		'''
		Private method to create a requests.Session object with configured attributes.
		steampowered.com will likely not approve of the package's default user-agent, so a Firefox string has been used.
		'''
		session = requests.Session()
		session.headers = {
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
		}

		return session

	def get_latest_title(self):
		response = self.session.get('https://store.steampowered.com/explore/new/')
		soup = BeautifulSoup(response.text, 'html.parser') # instantiating the BeautifulSoup class

		# finding the page's division for the top-selling titles
		top_seller_divs = soup.findAll(class_='peeking_carousel store_horizontal_autoslider store_capsule_container_scrolling bucket_contents')

		# iterating this div for the children nodes whose data is desired
		for div in top_seller_divs:
			hyperlinks = div.findAll('a')
			print(f'{len(hyperlinks)} New Top Sellers\n') # len of hyperlinks object is equivalent to the quantity of titles found

			for elem in hyperlinks:
				price = elem.find('div', {'class': 'discount_final_price'}).text # text attr stores the raw price string of the title
				print(f"{elem['href']} - {price}") # href value is the referenced link to the current title being iterated

scraper = Scraper()
scraper.get_latest_title()
