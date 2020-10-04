docker build . -t test
#this builds from the dockerfile in this directory (hence the '.') and labels the docker images as 'test'

docker run -p 5000:5000 test
#this runs the container and makes localhost:5000 link with localhost:5000 in the app
