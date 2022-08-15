from flask import Flask, render_template, request, redirect
application = Flask(__name__)


@application.route('/', methods=['GET', 'POST'])
def index():
    return render_template("BGMU.html")


if __name__ == '__main__':
    application.debug = True
    application.run()
