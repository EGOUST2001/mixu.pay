from telegram_bsmu_api import *
from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tarif = request.form.get('tarif')
        return redirect(f"/module/{tarif}")
    return render_template("BGMU.html")


@app.route('/module/<tarif>', methods=['GET', 'POST'])
def module(tarif):
    if request.method == 'POST':
        name = request.form.get('name')
        number = request.form.get('number')
        message = f"Заявка на {mess_tarif(tarif)}. Имя: {name}. Номер для связи: {number}"
        text_answer(message)
        return redirect("/")
    return render_template("SendForm.html", tarif="Заказать " + mess_tarif(tarif))


def mess_tarif(tariff):
    if tariff == "300":
        tariff = "Яркое решение за 300"
    if tariff == "600":
        tariff = "Яркое решение за 600"
    if tariff == "800":
        tariff = "Яркое решение за 800"
    if tariff == "1250":
        tariff = "Яркое решение за 1250"
    if tariff == "Заказ обратного звонка":
        tariff = "обратный звонок"
    return tariff


if __name__ == '__main__':
    app.debug = True
    app.run()
