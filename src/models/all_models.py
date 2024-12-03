from sqlalchemy import Column, Integer, String, LargeBinary
from config.database import db

class Image(db.Model):
    __tablename__ = "images"
    
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(100), nullable=False,unique=True)
    content_type = Column(String(50), nullable=False)
    size = Column(Integer, nullable=False)
    data = Column(LargeBinary, nullable=False)  # Store the image binary data

    def to_dict(self):
        return {
            "id": self.id,
            "filename": self.filename,
            "content_type": self.content_type,
            "size": self.size
        }
