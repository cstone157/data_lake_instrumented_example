-- Add the python extension to the database
CREATE EXTENSION IF NOT EXISTS plpython3u;

-- Install the dblink exstension (dblink is a module that 
--		supports connections to other PostgreSQL databases 
--		from within a database session.)
CREATE EXTENSION IF NOT EXISTS dblink;

-- Create the postgres superuser role incase it doesn't already
--		exist (we don't create it my default, since the default
--		user was named shoc)
DO
$do$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_catalog.pg_roles  -- SELECT list can be empty for this
      WHERE  rolname = 'postgres') THEN

      CREATE ROLE postgres WITH LOGIN SUPERUSER INHERIT CREATEDB CREATEROLE REPLICATION PASSWORD 'JustKeepSwimming!';
   END IF;
END
$do$;


-- Create the test_db database if it doesn't exist
DO
$do$
BEGIN
   IF EXISTS (SELECT FROM pg_database WHERE datname = 'test_db') THEN
      RAISE NOTICE 'Database already exists';  -- optional
   ELSE
      PERFORM dblink_exec('dbname=' || current_database()  -- current db
                        , 'CREATE DATABASE test_db OWNER=''shoc''');
   END IF;
END
$do$;

-- Switch to the test_db database
SET search_path TO test_db;
\connect test_db


CREATE SEQUENCE IF NOT EXISTS public.process_data_raw_uid
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.process_data_raw_uid
    OWNER TO shoc;

CREATE TABLE IF NOT EXISTS public.process_data_raw
(
    uid integer NOT NULL DEFAULT nextval('process_data_raw_uid'::regclass),
	user_name varchar(25),
	role_name varchar(25),
	process_name varchar(25),
	message text,
	timestamp timestamp,
    CONSTRAINT process_data_raw_pkey PRIMARY KEY (uid)
);

ALTER TABLE IF EXISTS public.process_data_raw
    OWNER to shoc;