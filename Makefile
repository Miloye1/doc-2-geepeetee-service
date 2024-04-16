start:
	docker compose build
	docker compose up server -d

stop:
	docker compose down