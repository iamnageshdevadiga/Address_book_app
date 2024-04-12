# Address_book_app

Address Book API
This is a simple RESTful API for managing addresses in an address book.

# Features
Create Address: Allows users to create new addresses.'

Update Address: Allows users to update existing addresses by ID.

Delete Address: Allows users to delete addresses by ID.

Get Addresses: Allows users to retrieve a list of addresses with pagination support.

## Technologies Used

FastAPI: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
SQLAlchemy: SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
SQLite: SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.

## Requirements
    1.Required VS code editor or Pycharm editor

    2.python should be installed

## Installation

Clone the repository:

```bash
  git clone https://github.com/iamnageshdevadiga/Address_book_app.git
```
    cd Address_book_app/

## Create and Activate Virtual Environment:
 
    python -m venv venv

Activate the virtual environment:
    
    For Windows Command Prompt:
    venv\Scripts\activate

    For Unix/Linux:
    source venv/bin/activate


## Install dependencies:

    pip install -r requirements.txt


## Running the Application
    Run the following command to start the FastAPI application:
    uvicorn main:app --reload

## Contributing

Feel free to contribute to this project. Follow the contribution guidelines for more details.


## License

This project is licensed under the MIT License.
