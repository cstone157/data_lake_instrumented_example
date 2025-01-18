FROM postgres:12.10

# Add the plpython function to the database
RUN apt-get update && apt-get install --assume-yes postgresql-plpython3-12

# Delete our left over sample_data.sql
RUN mkdir preloaded_data

# COPY ALL OF OUR DATA_SHEETS OVER (We copy all of them over since there's no conditional COPY)
COPY ./pg_sample_data/*.sql  /preloaded_data/
