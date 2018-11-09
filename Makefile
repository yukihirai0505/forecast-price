SHELL := /usr/bin/env bash
NAME = "forecast-price"

# http://postd.cc/auto-documented-makefile/
.PHONY: help
help: ## help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build: ## Build fastText
	@unzip csv.zip
