# Use the jupyter datascience-notebook
FROM jupyter/datascience-notebook:x86_64-ubuntu-22.04

# Switch to root user
USER root

# Add the libpq-dev library
RUN apt-get update && apt-get install --assume-yes libpq-dev 

# Switch back to jovyan
USER jovyan

# Install the psycopg2 library
RUN pip install psycopg2 plotly

# Install the Google generativeai library
RUN pip install -U google-generativeai