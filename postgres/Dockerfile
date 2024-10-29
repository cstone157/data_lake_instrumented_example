FROM postgres:12.10

# Delete our left over sample_data.sql
RUN mkdir preloaded_data

# COPY ALL OF OUR DATA_SHEETS OVER (We copy all of them over since there's no conditional COPY)
COPY ./pg_sample_data/*.sql \
		/preloaded_data/

COPY ./pg_sample_data/random/*.sql \
		/preloaded_data/
