# 📚 **Communities Web App**

This is a **web application** built with **Python, Django**, **HTML**, **CSS**, and **JavaScript** that allows users to create and participate in communities based on various interests such as hobbies, study groups, and job-related topics. Users can join these communities, create posts, leave comments, and update their profiles.

For example, in a **Django community**, a user might post an issue they face (e.g., trouble installing the Django framework). Other members of the community, who are subscribed, can view and help by leaving comments to provide solutions.

---

## ⚙️ **Features**

- **User Authentication**  
  - Create an account  
  - Login and logout  
  - Update your profile  
  - Password recovery (email-based)
  
- **Community Management**  
  - Create communities for hobbies, study groups, work, etc.  
  - Subscribe and unsubscribe from communities  
  
- **Post and Commenting**  
  - Create posts in subscribed communities  
  - Comment on posts (only allowed for subscribed members)  
  - Read more option for detailed posts
  
---

## 🚀 **Technologies Used**

- **Python**: Programming language used to build the app.  
- **Django**: Web framework for building the backend and logic.  
- **HTML**: For creating the web page structure.  
- **CSS**: For styling the web pages and layout.  
- **JavaScript**: For frontend functionality (such as dynamic interactions).  
- **PostgreSQL**: Database to store user information, posts, comments, and community data.  
- **Email**: For sending password recovery emails.

---

## 📝 **Setup Instructions**

### 1. **Clone the repository**
Clone the project from GitHub:

```bash
git@github.com:derleysoares94/social_media.git
cd social-media
```

### 2. **Install Dependencies**
Install the necessary packages using `pip`:

```bash
pip install -r requirements.txt
```

### 3. Setup PostgreSQL Database
Ensure PostgreSQL is installed and running. Create a new database for the application.

Update DATABASES in settings.py to reflect your database credentials.

For example:

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',  # Or your database host
        'PORT': '5432',
    }
}
```

### 4. Run Migrations
Run the migrations to set up the database:

```bash
python manage.py migrate
```

### 5. Create a Superuser (optional)
You can create a superuser to access the Django admin panel:

```bash
python manage.py createsuperuser
```
Open a browser and go to http://127.0.0.1:8000/ to see the app in action.

### 🧑‍💻 How to Use the Web App
Sign Up / Log In
- Go to the homepage and create an account.
- After registration, log in and access your profile, communities, and posts.
### Create Communities
- As an authenticated user, create new communities for various topics (e.g., hobbies, work).
### Join/Leave Communities
- Once logged in, subscribe to communities that interest you and unsubscribe at any time.
### Create Posts
- Only subscribed users can create posts within a community.
- After joining a community, you can create posts and share them with other members.
### Leave Comments
- Comment on posts to help other users by providing solutions or engaging in discussions.
- Only subscribed users are allowed to comment.
### Password Recovery
- Forgot your password? Use the password recovery feature to reset it via email.
