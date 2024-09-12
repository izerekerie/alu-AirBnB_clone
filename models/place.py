from models.base_model import BaseModel


class Place(BaseModel):
    city_id = ""    # string (city.id)
    user_id = ""    # string (user.id)
    name = ""   # string
    description = ""    # string
    number_rooms = 0   # integer
    number_bathrooms = 0   # integer
    max_guest = 0  # integer
    price_by_night = 0  # integer
    latitude = 0.00   # float
    longitude = 0.00  # float
    amenity_ids = []    # list(Amenity.id)
