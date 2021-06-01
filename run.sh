docker container stop greynircorrect
docker container rm greynircorrect
docker build . -t greynircorrect:example
docker run -d --name=greynircorrect -p 8080:8080 greynircorrect:example
