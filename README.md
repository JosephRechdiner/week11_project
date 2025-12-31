# Contact Project k8s

## Purpose
The final purpose of the project is to allow clients to save their contacts in a MongoDB database through their localhost using FastAPI.
All orgenized by Kubernetes!

## Setup
The setup is very simple:

1. Open your terminal.
2. Make a directory for the program.
3. Clone the GitHub repository:
   ```bash
   git clone https://github.com/JosephRechdiner/week11_project.git
   ```
4. Change into the project directory:
   ```bash
   cd week11_project
   ```
5. Start minikube:
   ```bash
   minikube start
   ```
6. Change terminal and type:
   ```bash
   kubectl apply -f ./k8s
   ```
7. Then type:
   ```bash
   minikube service fastapi
   ```

The program is now running!    
- Add `/docs` to the URL if you want to use FastAPI Swagger to test the routes.


## Database Connection Info
We need to initialize a connection to the database and use it every time we want to operate on it.

- `app/database` directory
  - `connector.py` — contains one class to connect Mongo and get db and collection names.

FastAPI has a special method called `Depends()`, which activates the function it receives and initializes the result into a variable. FastAPI also waits for the result before continuing execution.

## App Container Info
The project is divided into three layers:

1. **Application Layer (`routes` directory)**  
   Responsible for creating FastAPI routes visible to the user and sending requests to the service layer.  
   Routes:
   - `GET /` — get all contacts
   - `POST /` — add contact
   - `PUT /` — update contact
   - `DELETE /` — delete contact 

   HTTP exceptions will be raised if needed.

2. **Service Layer (`service` directory)**  
   Responsible for sending requests to the DAL layer to perform CRUD operations and returning appropriate responses:  
   - Status code 200 — returns relevant data
   - Status code 404 — contact not found in the database
   - Status code 409 — database access failed

3. **DAL Layer (`dal` directory)**  
   Responsible for making CRUD operations and returning boolean values to indicate success.

## DB Container Info
Built from the official mongo image.

