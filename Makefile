lint:
	ruff check .

test:
	pytest -q

run:
	python bot.py
