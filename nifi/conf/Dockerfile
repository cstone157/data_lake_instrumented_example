FROM apache/nifi:1.25.0

RUN CURL https://jdbc.postgresql.org/download/postgresql-42.2.12.jar --output /opt/nifi/nifi-current/lib/postgresql-42.2.12.jar

# jdbc:postgresql://postgres:5432/test_db
# org.postgresql.Driver
# /opt/nifi/nifi-current/lib/properties/postgresql-42.2.12.jar