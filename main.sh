#!/bin/bash

# Generate the site
python3 main.py

# Start the web server in the public directory
cd public && python3 -m http.server 8888
