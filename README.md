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

## Project Structure
```
api-testing-project/
  ├── mock-apis/
  │   ├── source/
  │   
  ├── tests/
  │   └── integration/
  ├── resources
  │   └── BookStoreAPIs.postman_collection.json
  │   └── BookStoreAPIs_Mockoon.json
  └── README.md
```

## API Specifications

### 1. User Registration
- **Endpoint**: `POST /users/register`
- **Endpoint**: `PUT /users/register`
- **Endpoint**: `DELETE /users/register`

### 2. User Login
- Endpoint: `POST /users/login`

### 3. Search Books
- Endpoint: `GET /book/search`
  
### 4. Add to Cart
- Endpoint: `POST /users/{userId}/cart`
  
### 5. Checkout
- Endpoint: `POST /users/{userId}/checkout`

  
## Mock API Implementation

The mock APIs for User Registration and User Login are implemented using the Mockoon tool. However, due to limitations of Mockoon, the remaining APIs (Search Books, Add to Cart, and Checkout) are implemented using Flask for Python. The source code for these mock services can be found in the mock-apis directory.


## Automated Testing

Automated tests are created using pytest and requests. Test scripts are located in the `tests/integration` directory.


## Postman Collection

A Postman collection is provided for manual testing. The collection is located at `resources/BookStoreAPIs.postman_collection.json`.

## Setup and Running

### Prerequisites
- Python 3.8+
- `pip` (Python package installer)

### Setup Mock APIs with Mockoon (To Execute User Registration and User Login APIs)
1. Install Mockoon:
   Download and install Mockoon from the official website.

2. Start Mockoon:
   Launch Mockoon from your applications folder.

3. Import Mock APIs Configuration: 
   Import the provided Mockoon configuration file `resources/BookStoreAPIs_Mockoon.json` into Mockoon.

6. Start the Mockoon server:
   Start the Mockoon server by clicking the "Play" button next to the imported environment.


### Setup Mock APIs for pytest (To Execute Search Books, Add to Cart and Checkout APIs)
1. Navigate to the `mock-apis/source` directory:
   ```terminal
   cd api-testing-project/mock-apis
   ```
2. Install dependencies:
   ```terminal
   pip install -r requirements.txt
   ```
3. Run the mock server:
   ```terminal
   python book_api.py
   ```

### Run Automated Tests
1. Navigate to the project root directory:
   ```terminal
   cd api-testing-project
   ```
2. Install test dependencies:
   ```terminal
   pip install pytest requests
   ```
3. Execute the tests:
   ```terminal
   pytest
   ```




