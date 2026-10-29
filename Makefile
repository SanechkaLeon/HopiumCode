PYTHON ?= .venv/bin/python

.PHONY: index ask test eval lint
index:
	$(PYTHON) -m hopiumcode.cli index
ask:
	$(PYTHON) -m hopiumcode.cli ask "$(Q)"
test:
	$(PYTHON) -m pytest -q
eval:
	$(PYTHON) -m eval.run_eval
lint:
	ruff check src tests eval
