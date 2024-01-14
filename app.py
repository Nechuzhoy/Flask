from flask import Flask, render_template, request, redirect

from models import db, Adv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///adv.db'
db.init_app(app)


@app.route('/')
def index():
    adv = Adv.query.all()
    return render_template('index.html', adv=adv)


@app.route('/add', methods=['GET', 'POST'])
def add_adv():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        owner = request.form['owner']
        adv = Adv(title=title, description=description, owner=owner)
        db.session.add(adv)
        db.session.commit()
        return redirect('/')
    return render_template('add_adv.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_adv(id):
    adv = Adv.query.get_or_404(id)
    if request.method == 'POST':
        adv.title = request.form['title']
        adv.description = request.form['description']
        adv.owner = request.form['owner']
        db.session.commit()
        return redirect('/')
    return render_template('edit_adv.html', adv=adv)


@app.route('/view/<int:id>')
def view_adv(id):
    adv = Adv.query.get_or_404(id)
    return render_template('view_adv.html', adv=adv)


@app.route('/delete/<int:id>', methods=['POST'])
def delete_adv(id):
    adv = Adv.query.get_or_404(id)
    db.session.delete(adv)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
