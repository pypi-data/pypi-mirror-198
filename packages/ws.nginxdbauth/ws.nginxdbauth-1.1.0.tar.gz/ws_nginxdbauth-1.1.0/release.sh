#!/bin/bash

set -ex

changelog=$(hatch run release:towncrier build --version=draft --draft 2>&1)
if echo "$changelog" | grep -q "No significant changes"; then
    echo "No changelog entries exist that could be released"
    exit 1
fi

hatch version release
version=$(hatch version)

hatch run release:towncrier build --version="$version" --yes
git commit src/**/__init__.py CHANGES.txt changelog/ -m "Preparing release: $version"
git tag "$version"

hatch build
# hatch publish

hatch version minor
hatch version dev
git commit src/**/__init__.py -m "Back to development: $(hatch version)"
