from flask import request,Response,json
from services.user_role_service import upload_image, get_image, delete_image
from config.database import db

def upload():
    if 'file' not in request.files:
        return {"error": "No file part"}, 400
    
    file = request.files['file']

    if file.filename == '':
        return {"error": "No selected file"}, 400
    response, status = upload_image(db.session, file)
    return Response(response=json.dumps(response), status=status, mimetype='application/json')

def get_image_route(image_id):
    return get_image(db.session, image_id)  # Pass the current session

def delete_image_route(image_id):
    response, status = delete_image(db.session, image_id)
    return Response(response=json.dumps(response), status=status, mimetype='application/json')
