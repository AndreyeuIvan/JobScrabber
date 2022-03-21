from flask import Flask
from flask_pymongo import PyMongo


app = Flask("JobScrabber")
app.config[
    "MONGO_URI"
] = "mongodb+srv://USER:USER@cluster0.aijn3.mongodb.net/flask_mongo_test?retryWrites=true&w=majority"
mongo = PyMongo(app)
# import pdb;pdb.set_trace()
db_operations = mongo.db.test

db_list = []

search = db_operations.find({"location": "Минск"})
for i in search:
    db_list.append(i)
if db_list:
    print("Exist")
    print(db_list)
else:
    data = [
        {
            "title": "Javascript developer with AWS Experience",
            "company": "УП Инсайтрей",
            "link": "https://rabota.by/vacancy/42041563?query=aws",
            "location": "Минск",
        },
        {
            "title": "DevOps Engineer",
            "company": "ООО АйТиЭф Групп",
            "link": "https://rabota.by/vacancy/41817913?query=aws",
            "location": "Минск",
        },
        {
            "title": "DevOps Engineer",
            "company": " GlobalDots",
            "link": "https://hh.ru/vacancy/42411419?query=aws",
            "location": "Минск",
        },
        {
            "title": "Data Engineer",
            "company": "ООО Зефир Девелопмент / Zephyrmobile",
            "link": "https://rabota.by/vacancy/42400149?query=aws",
            "location": "Минск, Фрунзенская",
        },
        {
            "title": "DevOps Engineer",
            "company": " Qulix Systems",
            "link": "https://rabota.by/vacancy/42444716?query=aws",
            "location": "Минск, Спортивная",
        },
        {
            "title": "Программист Python",
            "company": "ООО Карренси Ком Бел",
            "link": "https://rabota.by/vacancy/42430759?query=aws",
            "location": "Минск",
        },
        {
            "title": "Senior SRE Engineer",
            "company": "ООО Tealium",
            "link": "https://rabota.by/vacancy/42446922?query=aws",
            "location": "Минск",
        },
        {
            "title": "DevOps Support Engineer/Linux Administrator",
            "company": " SoftTeco",
            "link": "https://rabota.by/vacancy/42429405?query=aws",
            "location": "Минск",
        },
        {
            "title": "DevOps Engineer (Development)",
            "company": " Oxagile",
            "link": "https://rabota.by/vacancy/41779084?query=aws",
            "location": "Минск",
        },
        {
            "title": ".NET Developer",
            "company": " HiQo Solutions",
            "link": "https://rabota.by/vacancy/42413944?query=aws",
            "location": "Минск",
        },
        {
            "title": "Middle SRE Engineer",
            "company": "ООО Tealium",
            "link": "https://rabota.by/vacancy/42447018?query=aws",
            "location": "Минск",
        },
        {
            "title": ".NET Developer",
            "company": "ООО Д8 Финансовые Технологии",
            "link": "https://rabota.by/vacancy/42412505?query=aws",
            "location": "Минск, Грушевка",
        },
        {
            "title": "Middle Java Developer",
            "company": " SoftTeco",
            "link": "https://rabota.by/vacancy/42447439?query=aws",
            "location": "Минск",
        },
        {
            "title": "Senior Java Engineer",
            "company": "ООО Tealium",
            "link": "https://rabota.by/vacancy/42396193?query=aws",
            "location": "Минск",
        },
        {
            "title": "Middle Java Engineer",
            "company": "ООО Tealium",
            "link": "https://rabota.by/vacancy/42396333?query=aws",
            "location": "Минск",
        },
        {
            "title": "NodeJS Developer",
            "company": " Oxagile",
            "link": "https://rabota.by/vacancy/41148616?query=aws",
            "location": "Минск, Михалово",
        },
        {
            "title": "Full stack developer",
            "company": " Bringit Technologies",
            "link": "https://hh.ru/vacancy/42364442?query=aws",
            "location": "Минск",
        },
        {
            "title": "Golang Developer",
            "company": " Qulix Systems",
            "link": "https://rabota.by/vacancy/41552007?query=aws",
            "location": "Минск, Спортивная",
        },
        {
            "title": "DevOps Engineer",
            "company": "ООО Центр Разработки ПИ ЭС ЭЙ",
            "link": "https://rabota.by/vacancy/39423895?query=aws",
            "location": "Минск",
        },
        {
            "title": "ML Developer/Scientist with Python/Java or DevOps experience (удаленно)",
            "company": "ООО Априори групп",
            "link": "https://rabota.by/vacancy/42467971?query=aws",
            "location": "Минск",
        },
        {
            "title": "Principal Engineer (Ruby/React/AWS)",
            "company": " FORTE Group",
            "link": "https://rabota.by/vacancy/42044292?query=aws",
            "location": "Минск, Грушевка",
        },
        {
            "title": "Python Engineer",
            "company": "ООО Инспекторио Бел",
            "link": "https://rabota.by/vacancy/41176453?query=aws",
            "location": "Минск, Немига",
        },
        {
            "title": "Администратор системный (DevOps)",
            "company": "ОАО Приорбанк",
            "link": "https://rabota.by/vacancy/42245603?query=aws",
            "location": "Минск",
        },
        {
            "title": "Cloud and DevOps / trainee",
            "company": " EPAM Systems, Inc.",
            "link": "https://rabota.by/vacancy/42443627?query=aws",
            "location": "Минск",
        },
        {
            "title": "Python Middle+ Программист",
            "company": "ООО Неро Электроникс",
            "link": "https://rabota.by/vacancy/41484657?query=aws",
            "location": "Минск",
        },
        {
            "title": "Системный администратор / DevOps",
            "company": "ООО Альмус Медиа Бай",
            "link": "https://rabota.by/vacancy/41614025?query=aws",
            "location": "Минск",
        },
        {
            "title": "Java Developer",
            "company": "ИП Васько А. В.",
            "link": "https://rabota.by/vacancy/41733697?query=aws",
            "location": "Минск",
        },
        {
            "title": "DevOps engineer",
            "company": " Tango Me",
            "link": "https://hh.ru/vacancy/41925006?query=aws",
            "location": "Минск",
        },
        {
            "title": "Early Availability Engineer - Network Security",
            "company": "Иностр. п. Check Point",
            "link": "https://rabota.by/vacancy/42227417?query=aws",
            "location": "Минск",
        },
        {
            "title": "Cloud Architect",
            "company": "ООО СТДев",
            "link": "https://rabota.by/vacancy/41813767?query=aws",
            "location": "Минск",
        },
        {
            "title": "Senior Java Developer",
            "company": "ООО Бануба Девелопмент",
            "link": "https://rabota.by/vacancy/39899196?query=aws",
            "location": "Минск, Немига",
        },
        {
            "title": "Junior DevOps Engineer (Microsoft Azure Stack)",
            "company": " Айти Эксперт",
            "link": "https://rabota.by/vacancy/42117889?query=aws",
            "location": "Минск",
        },
        {
            "title": "Ruby Engineer\xa0at Tripledot Studios",
            "company": "ООО Он Зэ Спот Девелопмент",
            "link": "https://rabota.by/vacancy/41182734?query=aws",
            "location": "Минск",
        },
        {
            "title": "Lead Python Engineer at Orca Security",
            "company": "ООО Он Зэ Спот Девелопмент",
            "link": "https://rabota.by/vacancy/42246038?query=aws",
            "location": "Минск",
        },
        {
            "title": "DevOps Engineer (Azure)",
            "company": "ООО КАСТОМЕРТАЙМС",
            "link": "https://rabota.by/vacancy/42202288?query=aws",
            "location": "Минск",
        },
        {
            "title": "Senior Ruby Engineer at Tripledot Studios",
            "company": "ООО Он Зэ Спот Девелопмент",
            "link": "https://rabota.by/vacancy/40581442?query=aws",
            "location": "Минск",
        },
        {
            "title": ".Net Developer",
            "company": "ООО Сампад",
            "link": "https://rabota.by/vacancy/42203989?query=aws",
            "location": "Минск",
        },
        {
            "title": "DevOps Engineer",
            "company": "ООО АКДев Групп",
            "link": "https://rabota.by/vacancy/42443414?query=aws",
            "location": "Минск, Московская",
        },
        {
            "title": "Data Analyst / Data Science",
            "company": "ООО УАНЛАЙТ АППС",
            "link": "https://rabota.by/vacancy/42150054?query=aws",
            "location": "Минск, Немига",
        },
        {
            "title": "Python Developer",
            "company": " Девхаб",
            "link": "https://rabota.by/vacancy/39892371?query=aws",
            "location": "Минск",
        },
        {
            "title": "Backend Technical Lead",
            "company": "ООО Вайзор Геймз",
            "link": "https://rabota.by/vacancy/42373822?query=aws",
            "location": "Минск",
        },
        {
            "title": "Java Developer",
            "company": "ООО КлаудБизнес",
            "link": "https://rabota.by/vacancy/41422844?query=aws",
            "location": "Минск",
        },
        {
            "title": "Python Developer (Программист Python)",
            "company": " Playrix",
            "link": "https://hh.ru/vacancy/42463368?query=aws",
            "location": "Минск",
        },
        {
            "title": "Node.js Developer",
            "company": " Техниксофт",
            "link": "https://rabota.by/vacancy/42348264?query=aws",
            "location": "Минск, Немига",
        },
        {
            "title": "Senior/Lead Java developer",
            "company": "ЗАО Научсофт",
            "link": "https://rabota.by/vacancy/41415753?query=aws",
            "location": "Минск",
        },
        {
            "title": "Senior DevOps Engineer",
            "company": "ООО Изибрэйн",
            "link": "https://rabota.by/vacancy/41408178?query=aws",
            "location": "Минск, Молодежная",
        },
        {
            "title": "DevOps engineer",
            "company": " Altoros Development",
            "link": "https://rabota.by/vacancy/41659110?query=aws",
            "location": "Минск, Кунцевщина",
        },
        {
            "title": "CI/CD Engineer",
            "company": " Viber",
            "link": "https://rabota.by/vacancy/41541702?query=aws",
            "location": "Минск",
        },
        {
            "title": "Machine Learning Engineer",
            "company": " 21vek.by",
            "link": "https://rabota.by/vacancy/42450289?query=aws",
            "location": "Минск",
        },
        {
            "title": "Web-разработчик",
            "company": "ООО Перфект Системс",
            "link": "https://hh.ru/vacancy/41028245?query=aws",
            "location": "Минск",
        },
        {
            "title": "Senior QA engineer (back-end)",
            "company": " Tango Me",
            "link": "https://hh.ru/vacancy/42019032?query=aws",
            "location": "Минск",
        },
        {
            "title": "Back-end разработчик (node.js)",
            "company": "ООО Ниблсофт",
            "link": "https://rabota.by/vacancy/42469941?query=aws",
            "location": "Минск, Октябрьская",
        },
        {
            "title": "Senior DevOps Engineer (Kubernetes)",
            "company": " Exadel",
            "link": "https://rabota.by/vacancy/41712521?query=aws",
            "location": "Минск",
        },
        {
            "title": "AI Support Engineer",
            "company": " DataRobot",
            "link": "https://rabota.by/vacancy/42390868?query=aws",
            "location": "Минск",
        },
        {
            "title": "Full-stack developer",
            "company": "ЗАО Научсофт",
            "link": "https://rabota.by/vacancy/41524265?query=aws",
            "location": "Минск",
        },
        {
            "title": "Lead IT Recruiter",
            "company": "ООО Он Зэ Спот Девелопмент",
            "link": "https://rabota.by/vacancy/41658863?query=aws",
            "location": "Минск",
        },
        {
            "title": ".NET Engineer - Video Experiences, Technology",
            "company": "ООО Дельтатрэ",
            "link": "https://rabota.by/vacancy/42000277?query=aws",
            "location": "Минск",
        },
        {
            "title": "Junior Scala Developer",
            "company": " iTechArt Group",
            "link": "https://rabota.by/vacancy/41675846?query=aws",
            "location": "Минск, Институт Культуры",
        },
        {
            "title": "DevOps engineer",
            "company": " Elilink",
            "link": "https://rabota.by/vacancy/42376171?query=aws",
            "location": "Минск",
        },
        {
            "title": "Senior Backend Engineer (Python) at Via",
            "company": "ООО Он Зэ Спот Девелопмент",
            "link": "https://rabota.by/vacancy/41417310?query=aws",
            "location": "Минск",
        },
        {
            "title": "Tech Lead .Net / Architect",
            "company": "ООО Он Зэ Спот Девелопмент",
            "link": "https://rabota.by/vacancy/41150352?query=aws",
            "location": "Минск",
        },
        {
            "title": "Senior DevOps / Site Reliability Engineer at Via",
            "company": "ООО Он Зэ Спот Девелопмент",
            "link": "https://rabota.by/vacancy/42078529?query=aws",
            "location": "Минск",
        },
        {
            "title": "QA Automation Engineer",
            "company": "ООО AppXite",
            "link": "https://rabota.by/vacancy/42194784?query=aws",
            "location": "Минск, Восток и еще 1 ",
        },
        {
            "title": "Senior System Administrator",
            "company": " Skywind Group",
            "link": "https://rabota.by/vacancy/41850093?query=aws",
            "location": "Минск, Петровщина",
        },
        {
            "title": "Database Engineer, CloudOps",
            "company": " DataRobot",
            "link": "https://rabota.by/vacancy/42381659?query=aws",
            "location": "Минск",
        },
        {
            "title": "Python разработчик",
            "company": " Andersen",
            "link": "https://rabota.by/vacancy/42395837?query=aws",
            "location": "Минск",
        },
        {
            "title": "Frontend разработчик в продуктовую компанию",
            "company": "ООО СтилтСофт Девелопмент",
            "link": "https://rabota.by/vacancy/41793124?query=aws",
            "location": "Минск",
        },
        {
            "title": "Senior PHP Symfony developer. REMOTE",
            "company": "ООО StarOfService",
            "link": "https://hh.ru/vacancy/42358451?query=aws",
            "location": "Минск",
        },
        {
            "title": "Back-End (Node.JS) Engineer",
            "company": " Skywind Group",
            "link": "https://rabota.by/vacancy/41468337?query=aws",
            "location": "Минск, Петровщина",
        },
        {
            "title": "Senior Ruby Developer at Shoptagr",
            "company": "ООО Он Зэ Спот Девелопмент",
            "link": "https://rabota.by/vacancy/40993221?query=aws",
            "location": "Минск",
        },
        {
            "title": "Middle/Senior Python developer",
            "company": "ЗАО Научсофт",
            "link": "https://rabota.by/vacancy/41667623?query=aws",
            "location": "Минск",
        },
        {
            "title": "DevOps specialist",
            "company": " Paralect",
            "link": "https://rabota.by/vacancy/42415921?query=aws",
            "location": "Минск",
        },
        {
            "title": "QA Automation Engineer",
            "company": " 1pt / Уан Поинт",
            "link": "https://rabota.by/vacancy/42396075?query=aws",
            "location": "Минск",
        },
        {
            "title": "Middle/Senior Node.js Developer",
            "company": " instinctools",
            "link": "https://rabota.by/vacancy/42395173?query=aws",
            "location": "Минск",
        },
        {
            "title": "Fullstack Engineer",
            "company": "ООО Он Зэ Спот Девелопмент",
            "link": "https://rabota.by/vacancy/42194347?query=aws",
            "location": "Минск",
        },
        {
            "title": "Senior .NET Developer",
            "company": "ООО Финстек Бел",
            "link": "https://rabota.by/vacancy/41039187?query=aws",
            "location": "Минск, Молодежная",
        },
        {
            "title": "Front-end developer (middle)",
            "company": "ООО Визутех Плейтинг",
            "link": "https://rabota.by/vacancy/42005380?query=aws",
            "location": "Минск",
        },
        {
            "title": "Data Analyst (UA) / Маркетинговый аналитик",
            "company": " Playrix",
            "link": "https://hh.ru/vacancy/42463591?query=aws",
            "location": "Минск",
        },
        {
            "title": "Senior Java Developer for EverC",
            "company": " Ciklum",
            "link": "https://hh.ru/vacancy/41750878?query=aws",
            "location": "Минск",
        },
        {
            "title": "Senior С# Developer",
            "company": " B2Broker Москва",
            "link": "https://hh.ru/vacancy/41813322?query=aws",
            "location": "Минск",
        },
        {
            "title": "Fullstack .Net+React Developer",
            "company": " Nitka Technologies",
            "link": "https://hh.ru/vacancy/42406404?query=aws",
            "location": "Минск",
        },
        {
            "title": "Senior DevSecOPS Specialist",
            "company": "ООО Melsoft Games",
            "link": "https://rabota.by/vacancy/42399070?query=aws",
            "location": "Минск",
        },
        {
            "title": "Frontend Developer",
            "company": "ООО ДЕВСТРИМ",
            "link": "https://rabota.by/vacancy/41096735?query=aws",
            "location": "Минск",
        },
        {
            "title": "Middle / Senior Xamarin developer at Shoptagr",
            "company": "ООО Он Зэ Спот Девелопмент",
            "link": "https://rabota.by/vacancy/42414720?query=aws",
            "location": "Минск",
        },
        {
            "title": "Ruby Developer",
            "company": " Andersen",
            "link": "https://rabota.by/vacancy/42420554?query=aws",
            "location": "Минск",
        },
        {
            "title": "Fullstack Engineer at Soomla",
            "company": "ООО Он Зэ Спот Девелопмент",
            "link": "https://rabota.by/vacancy/42172050?query=aws",
            "location": "Минск",
        },
        {
            "title": "Full Stack Developer",
            "company": " Skywind Group",
            "link": "https://rabota.by/vacancy/42417362?query=aws",
            "location": "Минск",
        },
        {
            "title": "PHP Developer",
            "company": " 1pt / Уан Поинт",
            "link": "https://rabota.by/vacancy/42395890?query=aws",
            "location": "Минск",
        },
        {
            "title": "Mid/Senior Java Developer",
            "company": "ООО Центр Разработки ПИ ЭС ЭЙ",
            "link": "https://rabota.by/vacancy/42333608?query=aws",
            "location": "Минск",
        },
        {
            "title": "Senior Ruby on Rails Developer",
            "company": " Exadel",
            "link": "https://rabota.by/vacancy/42450391?query=aws",
            "location": "Минск",
        },
        {
            "title": "Senior Big Data Developer (Scala)",
            "company": " Exadel",
            "link": "https://rabota.by/vacancy/42447084?query=aws",
            "location": "Минск",
        },
        {
            "title": "Senior Software Development Engineer in Test, Engineering Productivity",
            "company": " DataRobot",
            "link": "https://rabota.by/vacancy/42381509?query=aws",
            "location": "Минск",
        },
        {
            "title": "Middle Java Software Engineer (net2phone)",
            "company": "ООО IDT Technologies",
            "link": "https://rabota.by/vacancy/42411059?query=aws",
            "location": "Минск, Первомайская и еще 1 ",
        },
        {
            "title": "Front-end Developer",
            "company": "ООО ИТС Партнёр",
            "link": "https://rabota.by/vacancy/41703531?query=aws",
            "location": "Минск",
        },
        {
            "title": "Full Stack Developer for EverC",
            "company": " Ciklum",
            "link": "https://hh.ru/vacancy/41750845?query=aws",
            "location": "Минск",
        },
        {
            "title": "Middle / Senior BackEnd developer",
            "company": "ООО Он Зэ Спот Девелопмент",
            "link": "https://rabota.by/vacancy/40581434?query=aws",
            "location": "Минск",
        },
        {
            "title": "Lead Java Developer",
            "company": " Godel Technologies Europe",
            "link": "https://rabota.by/vacancy/41711257?query=aws",
            "location": "Минск",
        },
        {
            "title": "Full-stack Lead Developer",
            "company": " Itransition",
            "link": "https://rabota.by/vacancy/42256384?query=aws",
            "location": "Минск",
        },
        {
            "title": "Lead DevOps Engineer (Azure)",
            "company": " Exadel",
            "link": "https://rabota.by/vacancy/42447421?query=aws",
            "location": "Минск",
        },
        {
            "title": "Senior .NET Developer",
            "company": " Belitsoft",
            "link": "https://rabota.by/vacancy/42457233?query=aws",
            "location": "Минск",
        },
    ]
    x = db_operations.insert_many(data)
    print("ids of inserted documents\n---------------------")
    for id in x.inserted_ids:
        print(id)


"""
for i in db_operations.find():
	print(i)
"""

"""
@app.route('/report')
def report():
	keyword = request.args.get('keyword')
	if keyword is not None:
		keyword = keyword.lower()
		getDB = db_.get(keyword)
		getDBope = db_operations.find(keyword)
		print(getDBope)
		if getDB:
			jobs = getDB
		else:
			jobs = get_jobs(keyword)
			db_[keyword] = jobs
			#import pdb;pdb.set_trace()
			jobs_new = id_insert(jobs)
			x = db_operations.insert_many(jobs_new)
			for i in x.inserted_ids:
				print(i)
		print(jobs)
	else:
		return redirect('/')
	return render_template('report.html', searchBy=keyword, resultsNumber=len(jobs), jobs=jobs)
"""
