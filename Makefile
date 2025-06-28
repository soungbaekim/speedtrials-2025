.PHONY: up

run:
	cd app && \
	poetry run streamlit run src/app/main.py

up:
	docker-compose up --detach --build