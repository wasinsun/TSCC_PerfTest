docker build -t tscc_single_response_time_test .
docker run -it --rm -v /<host>/<path>:/usr/src/app --name tscc_single_response_time_test tscc_single_response_time_test