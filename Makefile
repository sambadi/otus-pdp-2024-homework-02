install:  # установка зависимостей
	poetry install

test: # запуск тестов
	poetry run pytest ./tests

typing: # запуск на исполнение с помощью docker
	docker compose up --build