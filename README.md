# Aplikacja trójwarstwowa

(FE Angular, BE FastAPI, DB PostgreSQL/SQLite)

## Aby uruchomić

1. Clone the repository: </br>
   git clone https://github.com/konrad-wojda/aplikacje-bazodanowe.git

2. Navigate to the project directory: </br>
   cd aplikacje-bazodanowe/docker

3. Start the Docker containers: </br>
   docker-compose up

4. Back_FastApi/.env file content</br>

DB_TYPE=postgres </br>
</br>
JWT_SECRET_POSTGRES= </br>
DB_POSTGRES_USER=postgres </br>
DB_POSTGRES_PSWRD=123 </br>
DB_POSTGRES_HOST=postgresql-db </br>
DB_POSTGRES_PORT=5432 </br>
DB_POSTGRES_NAME=IntendantJobDB </br>
`DB_POSTGRES_URI=postgresql://${DB_POSTGRES_USER}:${DB_POSTGRES_PSWRD}@${DB_POSTGRES_HOST}:${DB_POSTGRES_PORT}/${DB_POSTGRES_NAME}`</br>
</br>
JWT_SECRET_LITE = nothingspecialtogetitrightlite </br>
DB_LITE_URI=sqlite:///./database.db </br>
################### </br>
MIN_PASSWORD_LEN = 8 </br>
MAX_EMAIL_LEN = 60 </br>
git clone https://github.com/konrad-wojda/35413_35383_57723.git
