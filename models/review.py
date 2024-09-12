from models import place
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""   # place.id
    user_id = ""    # user.id
    text = ""

