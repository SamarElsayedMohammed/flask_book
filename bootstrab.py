from flask import Flask ,render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
# from flask.wtf import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'


class NameForm(FlaskForm):
    name = StringField('what\'s your name',validators=[DataRequired()])
    submit = SubmitField('submi')



@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
            session['name'] = form.name.data
            form.name.data = ''
            return redirect(url_for('index'))
    return render_template('Bootstrap-based.html',form = form, name = session.get('name'))




# @app.route('/', methods=['GET', 'POST'])
# def index():
    
#     # name = 'samar'
#     form = NameForm()
#     if form.validate_on_submit():
#         session['name'] = form.name.data
#         return redirect(url_for('index'))
#     return render_template('Bootstrap-based.html', form=form, name=session.get('name'))


# @app.route('/')
# def index():
#     return render_template('Bootstrap-based.html')


if __name__ == '__main__':
    app.run(debug=True)


