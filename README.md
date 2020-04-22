Live: https://interwiev-process.herokuapp.com/

Endpoint to get json response for all stations: ***/stations***

Endpoint to get json response for a single resource (for example with id=3): ***/stations/id=3***



**Example code:**

requests.get('https://interwiev-process.herokuapp.com/stations/id=3').text

**Example output:**

{
  "station": {
    "coor_lat": 543.0, 
    "coor_lng": 123.543, 
    "date_created": "2020-03-03T21:42:05", 
    "date_modified": "2020-03-03T21:42:05", 
    "id": 3, 
    "kWh_price": 11111.0
  }
}
