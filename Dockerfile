FROM node
WORKDIR /app
COPY main.js /app/
RUN npm i
CMD ["node","main.js"]
