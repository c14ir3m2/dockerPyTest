**two ways to containerize python applications with docker**

**Building the Docker Image**
docker build -t your-image-name .

**Running the Docker Container**
docker run -d -p 9999:9999 your-image-name

**Running the Docker Container**
telnet localhost 9999
