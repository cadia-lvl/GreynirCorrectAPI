docker container stop greynircorrect
docker container rm greynircorrect
docker build . -t glaciersg/greynircorrect_api:v1.0.0
docker run -d --name=greynircorrect -p 8080:8080 glaciersg/greynircorrect_api:v1.0.0
