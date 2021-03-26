# periodic_scraper

Repo for Google Cloud MySQL DB updater

### Process

Set up a Google Cloud Scheduler job to emit a pub/sub message ~every hour. This should trigger a cloud function with
main in main.py as entry point. When on app engine, secrets are handled using secret manager.

When first inserting data into DB, run periodic_scraper main locally. Initial insertion takes about 2 hours. You will
need to create a secrets directory with username, password, optional cert files (if using SSL). See gcp_util/database
_engine.py for where to put local secrets. 