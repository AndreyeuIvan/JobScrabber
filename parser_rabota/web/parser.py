from requests import get

from bs4 import BeautifulSoup

ITEMS = 100

HEAD = {
	'Host': 'rabota.by',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36',
	"Accept": "*/*",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": 'keep-alive',
}

def extract_max_page(url):
	rabota_req = get(url, headers=HEAD)
	pages = []
	#Без заголовков работать не будет, в силу защиты зайта. Используя зашоловки, эмитируется запрос и пропускает его
	rabota_soup = BeautifulSoup(rabota_req.text, 'html.parser')
	paginator = rabota_soup.find_all('div', {'data-qa':'pager-block'})
	for page in paginator:
		pages.append(int(page.find('a').text))
	return pages[-1]


def extract_job(html, keyword):
	job_title = html.find('a').text
	job_title = job_title.strip()
	company = html.find('div', {'class':'vacancy-serp-item__meta-info-company'}).find('a').text
	link = html.find('a').get('href')
	location = html.find('span', {'data-qa':'vacancy-serp__vacancy-address'}).text
	return {'title': job_title, 'company': company, 'link':link, 'location':location, 'keyword':keyword}


def extract_hh_jobs(last_page, url, keyword):

	jobs = []

	for page in range(0, last_page):
		print(f'parsing of page {page}')
		res = get(f'{url}&page={page}', headers=HEAD)

		soup = BeautifulSoup(res.text, 'html.parser')

		results = soup.find_all('div', {'class': 'vacancy-serp-item'})

		for result in results:
			job = extract_job(result, keyword)
			jobs.append(job)
	return jobs


def get_jobs(keyword):
	url = f'https://rabota.by/search/vacancy?area=1002&fromSearchLine=true&st=searchVacancy&text={keyword}& items_on_page={ITEMS}'
	max_page = extract_max_page(url)
	jobs = extract_hh_jobs(max_page, url, keyword)
	return jobs
