from requests import get

from bs4 import BeautifulSoup



headers_1 = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}

def extract_job(html):
	job_title = html.find('a').text
	try:
		company = html.find('div', {'class':'vacancies-list-item__company'}).text
		company = company.replace('Удалённо', '')
	except:
		company = 'No data'
	link = 'https://jobs.dev.by' + html.find('a').get('href')
	try :
		salad = html.find('div', {'class':'vacancies-list-item__salary'}).text
	except:
		salad = 'No salad'
	return {'title': job_title, 'company': company, 'link':link, 'salad':salad}


def extract_dev_jobs(keyword):

	url = f'https://jobs.dev.by/?&filter[search]={keyword}'

	jobs = []

	res = get(url, headers=headers_1)

	soup = BeautifulSoup(res.text, 'html.parser')

	results = soup.find_all('div', {'class': 'vacancies-list-item__body js-vacancies-list-item--open'})

	for result in results:
		job = extract_job(result)
		jobs.append(job)

	return jobs

print(extract_dev_jobs('python'))