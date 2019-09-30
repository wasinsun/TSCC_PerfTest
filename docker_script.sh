docker build -t <image_name> .
docker run -it --rm -v /<host>/<path>:/usr/src/app --name <container_name> <image_name>