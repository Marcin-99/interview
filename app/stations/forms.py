from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Length


'''Class responsible for adding new stations.'''
class StationForm(FlaskForm):
    id = StringField('<h5>Station ID</h5>', validators=[DataRequired(), Length(min=1, max=10)])
    coor_lat_input = StringField('lat coordinate', validators=[DataRequired(), Length(min=1, max=10)])
    coor_lng_input = StringField('lng coordinate', validators=[DataRequired(), Length(min=1, max=10)])
    kWh_price_input = StringField('1kWh price', validators=[DataRequired(), Length(min=1, max=10)])
    submit = SubmitField('Add station')
    recaptcha = RecaptchaField()


'''Class responsible for deleting existing stations.'''
class DeleteForm(FlaskForm):
    st_id = StringField('<h5>Station ID</h5>', validators=[DataRequired(), Length(min=1, max=10)])
    submit = SubmitField('Delete station')


'''Class responsible for updating existing stations.'''
class UpdateForm(FlaskForm):
    station_id = StringField('<h5>Station ID</h5>', validators=[DataRequired(), Length(min=1, max=10)])
    coor_lat_new = StringField('New lat coordinate')
    coor_lng_new = StringField('New lng coordinate')
    kWh_price_new = StringField('New 1kWh price')
    submit_2 = SubmitField('Update station')