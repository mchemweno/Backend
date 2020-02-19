# Backend
Backend


The following are URLs to be used in the app:

## User Login
http://127.0.0.1:8000/professionals_app/token/login

### Method=POST

Required fields
* email
* password

## Create Users
http://127.0.0.1:8000/professionals_app/users/

### Method=POST

Required fields
* username
* phone
* first_name
* last_name
* bio
* user_type
* service
* email
* password
* re_password

# Get user details, update user details and update only one field user field
http://127.0.0.1:8000/professionals_app/users/me/

### Method=GET
This will return all required fields

### Method=PUT
Can be used to update a user details. All fields required.
Required fields
* username
* phone
* first_name
* last_name
* bio
* user_type
* service
* email
* password
* re_password


### Method=PATCH
Can be used to update details. With just one single required field.
Required fields 
* The field you want to update

# Resend activation email
http://127.0.0.1:8000/professionals_app/users/resend_activation

### Method=POST

Required fields
* email

## Logout
http://127.0.0.1:8000/professionals_app/token/logout

### Method=GET

## Provides the list of all the users
http://127.0.0.1:8000/professionals_app/userlist/

### Method=GET

## Filters the users by email
http://127.0.0.1:8000/professionals_app/userlist/user's email

### Method=GET

## Filters users by service
http://127.0.0.1:8000/professionals_app/userlist/service/service_name

### Method=GET


## Provides a list of all categories.
http://127.0.0.1:8000/professionals_app/categories/

### Method=GET

## Filters category by name
http://127.0.0.1:8000/professionals_app/categories/category_name

### Method=GET


## Provides a list of all services
http://127.0.0.1:8000/professionals_app/services

### Method=GET

## Filters service by name
http://127.0.0.1:8000/professionals_app/services/category_name

### Method=GET

## Password reset
http://127.0.0.1:8000/professionals_app/users/reset_password/

### Method=POST

Required
* email

## Password set
http://127.0.0.1:8000/professionals_app/users/set_password

### Method=POST

 Required
* new_password
* re_new_password
* current_password


The filters are not case sensitive therefore searching netwroking will return Networking and vice versa.
Also searchng work or net will return networking

This applies to all the filters provided.

You must also be authenticated to access all these APIs except the forgotten password and activation email links.
Authentication fields are Email and Password.


### Remaining
* Database normalization. I feel we should critically look at it for one more time and make necessary changes.
