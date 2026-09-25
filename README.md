# Flask API in Docker - coordinate interpolation

A small Python/Flask assessment project that generates a grid of pixel coordinates from image dimensions and four rectangle corners. The browser form posts the inputs to a Flask endpoint; the response contains the interpolated coordinates. This repository preserves the original assessment notebook alongside the runnable example.

## Explore

- [Assessment notebook and explanation](Fetch_Rewards/Fetch_Rewards_Coding_Assessment-Machine_Learning_Engineer.ipynb)
- [Flask application](Fetch_Rewards/api.py)
- [Browser form](Fetch_Rewards/templates/home.html)
- [Dockerfile](Fetch_Rewards/Dockerfile)

## Inputs and output

Enter dimensions as a two-item tuple `(rows, columns)`, for example `(3, 5)`. Enter four rectangle corners as coordinate tuples, for example `[(1, 1), (3, 3), (3, 1), (1, 3)]`. The service sorts the horizontal and vertical bounds and interpolates evenly spaced coordinates from left to right and top to bottom.

The `/join` route returns a JSON object whose `result` field holds string-formatted rows. This is a demonstration of a particular assessment solution, not a general image-processing library or production API. Inputs are parsed as Python literals and are not comprehensively validated.

## Run locally

From the repository root:

```bash
cd Fetch_Rewards
docker build -t coordinate-grid-demo .
docker run --rm -p 5000:5000 coordinate-grid-demo
```

Open `http://localhost:5000`. Stop the container with Ctrl+C. A local Python environment can run `python api.py` after installing `Fetch_Rewards/requirements.txt`.

The pinned dependencies and Dockerfile reflect the original exercise and have not been retested against current container tooling. If you encounter an installation error, inspect the Python base image and dependency compatibility before using this as a runnable example. The application runs Flask's development server with debug mode enabled, so use it only in a local development setting.

## Project scope

This exercise illustrates coordinate transformations, a small HTTP interface, and container packaging. The notebook provides the problem framing and fuller explanation.
