# API Test Suite

This repository contains a suite of automated tests for the API endpoints related to pets, stores, and users. The tests are implemented using the `unittest` framework in Python.

## Table of Contents

- [API Test Suite]
  - [Table of Contents]
  - [Installation]
  - [Usage]
  - [Test Structure]
    - [TestAPIPet]
    - [TestAPIStore]
    - [TestAPIUser]
  - [Contributing]

## Installation

    1. Clone the repository:
       git clone https://github.com/AliEisami/Final_Project.git

    2. Set up a virtual environment and install dependencies:
        python -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt


Usage
To run the tests, simply execute:
    python -m unittest discover -s tests


Test Structure
The test suite is organized into three main classes, each testing different parts of the API: pets, store, and users.


TestAPIPet
This class contains tests for the Pet API.

    test_add_pet_to_the_store: Tests adding a pet to the store.
    test_update_pet_in_the_store: Tests updating a pet in the store.
    test_get_pets_by_status: Tests retrieving pets by their status.
    test_get_pets_by_id: Tests retrieving a pet by its ID.
    test_update_pet_by_id: Tests updating a pet by its ID.
    test_delete_pet_by_id: Tests deleting a pet by its ID.


TestAPIStore
This class contains tests for the Store API.

    test_get_store_inventory: Tests retrieving the store inventory.
    test_place_order_for_purchasing: Tests placing an order.
    test_find_order_by_id_successful: Tests finding an order by a valid ID.
    test_find_order_by_id_unsuccessful: Tests finding an order by an invalid ID.
    test_delete_order_by_id_successful: Tests deleting an order by a valid ID.
    test_delete_order_by_id_unsuccessful: Tests deleting an order by an invalid ID.


TestAPIUser
This class contains tests for the User API.

test_create_list_of_users: Tests creating a list of users.
test_find_user_by_username: Tests retrieving a user by their username.
test_delete_user_by_username: Tests deleting a user by their username.
test_login_user_successful: Tests logging in with a valid username and password.
test_login_user_unsuccessful: Tests logging in with an invalid username and password.


Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.
