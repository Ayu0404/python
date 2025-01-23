from flask import Flask, jsonify, render_template, request
from Cafe import Cafe, db
import random
app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
API_KEY = 'TopSecretAPIKey'


def create_db():
    with app.app_context():
        db.create_all()
# create_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def randomCafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(random_cafe.to_dict())


# HTTP GET - Read Record
@app.route('/all')
def get_all_cafes():
    cafes = db.session.query(Cafe).all()
    all_cafes = [cafe.to_dict() for cafe in cafes]
    return jsonify(all_cafes)


# Search using GET
@app.route("/search")
def get_cafe_at_location():
    query_location = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=query_location).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify({"response": {"success": "New entry added successfully."}})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update_coffee_price(cafe_id):
    to_update = db.session.query(Cafe).get(cafe_id)
    if to_update:
        to_update.coffee_price = request.args.get('update-price')
        db.session.commit()
        return jsonify({"response": {"success": "Data updated successfully."}})
    else:
        return jsonify({"response": {"error": {"Not Found": "Cafe with given id not found."}}})


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=['DELETE'])
def delete_Cafe(cafe_id):
    api = request.args.get('api-key')
    if api == API_KEY:
        to_delete = db.session.query(Cafe).get(cafe_id)
        if to_delete:
            db.session.delete(to_delete)
            db.session.commit()
            return jsonify({"response": {"success": "Data deleted successfully."}})
        else:
            return jsonify({"response": {"error": {"Not Found": "Cafe with given id not found."}}})
    return jsonify({"response": {"error": "Incorrect api key."}})


if __name__ == '__main__':
    app.run(debug=True)
