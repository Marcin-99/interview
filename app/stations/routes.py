from flask import render_template, flash, url_for, redirect, jsonify, Blueprint
from app import db
from app.stations.utilities import is_int, is_float, look_for_duplicates
from app.stations.forms import StationForm, DeleteForm, UpdateForm
from app.models import Station
from sqlalchemy import update
from datetime import datetime
from app.stations.schemas import StationSchema

stations = Blueprint('stations', __name__)


'''Route responsible for adding records.'''
@stations.route('/', methods=['POST', 'GET'])
@stations.route('/addstation', methods=['POST', 'GET'])
def addstation():
    form = StationForm()
    validation_data = [form.coor_lat_input.data, form.coor_lng_input.data, form.kWh_price_input.data]

    if form.validate_on_submit():
        if is_int(form.id.data) and is_float(validation_data) and look_for_duplicates(form.id.data) == False:
            new_station = Station(id=form.id.data, coor_lat=form.coor_lat_input.data,
                            coor_lng=form.coor_lng_input.data, kWh_price=form.kWh_price_input.data)
            db.session.add(new_station)
            db.session.commit()
            db.session.close()
            flash('Station added succesfully.')

        elif is_int(form.id.data) and look_for_duplicates(form.id.data):
            flash(f'There already is a station with id "{form.id.data}" in database.')

        else:
            flash('All inputs should be numbers.')

        return redirect(url_for('stations.addstation'))

    return render_template('addstation.html', form=form)


'''Route responsible for updating and deleting records.'''
@stations.route('/allstations', methods=['POST', 'GET'])
def allstations():
    delete_form = DeleteForm()
    update_form = UpdateForm()
    validation_data = [update_form.coor_lat_new.data, update_form.coor_lng_new.data, update_form.kWh_price_new.data]
    Stations = Station.query.all()

    if delete_form.submit.data and delete_form.validate():
        if is_int(delete_form.st_id.data) and look_for_duplicates(delete_form.st_id.data):

            station_to_delete = Station.query.filter_by(id=delete_form.st_id.data).first()
            local_object = db.session.merge(station_to_delete)
            db.session.delete(local_object)
            db.session.commit()
            db.session.close()

            flash(f'Station with id "{delete_form.st_id.data}" deleted.')
            return redirect(url_for('stations.allstations'))

        elif is_int(delete_form.st_id.data) and look_for_duplicates(delete_form.st_id.data) == False:
                flash(f'There is not station with id "{delete_form.st_id.data}" in database.')
                return redirect(url_for('stations.allstations'))

        else:
            flash(f'ID must be an integer.')
            return redirect(url_for('stations.allstations'))


    if update_form.submit_2.data and update_form.validate():
        if is_int(update_form.station_id.data) and is_float(validation_data) \
            and look_for_duplicates(update_form.station_id.data):

            station_to_update = Station.query.filter_by(id=update_form.station_id.data).first()
            if update_form.coor_lat_new.data:
                station_to_update.coor_lat = update_form.coor_lat_new.data
            if update_form.coor_lng_new.data:
                station_to_update.coor_lng = update_form.coor_lng_new.data
            if update_form.kWh_price_new.data:
                station_to_update.kWh_price = update_form.kWh_price_new.data

            new_modification_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            station_to_update.date_modified = new_modification_date

            db.session.merge(station_to_update)
            db.session.commit()
            db.session.close()

            flash(f'Station with id "{update_form.station_id.data}" updated.')
            return redirect(url_for('stations.allstations'))

        elif is_int(update_form.station_id.data) and is_float(validation_data) \
            and look_for_duplicates(update_form.station_id.data) == False:
            flash(f'There is not station with id "{update_form.station_id.data}" in database.')
            return redirect(url_for('stations.allstations'))

        else:
            flash(f'Every input must be a number.')
            return redirect(url_for('stations.allstations'))

    return render_template('allstations.html', Stations=Stations, delete_form=delete_form, update_form=update_form)


'''Route responsible for returning json for all resources on request.'''
@stations.route('/stations')
def json():
    data = Station.query.all()
    data_schema = StationSchema(many=True)
    output = data_schema.dump(data)

    return jsonify({'stations' : output})


'''Route responsible for single resource json on request (with given ID).'''
@stations.route('/stations/id=<int:station_id>')
def single_resource_json(station_id):
    data = Station.query.filter_by(id=station_id).first()
    data_schema = StationSchema()
    output = data_schema.dump(data)

    return jsonify({'station' : output})