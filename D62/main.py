from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from CafeForm import CafeForm
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


def getCafes():
    with open('./cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        data = []
        for row in csv_data:
            data.append(row)
        return data


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('./cafe-data.csv', 'a', newline='\n', encoding='utf-8') as file:
            coffeeData = dict(form.coffee.choices).get(form.coffee.data)
            wifiData = dict(form.wifi.choices).get(form.wifi.data)
            powerData = dict(form.power.choices).get(form.power.data)
            newRow = [form.cafe.data, form.location.data, form.open.data,
                      form.close.data, coffeeData, wifiData, powerData]
            writer = csv.writer(file)
            writer.writerow(newRow)

        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    list_of_rows = getCafes()
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
