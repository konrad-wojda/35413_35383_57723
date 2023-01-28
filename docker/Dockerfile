ARG     PYTHON_VER=3.10
ARG     NODE_VER=latest

FROM    node:${NODE_VER} AS build 

WORKDIR /app

COPY    Front-Angular/ /app

RUN     npm install
RUN     npm run build --prod

FROM    nginx:alpine AS nginx

COPY    --from=build /app/dist/front-angular /usr/share/nginx/html

COPY    /docker/nginx.conf  /etc/nginx/conf.d/default.conf

FROM    python:${PYTHON_VER} AS fast-api-back

WORKDIR /app

COPY    Back_FastApi /app

RUN     pip install -r requirements.txt

EXPOSE 8000

CMD     ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]