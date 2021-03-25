from flask import Flask, config, render_template, request
from datetime import datetime, time

app = Flask(__name__)
app.config.from_pyfile('./config/config.cfg')

@app.route('/')
def home():
    return render_template('default.html', date=app.config["EVENT_DATE"], title=app.config["TITLE"], annual=app.config["ANNUAL"], reglink=app.config["REG_LINK"])


@app.route('/contact/')
def contact():
    return render_template('contact.html', date=app.config["EVENT_DATE"], title=app.config["TITLE"], annual=app.config["ANNUAL"], reglink=app.config["REG_LINK"])


@app.route('/404.html')
def notfound():
    return render_template('404.html', date=app.config["EVENT_DATE"], title=app.config["TITLE"], annual=app.config["ANNUAL"], reglink=app.config["REG_LINK"])


@app.route('/privacy/')
def privacy():
    return render_template('privacy.html', date=app.config["EVENT_DATE"], title=app.config["TITLE"], annual=app.config["ANNUAL"], reglink=app.config["REG_LINK"])

@app.route('/waiver/')
def waiver():
    return render_template('waiver.html', date=app.config["EVENT_DATE"], title=app.config["TITLE"], annual=app.config["ANNUAL"], reglink=app.config["REG_LINK"])


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, use_reloader=True)