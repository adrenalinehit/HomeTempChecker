#!/bin/bash

# Change to the directory containing the Python script
cd ./code

# Run the Python script
nohup python airqual.py > /dev/null 2>&1 &
