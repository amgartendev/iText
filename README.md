# iText - Chat App
iText is a desktop application whose functionality and design were inspired by iMessage and Discord. The application allows users to add their friends, send and receive messages, update their profile information, and more, all in real time. Depending on which version of iText you are using, the design may be a little "raw," as the main goal in the early stages of development was to make every feature functional, with the UI/UX improvements to be done later.

The main technologies utilized for the creation of iText are:
- Python 3
- PySide6
- FastAPI
- SQLAlchemy
- Websockets

## ⚡ Performance
Since iText is a real-time application and has numerous database operations, the performance of the server-client communication can vary depending on your machine's specifications, such as CPU power and RAM.


## 💬 How can you help the project?
If you discover any bugs, please use the link below to submit a bug report.

| Type                            | Links                              |
|---------------------------------|-----------------------------------------|
| ✅ **Pull Requests**             | [**Send your Pull Request**](https://github.com/amgartendev/iText/pulls) |
| 🚨 **Bug Reports**              | [**Send your Bug Report**](https://github.com/amgartendev/iText/issues) |


## 💻 iText works in
This is all the platforms that I've tested iText, and it's working so far.
If your platform is not listed here it was not tested yet.

| Platform | Status      | Latest Python Version Tested |
|----------|-------------|------------------------------|
| Windows  | ✅ Working | 3.12.5                       |
| MacOS    | ✅ Working | 3.13                         | 
| Linux    | ✅ Working | 3.13                         |


## 📦 Install and setup iText
Follow the steps below to install all the packages necessary to use iText:
```bash
python -m venv venv
pip install --upgrade pip
pip install -r requirements.txt
```

## 💾 Setting up the database
Since iText needs a database connection to create users and perform numerous other operations via API, you will need to set up a database.

⚠️Please keep in mind that the DBMS used while developing this project was MySQL, with MySQL Workbench as the client application. If you are using PostgreSQL or any other DBMS, you might need to change the SQL driver constant named `DB_URL` located in `\server\core\configs.py`⚠️ 

Once we have our DBMS installed, we need to create a new database (or schema) named `itext`. Once the database is created, you don't need to do anything else inside it.

Now, open the terminal inside the project folder and run the `create_tables.py` script. Follow the example below:
```bash
cd server
python create_tables.py
```

## 💻 Running iText
To properly execute iText, you will need to open two separate terminals, one for the server and one for the client. This can easily be done by entering the respective server and client directories and executing their main files. Follow the terminal instructions below:

To execute the server:
```bash
cd server
python main.py
```

To execute the client:
```bash
cd client
python main_window.py
```