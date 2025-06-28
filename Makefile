.PHONY: up

run:
	cd app && make run

up:
	docker-compose up --detach --build