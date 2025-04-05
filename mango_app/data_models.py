# mango_app/data_models.py

class MangoItem:
    """Class representing a pest or disease affecting mangoes"""
    
    def __init__(self, id, name, scientific_name, description, image_path, item_type, detailed_info):
        """
        Initialize a MangoItem object.
        
        Args:
            id (int): Unique identifier for the item
            name (str): Common name of the pest or disease
            scientific_name (str): Scientific name of the pest or disease
            description (str): Brief description
            image_path (str): Path to the image file
            item_type (str): Either 'pest' or 'disease'
            detailed_info (str): Detailed information about the pest or disease
        """
        self.id = id
        self.name = name
        self.scientific_name = scientific_name
        self.description = description
        self.image_path = image_path
        self.item_type = item_type
        self.detailed_info = detailed_info
    
    def get_item_type_display(self):
        """Return the display name for the item type"""
        return "Pest" if self.item_type == "pest" else "Disease"
    
    def __str__(self):
        """String representation of the object"""
        return f"{self.name} ({self.get_item_type_display()})"