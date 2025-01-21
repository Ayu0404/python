from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, URL


class MovieForm(FlaskForm):
    title = StringField(label='Movie Name', validators=[DataRequired()])
    year = IntegerField(label='Year Released', validators=[
                        NumberRange(min=1900, max=2025)])
    description = StringField(label='Description')
    rating = IntegerField(label='Rating', validators=[
                          NumberRange(min=1, max=10)])
    ranking = IntegerField(label='Ranking')
    review = StringField(label='Review')
    image_url = StringField(label='URL', validators=[URL()])
    submit = SubmitField(label='Add Movie')


class EditMovieRating(FlaskForm):
    rating = IntegerField(label='Updated Rating', validators=[
                          NumberRange(min=1, max=10)])
    submit = SubmitField(label='Update')
