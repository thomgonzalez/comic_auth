.PHONY: build_dev
build_dev:
	@docker-compose -f docker-compose.yml build

.PHONY: run_dev
run_dev:
	@docker-compose -f docker-compose.yml up

.PHONY: down
down:
	@docker-compose down
	