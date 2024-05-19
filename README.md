# Online Bookstore Mock API and Automated Testing

## Project Overview
This project involves designing and implementing mock APIs for a hypothetical online bookstore, followed by the development of a comprehensive automated testing suite for these APIs. The mock APIs simulate key functionalities like user registration, user login, book search, adding to cart, and checkout. Automated tests are created to validate these functionalities.

## Table of Contents
- [Project Structure](#project-structure)
- [API Specifications](#api-specifications)
- [Mock API Implementation](#mock-api-implementation)
- [Automated Testing](#automated-testing)
- [Postman Collection](#postman-collection)
- [Setup and Running](#setup-and-running)
- [Documentation](#documentation)

## Project Structure

## Project Structure
```
api-testing-project/
  ├── mock-apis/
  │   ├── source/
  │   └── config/
  ├── tests/
  │   └── integration/
  ├── Postman_collection.json
  └── README.md
```

![image](https://github.com/braja555/api-testing-project/assets/20472118/6b879a83-7bbf-440c-9a21-48ec40a55ef8)


## API Specifications

### 1. User Registration
### 2. User Login
### 3. Search Books
### 4. Add to Cart
### 5. Checkout

##Mock API Implementation

The mock APIs for User Registration and User Login are implemented using the Mockoon tool. However, due to limitations of Mockoon, the remaining APIs (Search Books, Add to Cart, and Checkout) are implemented using Flask for Python. The source code for these mock services can be found in the mock-apis directory.


## Automated Testing

Automated tests are created using pytest and requests. Test scripts are located in the tests/integration directory.


## Postman Collection
A Postman collection is provided for manual testing. The collection is located at `Postman_collection.json`.

## Setup and Running
### Prerequisites
- Python 3.8+
- `pip` (Python package installer)

Setup Mock APIs with Mockoon (To Execute User Registration and User Login APIs)
Install Mockoon:

Download and install Mockoon from the official website.
Start Mockoon:

Launch Mockoon from your applications folder.
Import Mock APIs Configuration: Shared in email and google drive.

Import the provided Mockoon configuration file (mock-apis/mockoon_config.json) into Mockoon.
Start Mockoon Server:

Start the Mockoon server by clicking the "Play" button next to the imported environment.

### Setup Mock APIs for pytest (To Execute Search Books, Add to Cart and Checkout APIs)
1. Navigate to the `mock-apis/source` directory:
   ```bash
   cd api-testing-project/mock-apis
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the mock server:
   ```bash
   python app.py
   ```

### Run Automated Tests
1. Navigate to the project root directory:
   ```bash
   cd api-testing-project
   ```
2. Install test dependencies:
   ```bash
   pip install pytest requests
   ```
3. Execute the tests:
   ```bash
   pytest
   ```

## Documentation
Detailed documentation is provided within each script and the API specification section above. For further information, refer to the comments and docstrings within the source code.


