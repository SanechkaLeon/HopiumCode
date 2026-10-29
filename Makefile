.PHONY: fetch index ask test eval lint
fetch:
	bash scripts/fetch_repo.sh
index:
	python -m hopiumcode.cli index
ask:
	python -m hopiumcode.cli ask "$(Q)"
test:
	python -m pytest -q
eval:
	python -m eval.run_eval
lint:
	ruff check src tests eval
