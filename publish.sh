#!/bin/bash
set -e

quarto render
ghp-import -c pythonbook.madebykim.kr -f -n -o -p _site
