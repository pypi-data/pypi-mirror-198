# Pysura

## Requirements:

- gcloud CLI
- gcloud beta CLI
- A billing account with Google Cloud
- Docker
- Firebase CLI
- Python 3.6+

```commandline
pip install pysura
pysura
(pysura_cli) >>> setup
```

What is Pysura?

Pysura is a CLI tool that's designed to make building and deploying actions, events, and chron-jobs as 
easy as it is to do everything else in Hasura.

Pysura does *not* use the Hasura CLI, and instead manages the metadata directly via retrieving it and overwriting it.

Pysura is built to bring Python to Hasura because it's a really great language for things like actions, events, and
chron-jobs. 

How can Pysura help me setup my project?

Run the setup command and follow the installer instructions and you are done.

### What the setup command does?

1. Create or select an existing project in Google Cloud
2. Select an existing billing account in Google Cloud
3. Configure a Virtual Private cloud with subnets and firewall rules
4. Create a Cloud SQL Postgresql instance with specified memory and storage in specified region
5. Deploys Hasura to Cloud Run with all database connections routed through serverless VPC connectors
6. Attaches a Firebase project to the google cloud project
7. Enables Firebase Authentication (Requires user to enable phone authentication in the Firebase console)
8. Builds and Deploys template firebase functions to handle authentication and authorization
9. Attaches Firebase Authentication JWT to Hasura for RBAC
10. 