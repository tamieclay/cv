

CV Management System

This project is a comprehensive User Management System built with Django, a high-level Python Web framework. The system is designed to handle user authentication, authorization, and profile management in a secure and efficient manner.

## Key Features

- **User Registration**: The system allows users to create an account by providing their personal details. Each user is required to have a unique username and email. The registration process involves form validation and error handling to ensure data integrity.

- **User Authentication**: The system provides a secure login mechanism. Users can log in to their account using their email and password. The system validates the credentials, handles invalid inputs gracefully, and maintains the user session.

- **User Authorization**: The system supports role-based authorization. It distinguishes between regular users and superusers (admins). Superusers have additional privileges such as creating accounts for other users.

- **Profile Management**: Each user has a profile where they can manage their personal information. Users can also upload a profile picture, which is handled securely by the system.

- **CV Management**: The system provides a platform for users to create and manage their CVs. Superusers have the privilege to view all CVs in the system.

- **Admin Dashboard**: Superusers have access to an admin dashboard. The dashboard provides a summary of the system, including user count and CV count. Superusers can manage users and CVs directly from the dashboard. The dashboard also provides analytics data.

## Tech Stack

- **Backend**: The backend of the system is built with Django. Django's built-in authentication system is used for handling user authentication and session management.

- **Database**: The system uses SQLite for data storage. SQLite is the default database provided by Django. It's lightweight and perfect for development and testing.

- **Frontend**: The frontend of the system is built with HTML, CSS, and JavaScript. It's designed to be user-friendly and responsive.

