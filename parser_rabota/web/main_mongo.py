from flask import Flask, render_template, request, redirect, send_file
from flask_pymongo import PyMongo

from parser import get_jobs

from export import save_to_csv, id_insert


app = Flask("JobScrabber")
app.config[
    "MONGO_URI"
] = "mongodb+srv://USER:USER@cluster0.aijn3.mongodb.net/flask_mongo_test?retryWrites=true&w=majority"
mongo = PyMongo(app)
db_operations = mongo.db.test

db_ = []


@app.route("/")  # creating url
def home():
    return render_template("home.html")


@app.route("/report")
def report():
    """Get keyword, transform keyword to lower case, check if keyword is in a db, if not create new cluster."""
    keyword = request.args.get("keyword")
    if keyword is not None:
        keyword = keyword.lower()
        getDBope = db_operations.find({"keyword": keyword})
        for i in getDBope:
            db_.append(i)
        if db_:
            jobs = db_
        else:
            jobs = get_jobs(keyword)
            x = db_operations.insert_many(jobs)
            for id_ in x.inserted_ids:
                print(id_)
        print(jobs)
    else:
        return redirect("/")
    return render_template(
        "report.html", searchBy=keyword, resultsNumber=len(jobs), jobs=jobs
    )


@app.route("/export")
def export():
    try:
        keyword = request.args.get("keyword")
        if not keyword:
            raise Exception()
        keyword = keyword.lower()
        jobs = db_.get(keyword)

        if not jobs:
            raise Exception()
        save_to_csv(jobs, keyword)
        return send_file(f"{keyword}.csv")
    except:
        return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
