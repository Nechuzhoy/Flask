from flask import Flask, request
from models import db, Adv
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///adv.db'
db.init_app(app)
ma = Marshmallow(app)


class AdvSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "description", "owner", "date_of_creation")
        model = Adv


adv_schema = AdvSchema()
advs_schema = AdvSchema(many=True)


@app.route('/api/', methods=['GET'])
def index():
    adv = Adv.query.all()
    return advs_schema.dump(adv)


@app.route('/api/add_adv/', methods=['POST'])
def add_adv():
    new_adv = Adv(
        title=request.json['title'],
        description=request.json['description'],
        owner=request.json['owner']
    )
    db.session.add(new_adv)
    db.session.commit()
    return adv_schema.dump(new_adv)


@app.route('/api/<int:adv_id>', methods=['GET'])
def view_adv(adv_id):
    adv = Adv.query.get_or_404(adv_id)
    return adv_schema.dump(adv)


@app.route('/api/delete/<int:id>', methods=['POST'])
def delete_adv(id):
    adv = Adv.query.get_or_404(id)
    db.session.delete(adv)
    db.session.commit()
    return adv_schema.dump(adv)


@app.route('/api/edit/<int:id>', methods=['PATCH'])
def edit_adv(id):
    edit_adv = Adv.query.get_or_404(id)
    if 'title' in request.json:
        edit_adv.title = request.json['title']
    if 'content' in request.json:
        edit_adv.description = request.json['description']
    if 'content' in request.json:
        edit_adv.owner = request.json['owner']

    db.session.commit()
    return adv_schema.dump(edit_adv)


if __name__ == '__main__':
    app.run(debug=True)
