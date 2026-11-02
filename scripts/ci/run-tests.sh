#!/usr/bin/env bash

set -euo pipefail

#############################################
# Author: Christian Javier Zuñiga Mera
# email: christianjmera@gmail.com
#############################################

echo "=================================="
echo "     Starting automated tests     "
echo "=================================="

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

cd "$PROJECT_ROOT"

echo "Project: devops-sre-lab"
echo "Working directory: $(pwd)"

echo "Installing test dependencies..."
python -m pip install -r requirements-dev.txt

echo "Running pytest..."
python -m pytest -v

echo "=================================="
echo "   Tests completed successfully   "
echo "=================================="
