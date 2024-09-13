class FileStorage:
    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary to store all objects

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects, if it exists"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    # Import the class dynamically
                    from models.base_model import BaseModel  # Import BaseModel
                    cls_name = value['__class__']
                    if cls_name == 'BaseModel':  # Ensure it deserializes to the correct class
                        obj = BaseModel(**value)
                    FileStorage.__objects[key] = obj
