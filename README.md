TaskTracker: A Full-Stack To-Do List Web Application
Overview: TaskTracker is a full-stack web application designed to help users manage and track their tasks and to-dos efficiently. It provides a user-friendly platform where individuals can create, edit, and delete tasks, ensuring they stay organized and productive. The app includes a user authentication system for a personalized experience, allowing users to log in, manage their tasks, and securely store data.

Key Features:
User Authentication:

Users can sign up for an account, log in, and log out.

Passwords are stored securely (hashed) for safety.

Provides a personalized experience, allowing users to manage only their own tasks.

Task Management:

Users can create new tasks, providing details like the task name and description.

Tasks can be marked as completed or pending.

The app allows users to delete tasks when they're no longer needed.

Task Tracking:

Users can view tasks in different statuses (completed or pending).

The app might allow filtering or sorting tasks based on their status, priority, or due date.

Responsive Design:

The app is built using Tailwind CSS, ensuring that it looks great on both desktop and mobile devices.

Backend and Database Integration:

Built with Flask (Python framework) as the backend.

Uses SQLite as the database for storing user and task data.

Data is stored securely, ensuring a reliable experience across sessions.

Technology Stack:
Frontend:

HTML, CSS (Tailwind CSS): For the layout and design of the app.

JavaScript (Optional): For any interactive features (e.g., task status updates).

Backend:

Flask (Python): Lightweight Python web framework for building web applications.

SQLite: A lightweight database for storing task data and user information.

User Authentication:

Flask extensions like Flask-Login and Flask-WTF for handling authentication and form submissions.

App Structure:
app/init.py:

Initializes the Flask app and registers any necessary blueprints (e.g., auth for authentication, tasks for task-related functionality).

app/auth/ (Blueprint for Authentication):

Handles user sign-up, login, logout, and user session management.

app/tasks/ (Blueprint for Task Management):

Manages the creation, deletion, and updating of tasks.

Displays the list of tasks, sorted by their status (e.g., completed, pending).

app/templates:

Contains HTML templates for different pages (login, registration, dashboard, task listing, etc.).

app/static:

Stores static files like images, CSS, and JavaScript.

User Flow:
User Registration/Log In:

A new user can sign up with a username, email, and password.

After registration, the user can log in with their credentials to access their personalized dashboard.

Task Dashboard:

After logging in, users will be directed to their dashboard, where they can see their tasks listed.

They can create new tasks, edit existing ones, or delete completed tasks.

Task Management:

Users can easily toggle the status of tasks (e.g., from "pending" to "completed").

They can also filter tasks based on status or priority.

Future Enhancements:
Task Deadlines & Reminders: Users could set deadlines for tasks and receive reminders.

Task Priorities: Allow users to set priority levels (e.g., low, medium, high).

Data Export: Users might want to export their tasks as CSV or PDF for offline use.

Purpose of the Project:
TaskTracker is being built as a beginner-friendly full-stack project, offering hands-on experience with:

Flask and backend development

Frontend design with Tailwind CSS

User authentication and session management

Database interaction with SQLite

This project is ideal for learning how to build web applications from scratch and provides a great foundation for future, more complex applications.

