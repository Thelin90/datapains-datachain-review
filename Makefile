export MINIO_ROOT_USER := admin
export MINIO_ROOT_PASSWORD := admin-123

.PHONY: setup-environment
setup-environment:
	uv lock

.PHONY: get-python-path
get-python-path:
	uv run which python

.PHONY: run
run:
	uv run python run.py

.PHONY: setup-storage
setup-storage:
	kubectl apply -f tools/k8s/local/storage
