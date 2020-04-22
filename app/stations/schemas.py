from app.models import Station
from app import marshm


class StationSchema(marshm.SQLAlchemyAutoSchema):
    class Meta:
        model = Station
