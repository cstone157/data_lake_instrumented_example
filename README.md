# Example Data Lake
## Instructions
### Start the server
```bash
$ docker-compose up
```

### Start the server (silent mode)
```bash
$ docker-compose up -d
```

### Stop the server
```bash
$ docker-compose down
```

### Stop the server and delete containers
```bash
$ docker-compose down -v
```

## pgAdmin (http://localhost:3001/) (username=shoc@shoc.us, password=JustKeepSwimming)
###   - Used for accessing the SQL database
###   - Add server, in connection tab set (host=pg_container, username=shoc, password=JustKeepSwimming)
###   - The database should come with a precreated tablespace / table called process_data_raw
## JupyterLab (http://localhost:3000/)
###   - Used for writing Python code for analysis
## Nifi (http://localhost:3003/)
###   - ETL (Extract Transform Load), used for routing all of the data from the generators to the database

