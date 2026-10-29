PYTHON ?= .venv/bin/python

.PHONY: fetch index ask test eval lint
fetch:
	bash scripts/fetch_repo.sh
index:
	$(PYTHON) -m hopiumcode.cli index
ask:
	$(PYTHON) -m hopiumcode.cli ask "$(Q)"
test:
	$(PYTHON) -m pytest -q
eval:
	$(PYTHON) -m eval.run_eval
lint:
	$(PYTHON) -m ruff check src tests eval
