.PHONY: install
install:
	pip install --no-cache-dir .

.PHONY: install-dev
install-dev:
	pip install --upgrade pip
	pip install --no-cache-dir -e .[dev,build,test,lint,doc]

.PHONY: name
name:
	$(eval PATH_NEW := $(shell python3 ./zdevelop/make_scripts/make_name.py $(n)))
	@echo "library renamed! to switch your current directory, use the following \
	command:\ncd '$(PATH_NEW)'"

.PHONY: clean
clean:
	-rm -r .mypy_cache
	-rm -r .pytest_cache
	-rm -r ./zdocs/build
	-rm -r ./build
	-rm -r ./dist
	-find '.' -name '*.pyc' -type f -delete
	-rm .coverage
	-rm -r .idea

.PHONY: test
test:
	-pytest
	sleep 1
	open ./zdevelop/tests/_reports/coverage/index.html
	open ./zdevelop/tests/_reports/test_results.html

.PHONY: lint
lint:
	-flake8
	-black . --diff
	-mypy .

.PHONY: venv
venv:
ifeq ($(py), )
	$(eval PY_PATH := python3)
else
	$(eval PY_PATH := $(py))
endif
	$(eval VENV_PATH := $(shell $(PY_PATH) ./zdevelop/make_scripts/make_venv.py))
	@echo "venv created! To enter virtual env, run:"
	@echo ". ~/.bash_profile"
	@echo "then run:"
	@echo "$(VENV_PATH)"

.PHONY: format
format:
	-autopep8 --in-place --recursive --aggressive .
	-black .

.PHONY: doc
doc:
	python setup.py build_sphinx -E
	sleep 1
	open ./zdocs/build/html/index.html

.PHONY: proto
proto:
	python3 -m grpc_tools.protoc -I. --python_out=./gen --python_grpc_out=./gen ./stalk_proto/*.proto ./stalk_proto/google/api/*.proto
	python3 ./zdevelop/make_scripts/make_proto.py
	make format

.PHONY: image-dev
image-dev:
	DOCKER_BUILDKIT=1 docker build \
	--no-cache \
	-t bpeake89/stalkreporter:dev .