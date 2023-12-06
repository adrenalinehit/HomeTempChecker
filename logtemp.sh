#!/bin/bash

# Change to the directory containing the Python script
cd ./code

# Run the Python script
nohup python templogger.py > /dev/null 2>&1 &
