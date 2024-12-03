from flask import Blueprint
from controllers.user_controller import (
    upload,
    get_image_route,
    delete_image_route
)

# Blueprint for user image routes
user_bp = Blueprint('user_bp', __name__)

# Define routes
user_bp.route('/upload', methods=['POST'])(upload)
user_bp.route('/get-image-route/<int:image_id>', methods=['GET'])(get_image_route)
user_bp.route('/delete-image-route/<int:image_id>', methods=['DELETE'])(delete_image_route)
