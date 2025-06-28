run:
	set -a && source .env && poetry run streamlit run src/app/main.py

data:
	poetry run python src/data/data.py

graph:
	set -a && source .env && poetry run python src/agents/graph.py