.PHONY: all
all:
	$(MAKE) get-deps
	$(MAKE) build

.PHONY: get-deps
get-deps: get-deps-pip get-deps-go get-deps-bindings get-deps-webui

.PHONY: get-deps-%
get-deps-%:
	$(MAKE) -C $(subst -,/,$*) get-deps

.PHONY: get-deps-pip
get-deps-pip:
	pip install -r requirements.txt

.PHONY: get-deps-go
get-deps-go:
	$(MAKE) get-deps-master
	$(MAKE) get-deps-agent
	$(MAKE) get-deps-proto

.PHONY: package
package:
	$(MAKE) -C agent $@
	$(MAKE) -C master $@

.PHONY: build-%
build-%:
	$(MAKE) -C $(subst -,/,$*) build

.PHONY: build-docs
build-docs: build-common build-harness build-cli build-deploy build-model_hub build-examples build-helm build-proto 
	$(MAKE) -C docs build

.PHONY: build-bindings
build-bindings: build-proto
	$(MAKE) -C bindings build

.PHONY: build-webui
build-webui: build-bindings
	$(MAKE) -C webui build

.PHONY: build-agent
build-agent: build-proto
	$(MAKE) -C agent build

.PHONY: build-master
build-master: build-proto
	$(MAKE) -C master build

.PHONY: build
build: build-master build-agent build-webui build-docs 

.PHONY: clean-%
clean-%:
	$(MAKE) -C $(subst -,/,$*) clean
.PHONY: clean
clean: clean-tools clean-proto clean-common clean-harness clean-cli clean-deploy clean-model_hub clean-examples clean-docs clean-webui clean-master clean-agent clean-bindings 

.PHONY: check-%
check-%:
	$(MAKE) -C $(subst -,/,$*) check
.PHONY: check
check: check-common check-proto check-harness check-cli check-deploy check-model_hub check-e2e_tests check-tools check-master check-webui check-examples check-docs check-schemas
	$(MAKE) check-agent

.PHONY: fmt-%
fmt-%:
	$(MAKE) -C $(subst -,/,$*) fmt
.PHONY: fmt
fmt: fmt-common fmt-harness fmt-cli fmt-deploy fmt-model_hub fmt-e2e_tests fmt-tools fmt-master fmt-agent fmt-webui fmt-examples fmt-docs fmt-schemas fmt-proto 

.PHONY: test-%
test-%:
	$(MAKE) -C $(subst -,/,$*) test
.PHONY: test
test: test-harness test-cli test-common test-model_hub test-master test-agent test-webui 

.PHONY: devcluster
devcluster:
	devcluster -c tools/devcluster.yaml
