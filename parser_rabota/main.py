'''from headhunter import get_jobs
from save import save_to_csv

hh_jobs = get_jobs()

save_to_csv(hh_jobs)

with open('test.csv', 'w+r') as f:
	print(f.read())'''

from parser_rabota.fast_graber.dev_parser import extract_dev_jobs
from save import save_dev_to_csv


save_dev_to_csv(extract_dev_jobs('python'), 'python')

with open('test.csv', 'r') as f:
	print(f.read())