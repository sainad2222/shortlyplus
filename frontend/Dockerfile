FROM node:14

WORKDIR /usr/local/app/frontend

ENV PATH /app/node_modules/.bin:$PATH

COPY . ./

RUN npm install

CMD ["npm", "start"]
