# Pysura

## Requirements:

- gcloud CLI
- gcloud beta CLI
- A billing account with Google Cloud
- Docker
- Firebase CLI
- Python 3.6+
- Node 10+

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
2. Create or select an existing billing account in Google Cloud
3. Create or select an existing Firebase project
4. Create or select an existing VPC network with relevant serverless VPC connectors
5. Create or select an existing Cloud SQL instance
6. Deploy JWT auth via Firebase and configure Hasura to use it
7. Create a new Hasura project and configure it with baked in RBAC-auth
8. 