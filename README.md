# Olympic Innovation Challenge - Web Application
### Written with ExpressJS and React

## Installation
After downloading and unzipping, in each folder (root, client, server) run the following command:
```
npm install
```

## Setting Up The Database
In the db directory, run
```
python db_setup.py
```
This will drop all tables in `teamolympic.db`, create them, and populate them.
## Usage

Open a terminal in the root folder. Individual npm scripts have been set-up that can be run from the root folder.
```
npm start : Runs both client and server concurrently
npm run server : runs server on port 9000
npm run client : runs client on port 3000
```
After running both client and server, you can visit the landing page at localhost:3000
