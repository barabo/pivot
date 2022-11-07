TRASH := dist __pycache__ .coverage


.PHONY: test  ## run unit tests
test:
	pytest

.PHONY: coverage  ## generate code coverage
coverage:
	coverage run -m pytest
	coverage html
	open htmlcov/index.html

.PHONY: clean  ## delete unused files
clean:
	rm -rf ${TRASH}
