FROM postgres:15.6

# Add the plpython function to the database
RUN apt-get update && apt-get install --assume-yes postgresql-plpython3-12

# Delete our left over sample_data.sql
#RUN mkdir preloaded_data

# COPY ALL OF OUR DATA_SHEETS OVER (We copy all of them over since there's no conditional COPY)
#COPY ./pg_sample_data/*.sql  /preloaded_data/
COPY ./pg_sample_data/*.sql  /docker-entrypoint-initdb.d/

# Retrieve all of the files from the folder, copy them, print them, and delete the preloaded_data folder
#RUN file="$(ls -1 /preloaded_data)" && echo $file
#RUN array=$(ls ./preloaded_data -1); for i in ${array}; do cp ./preloaded_data/$i /docker-entrypoint-initdb.d/$i; echo $i; done
#RUN rm -rf /preloaded_data