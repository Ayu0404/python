from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL


class CafeForm(FlaskForm):

    coffeeOptions = [('1', '☕️'), ('2', '☕️☕️'),
                     ('3', '☕️☕️☕️'), ('4', '☕☕☕☕️'), ('5', '☕☕☕☕️☕️')]
    wifiOptions = [('0', '✘'), ('1', '💪'), ('2', '💪💪'), ('3', '💪💪💪'),
                   ('4', '💪💪💪💪'), ('5', '💪💪💪💪💪')]
    powerOptions = [('0', '✘'), ('1', '🔌'), ('2', '🔌🔌'), ('3', '🔌🔌🔌'),
                    ('4', '🔌🔌🔌🔌'), ('5', '🔌🔌🔌🔌🔌')]

    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField(
        'Cafe Location on Google Maps URL', validators=[DataRequired(), URL()])
    open = StringField('Opening Time eg: 8:00AM', validators=[DataRequired()])
    close = StringField('Closing Time eg: 6:00PM', validators=[DataRequired()])
    coffee = SelectField('Coffee Rating', choices=coffeeOptions)
    wifi = SelectField('Wifi Strength Rating', choices=wifiOptions)
    power = SelectField('Power Socket Availability', choices=powerOptions)
    submit = SubmitField('Submit')
