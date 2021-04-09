test:
	@docker-compose up --build --abort-on-container-exit

# Fast write testcase, no need build container again
test-nobuild:
	@docker-compose up --abort-on-container-exit

test-extra:
	@docker-compose -f docker-compose.extra.yml up --build --abort-on-container-exit

# Fast write testcase, no need build container again
test-extra-nobuild:
	@docker-compose -f docker-compose.extra.yml up --abort-on-container-exit
