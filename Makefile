SPHINXOPTS    ?=
SPHINXBUILD   ?= poetry run sphinx-build
SOURCEDIR     = docsrc
BUILDDIR      = build

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

github-docs:
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@cp -a build/html/. ./docs

.PHONY: help Makefile
