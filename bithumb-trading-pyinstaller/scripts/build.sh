#!/bin/bash

# Navigate to the src directory
cd ../src

# Use PyInstaller to create the executable
pyinstaller --onefile bithumb-trading.py

# Move the generated executable to the root of the project
mv dist/bithumb-trading ../

# Clean up the build artifacts
rm -rf build dist __pycache__ bithumb-trading.spec

echo "Build completed. Executable is located at ../bithumb-trading."