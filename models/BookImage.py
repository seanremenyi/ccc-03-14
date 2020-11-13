from main import db

class BookImage(db.Model):
    __tablename__ = "book_images"
    
    id = db.Column(db.Integer, primary_key = True)
    filename = db.Column(db.string(), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)
    
    def _repr__(self):
        return f"<BookImage {self.filename}>"