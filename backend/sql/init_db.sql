CREATE USER homebank PASSWORD 'homebank' CREATEDB;
CREATE DATABASE homebank WITH ENCODING='UTF8' OWNER=homebank;
\connect homebank
GRANT ALL PRIVILEGES ON DATABASE homebank TO homebank;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO homebank;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO homebank;
