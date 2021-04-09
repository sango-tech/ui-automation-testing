test:
	@docker-compose up --build --abort-on-container-exit

# Fast write testcase, no need build container again
test-nobuild:
	@docker-compose up --abort-on-container-exit
