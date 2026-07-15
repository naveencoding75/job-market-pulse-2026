FROM node:20-alpine

#Installing Python and building tools inside the container.
RUN apk add --no-cache python3 py3-pip make g++

WORKDIR /app

#Copying package files first to leverage Docker caching.
COPY package*.json ./
COPY scripts/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt --break-system-packages
RUN npm i

COPY . .

RUN npm run build

EXPOSE 3000

CMD ["npm", "run", "start"]