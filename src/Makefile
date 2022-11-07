MAN := data/share/man/man1
TRASH := .coverage .pytest_cache .tox dist htmlcov


.PHONY: help       ## display the make target descriptions
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@grep -E '^\.PHONY: [a-zA-Z_-]+ .*?## .*$$' $(MAKEFILE_LIST) \
	  | sort \
	  | awk 'BEGIN {FS = "(: |##)"}; {printf "\033[36m%-30s\033[0m %s\n", $$2, $$3}'

.PHONY: black      ## lint the codebase
black:
	black .

.PHONY: test       ## run unit tests
test: black
	pytest

.PHONY: coverage   ## generate code coverage
coverage: test
	coverage run -m pytest

.PHONY: html       ## show the html code coverage report
html: coverage
	coverage html
	open htmlcov/index.html

.PHONY: install    ## install the current pivot module locally
install: test
	flit install

.PHONY: man        ## update the pivot man pages
man: install
	click-man --target ${MAN} pivot
	@ flit install
	man pivot

.PHONY: publish    ## publish the current version to pypi
publish: clean man
	flit publish

.PHONY: clean      ## delete unused files
clean:
	rm -rf ${TRASH} **/__pycache__
