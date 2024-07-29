# erp-backend
Django, PostgreSQL and Docker

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

## Setup for development
1. Create python virtual environment
  ```bash
  eval $(pdm venv activate)
  ```
2. Install dependencies for lsp support
  ```bash
  pdm install
  ```
