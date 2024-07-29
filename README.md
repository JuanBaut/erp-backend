# erp-backend
Django, PostgreSQL and Docker

![image](https://github.com/user-attachments/assets/9ea3895f-eece-4be4-80b0-006224ed5d47)
![image](https://github.com/user-attachments/assets/b195e72e-1097-4f14-a2a6-7449f3776101)


## Dependencies
- docker and docker-compose

## Starting the app
1. Build and run the container
  ```bash
  docker-compose up --build
  ```
2. Open `http://localhost:8000/` to verify that the django app is running
3. After building just run this to start the container and remove older versions of the container
  ```bash
  docker-compose up --remove-orphans
  ```
## Important flows

- Clean up older containers (will delete db entries and migrations must be run again)
  ```bash
  docker stop $(docker ps -aq)
  docker rm $(docker ps -aq)
  docker-compose down -v
  ```
- Run migrations for model changes
  ```bash
  docker-compose run web pdm run makemigrations <app-name>
  ```
- Open the psql shell to make queries
  ```bash
  docker-compose exec db psql -U psql -d psql
  ```

## Setup for development (after docker container setup)
1. Install dependencies for lsp support
  ```bash
  pdm install
  ```
2. Create python virtual environment
  ```bash
  eval $(pdm venv activate)
  ```
