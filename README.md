
# **Flask Image Upload and Management API**

## **Description**

The **Flask Image Upload and Management API** is a RESTful API built using **Flask** that allows users to upload images to a server. The API stores image metadata (such as filename, size, type, and upload time) in a database, providing functionality to retrieve and delete images. The API includes file size validation, security checks, and supports multiple file types. It uses **Flask-SQLAlchemy** for database interactions and supports both **MySQL** and **SQLite** for data storage.



## **Features**

- **Secure File Handling**: Ensures uploaded files are validated for size, type, and integrity.
- **Database Management**: Stores and retrieves image metadata efficiently using **Flask-SQLAlchemy**.
- **Authentication and Authorization**: Protects routes to manage images with user authentication.
- **Modular Code Organization**: Clear separation of concerns with a maintainable folder structure.
- **Configuration Management**: Handles environment-specific settings using **python-dotenv**.
- **Error Handling**: Comprehensive error responses to manage common issues (e.g., invalid file type, unauthorized access).
- **Response Formatting**: Standardized and user-friendly response formats for API endpoints.


## Prerequisites

- Python 3.9+
- pip
- Virtual environment support
## **Libraries Used**

- **Flask** 
- **Flask-SQLAlchemy** 
- **MySQL/SQLite** 
- **python-dotenv** 
- **Werkzeug** 
- **JWT** 



## **Installation and Setup**

### **1. Clone the Repository**

```bash
git clone https://github.com/pavandandla/Flask-Image-Upload-and-Management-API.git
cd Flask-Image-Upload-and-Management-API
```



### **2. Create a Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```



### **3. Install Dependencies**

```bash
pip install -r src/requirements.txt
```



### **4. Configure Environment Variables**

Create a `.env` file in the root directory with the following configuration:

```plaintext
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///./test.db  # Or MySQL connection string
JWT_SECRET_KEY=your_jwt_secret_key
ALLOWED_FILE_EXTENSIONS=jpg,png,gif
MAX_CONTENT_LENGTH=5MB
FLASK_ENV=development
```

- **SECRET_KEY**: Key for signing cookies and sessions.
- **DATABASE_URL**: SQLite or MySQL connection string for storing image metadata.
- **JWT_SECRET_KEY**: Secret key used for encoding JWT tokens.
- **ALLOWED_FILE_EXTENSIONS**: List of acceptable image file extensions.
- **MAX_CONTENT_LENGTH**: Maximum allowed file size for uploads (e.g., 5MB).
- **FLASK_ENV**: Set to `development` for debugging.



### **5. Set Up the Database**

Run the following command to initialize the database and create necessary tables:

```bash
python src/init_db.py
```



### **6. Run the Application**

To run the Flask application:

```bash
flask run
```

The application will be available at: `http://127.0.0.1:5000`



## **Example Workflow**

1. **Image Upload**  
    To upload an image, users can make a `POST` request to the `/upload` endpoint with the image file as part of the request body. The API checks the file type and size, stores it on the server, and saves metadata in the database.
    
2. **Retrieve Image Metadata**  
    To retrieve an image’s metadata, users can make a `GET` request to `/image/<image_id>`. The response includes the file details such as the name, size, and upload date.
    
3. **Delete Image**  
    To delete an image, users can make a `DELETE` request to `/image/<image_id>`. The image will be removed from both the server and the database.
    



## **Environment Configuration**

Example `.env` file:

```plaintext
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///./test.db  # Or MySQL connection string
JWT_SECRET_KEY=your_jwt_secret_key
ALLOWED_FILE_EXTENSIONS=jpg,png,gif
MAX_CONTENT_LENGTH=5MBt
```


## **Contact**

For questions, suggestions, or issues, contact:

- GitHub: [pavandandla](https://github.com/pavandandla)
