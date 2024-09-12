from models.base_model import BaseModel


class Place(BaseModel):
    city_id = ""    # string (city.id)
    user_id = ""    # string (user.id)
    name = ""   # string
    description = ""    # string
    number_rooms = ""   # integer
    number_bathrooms = ""   # integer
    max_guest = ""  # integer
    price_by_night = ""  # integer
    latitude = ""   # float
    longitude = ""  # float
    amenity_ids = []    # list(Amenity.id)
