SPHINXOPTS    ?=
SPHINXBUILD   ?= poetry run sphinx-build
SOURCEDIR     = docsrc
BUILDDIR      = build

help:
	@make github-docs

github-docs:
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@cp -a build/html/. ./docs

.PHONY: help Makefile
