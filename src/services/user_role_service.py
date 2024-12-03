import os
from flask import current_app, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from models.all_models import Image
from sqlalchemy.orm import Session

def allowed_file(filename):
    ALLOWED_EXTENSIONS = current_app.config['ALLOWED_EXTENSIONS']
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_image(db: Session, file):
    if not allowed_file(file.filename):
         return {'status': "failed", "statusCode": 400, "message": "File type not allowed"}, 400
        
    
    if file.content_length > current_app.config['MAX_CONTENT_LENGTH']:
        return {'status': "failed", "statusCode": 400, "message": "File too large"}, 400
       
    filename = secure_filename(file.filename)
    if db.query(Image).filter_by(filename=filename).first():
        return {'status': "failed", "statusCode": 400, "message": "Already file exist"}, 400

    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    #This is the final full path where the uploaded file will be saved.
    
    # Save the file data to the filesystem
    file.save(filepath)

    new_image = Image(
        filename=filename,
        content_type=file.content_type,
        size=os.path.getsize(filepath),#size = round(os.path.getsize(filepath) / (1024 * 1024), 2)  # Convert to MB
        data=file.read()
    )

    db.add(new_image)  
    db.commit() 
    
    return {'status': "success", "statusCode": 201,"message": "Image uploaded successfully", "id": new_image.id}, 201
    

def get_image(db: Session, image_id):
    image = db.query(Image).filter(Image.id == image_id).first()
    if not image:
        return jsonify({"error": "Image not found"}), 404
    
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], image.filename)

def delete_image(db: Session, image_id):
    image = db.query(Image).filter(Image.id == image_id).first()
    if not image:
        return {'status': "failed", "statusCode": 404, "message": "Image not found"}, 404
        
    
    # Remove the file from the filesystem
    os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], image.filename))

    db.delete(image)
    db.commit()

    return {'status': "success", "statusCode": 200, "message": "Image deleted successfully"}, 200


"""
file.filename: This retrieves the name of the file uploaded by the user.
secure_filename: A function from the werkzeug.utils module that sanitizes the filename to make it safe for use
in a filesystem.
It removes potentially dangerous characters.
It replaces spaces and special characters with underscores or other safe equivalents.
Prevents directory traversal attacks (e.g., ../../etc/passwd).

file.filename: This retrieves the name of the file uploaded by the user.
secure_filename: A function from the werkzeug.utils module that sanitizes the filename to make it safe for use 
in a filesystem.
It removes potentially dangerous characters.
It replaces spaces and special characters with underscores or other safe equivalents.
Prevents directory traversal attacks (e.g., ../../etc/passwd).

"""