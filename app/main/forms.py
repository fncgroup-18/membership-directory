from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, URL, Optional

class CompanyForm(FlaskForm):
    name = StringField('Company Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    industry = StringField('Industry')
    website = StringField('Website', validators=[Optional(), URL()])
    address = StringField('Address')
    phone = StringField('Phone')
    submit = SubmitField('Save')

class SearchForm(FlaskForm):
    query = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Search')
