# Flask REST API Devolopment

This project is a simple CRUD (Create, Read, Update, Delete) application built with Flask and MongoDB, designed to manage a users database. It provides basic functionalities to interact with user data through the following API endpoints:

- **GET /users**: Returns a list of all users in the database.

- **GET /users/\<id\>**: Returns the user with the specified ID.

- **POST /users**: Creates a new user with the specified data.

- **PUT /users/\<id\>**: Updates the user with the specified ID with the new data.

- **DELETE /users/\<id\>**: Deletes the user with the specified ID.

These endpoints allow you to perform essential operations on user data.


## Table of Contents
- [Project Description](#project-description)
- [Prerequisites](#prerequisites)
  - [Running with Python (without Docker)](#running-with-python-without-docker)
  - [Running with Docker](#running-with-docker)
- [Getting Started](#getting-started)
  - [Cloning the GitHub Repository](#cloning-the-github-repository)
  - [Activate Virtual Environment (Optional)](#activate-virtual-environment-optional)
  - [Install Project Dependencies](#install-project-dependencies)
  - [Get MongoDB Credentials](#get-mongodb-credentials)
  - [Create a .env File](#create-a-env-file)
  - [Run Flask Server](#run-flask-server)
  - [Access the Flask Application](#access-the-flask-application)
- [Run the Flask Application with Docker](#run-the-flask-application-with-docker)
  - [Prerequisites](#prerequisites-1)
  - [Create a .env File](#create-a-env-file)
  - [Building the Docker Image](#building-the-docker-image)
  - [Running the Docker Container](#running-the-docker-container)
  - [Access the Flask Application](#access-the-flask-application-1)
- [Usage](#usage)

## Project Description

The project utilizes Flask, a lightweight Python web framework, to simplify web application development, handling routing, and request processing efficiently. MongoDB, a NoSQL database, stores user data in a flexible JSON-like format, making it ideal for accommodating varying user attributes. Docker containerization ensures consistent deployment across different environments, simplifying the setup process and reducing compatibility issues. Together, these technologies enable the creation of a basic CRUD (Create, Read, Update, Delete) application for managing a user database, providing a solid foundation for web development with Python and MongoDB, while also allowing for future expansion and customization.

## Prerequisites

### Running with Python (without Docker)
- **Python 3.x**: Required for running the Flask application.
- **Flask**: As the web framework used in your project.
- **MongoDB**: If you're using MongoDB as the database.

### Running with Docker
- **Docker**: Since Docker containers include all necessary dependencies, including Python, when running the application in a Docker container.
- **MongoDB**: If you're using MongoDB as the database.

## Getting Started

To run flask application with docker skip to [Run the Flask Application with Docker](#run-the-flask-application-with-docker).

### Cloning the GitHub Repository

To get the project source code, you can clone the GitHub repository:

```bash
git clone https://github.com/irfanrasheedkc/Flask-Rest-API-Development
cd Flask-Rest-API-Development
```

### Activate the Virtual Environment (Optional)

- On Windows:

  ```bash
  venv\Scripts\activate
  ```

- On macOS or Linux:

    ```bash
    source venv/bin/activate
    ```

### Install Project Dependencies
To install the required Python packages for this project, use pip inside your virtual environment:
```bash
pip install -r requirements.txt
```

### Get MongoDB credentials

Get the MongoDB URI: You will need a MongoDB URI to connect to your database. You can obtain a MongoDB URI by signing up for a MongoDB Atlas account or setting up a local MongoDB server.

### Create a .env file: 
In the project directory, create a .env file and add the following content:

```envrc
MONGO_USERNAME=<mognodb_username>
MONGO_PASSWORD=<mongodb_password>
```

### Run flask server
Run the flask server
```bash
python app.py
```

### Access the flask application
Your Flask application should now be running inside a virtual environment. You can access it by opening a web browser and going to:
```html
http://localhost:3000/
```

## Run the Flask Application with Docker

You can also run the Flask application using Docker. Docker allows you to encapsulate your application and its dependencies within a container for easy deployment.

### Prerequisites

Before running the application with Docker, make sure you have Docker installed on your system. You can download and install Docker from the [official Docker website](https://www.docker.com/get-started).

### Building the Docker Image

1. Navigate to the root directory of your project, where your `Dockerfile` is located.

2. Build the Docker image by running the following command (don't forget the period at the end, which specifies the current directory):

   ```bash
   docker build -t flask-rest-api .

This command builds a Docker image with the tag "flask-rest-api.

### Create a .env file: 
In the project directory, create a .env file and add the following content:

```envrc
MONGO_USERNAME=<mognodb_username>
MONGO_PASSWORD=<mongodb_password>
```

### Running the Docker container
Once the Docker image is built, you can run a Docker container from it:
```bash
docker run -p 3000:3000 -d flask-rest-api
```
- The -p 3000:3000 flag maps port 3000 from the container to port 3000 on your host system.

- The -d flag runs the container in detached mode.

### Access the flask application
Your Flask application should now be running inside a Docker container. You can access it by opening a web browser and going to:
```html
http://localhost:3000/
```

## Usage

### Using the API Endpoints

Once your Flask application is running, you can use the provided API endpoints to interact with the user database.