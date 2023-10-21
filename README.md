# Simple Python API

This repository contains a Flask API project primarily intended for study and learning purposes. As I continue to learn and grow in my understanding of Flask and web development, I'll be updating this project to reflect new knowledge, best practices, and improvements.

## Project Overview
This Flask API provides basic CRUD operations for user management. It's designed to demonstrate fundamental concepts of Flask, RESTful API design, and Python development.

## Features
- Basic CRUD operations for users.
- In-memory database for demonstration purposes.
- Error handling and validation.
- Docker integration for containerization.

## Getting Started
### Prerequisites
- Python 3+
- Docker (optional for containerization)

### Installation
1. Clone the repository:
```bash
git clone https://github.com/CleytonBonamigo/simple-python-api.git
cd simple-python-api
```

2. Install the required packages:
```bash
cd examples/flask/in-memory # Or whatever example you want to run
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py --port=1234 # Port is optional
```

### Examples
Explore various examples in the examples directory:
- [Basic](https://github.com/CleytonBonamigo/simple-python-api) - [Post explaining](https://medium.com/@CleytonBonamigo/building-a-flask-api-a-step-by-step-guide-e73345717b52)
    - Basic CRUD operations for users.
    - In-memory database for demonstration purposes.
    - Error handling and validation.
    - Docker integration for containerization.

### Docker Usage

If you prefer to run the application inside a Docker container, where will install everything for you:
```bash
docker-compose up -d
```

## Contributing 

While this project is primarily for personal study, contributions or suggestions are welcome. Feel free to open an issue or submit a pull request.

## License 

This project is open-source and available under the MIT License.

## Future Updates

As I continue my journey in web development and Flask, I plan to update this project with:

- Test coverage.
- Database integration.
- User authentication and authorization.
- Enhanced logging and monitoring.
And more...