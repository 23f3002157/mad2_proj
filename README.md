
# Modern Application Development Project - 2


Welcome to the mad2_proj repository! This project is part of the Modern Application Development 2 (MAD2) course offered by IIT Madras as part of its online BS program in Data Science & Applications. The repository contains a practical implementation designed to demonstrate key concepts in modern application development using a combination of technologies including Vue.js, Flask, Redis, and Celery.

## Tech Stack

**Web Frontend:** Built with Vue.js for a responsive and interactive user interface.

**Backend API:** Implemented using Flask to handle server-side logic and API endpoints.

**Task Queue:** Utilizes Celery for asynchronous task processing, integrated with Redis as the message broker.

**Data Management:** Initial data setup scripts to populate the application with sample data.



## Pre-requisites

Before running the project, ensure you have the following installed on your system:

Python 3.6 or higher
Node.js and npm
Redis Server
Virtual environment (e.g., virtualenv)


## Installation


Clone the Repository
git clone https://github.com/23f3002157/mad2_proj.git

```bash
  cd mad2_proj
```



Set Up the Virtual Environment
```bash
python -m venv venv1
source venv1/bin/activate  # On Windows use: venv1\Scripts\activate
```

Install Dependencies
```
For the Python backend:
pip install -r requirements.txt
```

For the Vue.js frontend:
```
npm install
```

Running the Application

Follow these steps to start the application:

Start the Redis Server
```
redis-server
```

Run the Flask Backend
```
python3 app.py
```


Start the Celery Beat Service
```
celery -A app.celery beat --loglevel=info
```


Start the Celery Worker
```
celery -A main:celery_app worker --loglevel INFO --uid=redisuser
```

Launch the Vue.js Frontend
```
npm run dev
```

    
## Acknowledgements

The application should now be accessible at http://localhost:8080 (or the port specified by Vue.js).

Project Structure

```
backend/: Contains Flask application files and Python scripts.
frontend/: Houses the Vue.js project files.
```




## Contributing
This repository is primarily for educational purposes. However, contributions are welcome! Please fork the repository and submit pull requests for any enhancements or bug fixes. Ensure you follow the existing code style and include tests where applicable.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
## Acknowledgments

Thanks to IIT Madras for providing the MAD2 course framework.
Inspired by various open-source projects and tutorials on Vue.js, Flask, Redis, and Celery integration.



## Usage

Navigate to the frontend URL to interact with the application.
The backend handles API requests, while Celery manages asynchronous tasks such as data processing or notifications.
Use the initial data scripts to populate the application with test data for exploration.
