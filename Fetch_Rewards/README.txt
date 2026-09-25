# Fetch Rewards coding assessment - Flask demonstration

This folder contains the Flask implementation, a browser form, and the original notebook. Start with the [repository overview](../README.md) for inputs, output, scope, and limitations.

## Files

- `api.py`: coordinate interpolation and the Flask routes
- `templates/home.html`: browser form and response display
- `static/css/style.css`: form styling
- `Dockerfile` and `requirements.txt`: container and Python dependencies
- `Fetch_Rewards_Coding_Assessment-Machine_Learning_Engineer.ipynb`: original assessment walkthrough
- `cmdFR.txt`: quick Docker commands

## Start locally

From the repository root, change to this directory and run the commands in `cmdFR.txt`. Then open `http://localhost:5000`. Stop the server with Ctrl+C. Docker must be installed and running. These original pinned dependencies have not been verified against current container tooling.

The service is a local development demonstration. Its Flask debug server and limited input validation are not suitable for public deployment.
