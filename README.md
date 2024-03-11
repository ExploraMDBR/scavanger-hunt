# Explora Scavanger Hunt Web App
A game of Scavanger Hunt implemented in Python Flask, serving an Admin Dashboard for setting up the game and a client for players.


Tested and running in VPS with Ubuntu Server 18.04 LTS

## Development
```bash
# Clone repo
git clone <repo>

# Install pipenv if you don't have it
pip3 install pipenv

# Activate virtual env
python3 -m pipenv shell

# Install dependencies
pipenv install

# Initialize application
pipenv run init

# Run DEV server locally on port 5000
pipenv run dev_server

# or

# Run DEV server accessible from remote on port 5001
pipenv run dev_server_remote

```

## Production WSGI Server with Apache

- Clone repo to VPS, after setting DEPLOY_VARS.sh
`./deploy.sh`

- Connect with ssh to server and 
`~/install_caccia_apache.sh`

See [this article](https://medium.com/@prithvishetty/deploying-a-python-3-flask-app-into-aws-using-apache2-wsgi-1b26ed29c6c2) for more info. 


## Firebase services
This project uses Firebase for auth services. To set this up correctly, after create a Firebase project and follow these instructions:

- place firebase.json in `instance` folder, rename `FIREBASE_CONF` value in `__init__.py`

- place `firebaseConfig.js` in `caccia_server/static` folder