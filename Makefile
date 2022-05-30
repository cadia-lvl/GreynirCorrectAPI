build:
	docker build . -t greynircorrect_api
run:
	docker run -d --name=greynircorrect -p 8080:8080 greynircorrect_api
stop:
	docker container stop greynircorrect
	docker container rm greynircorrect
