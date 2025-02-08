#!/usr/bin/python3
"""
BaseModel Class: Defines common attributes and methods for all models.
Acts as the foundation for other classes and integrates with FileStorage.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    A base class that provides:
    - Unique ID generation for each instance.
    - Timestamps for creation and updates.
    - Serialization and deserialization methods.
    - Automatic linking to FileStorage.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance.

        If kwargs are provided (from a dictionary), it reconstructs an instance
        using the dictionary values. Otherwise, it generates a new instance 
        with a unique ID and timestamps.
        """
        if kwargs is not None and len(kwargs) != 0:
            # Remove the '__class__' key if present
            if '__class__' in kwargs:
                del kwargs['__class__']

            # Convert string timestamps back to datetime objects
            kwargs['created_at'] = datetime.fromisoformat(kwargs['created_at'])
            kwargs['updated_at'] = datetime.fromisoformat(kwargs['updated_at'])

            # Assign dictionary values to instance attributes
            self.__dict__.update(kwargs)
        else:
            # Generate a new instance with a unique ID and timestamps
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            # Import storage and register the new instance
            from .__init__ import storage
            storage.new(self)

    def __str__(self):
        """
        Returns a formatted string representation of the instance.
        Format: [ClassName] (id) {instance attributes}
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' timestamp and saves the instance
        to the storage system.
        """
        self.__dict__.update({'updated_at': datetime.now()})
        from .__init__ import storage
        storage.save()

    def to_dict(self):
        """
        Converts the instance into a dictionary format.

        Includes:
        - All instance attributes.
        - The class name as '__class__'.
        - 'created_at' and 'updated_at' as ISO formatted strings.
        """
        instance_dict = dict(self.__dict__)
        instance_dict.update({
            '__class__': type(self).__name__,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'id': self.id
        })
        return instance_dict