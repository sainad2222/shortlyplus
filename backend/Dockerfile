FROM node:14

WORKDIR /usr/local/app/backend

COPY api api

COPY client client

WORKDIR client

RUN npm install

RUN npm rebuild

EXPOSE 8084

CMD node client.js
