# Backend
Backend


The following are URLs to be used in the app:

## User Login
http://127.0.0.1:8000/professionals_app/token/login

### Method=POST

Required fields
* email
* password

#### Response
* HTTP_204 - Ok 
   * auth_token

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

#### Responses
* HTTP_201 - SUccessfully created
* HTTP_400 - Bad request 
    Either username exists
    Passwords dont match
    All required fields have not been filled


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

#### Responses 
* HTTP_200 - Succesful
* HTTP_400 - Bad request
    Fields required have not been filled


### Method=PATCH
Can be used to update details. With just one single required field.
Required fields 
* The field you want to update

#### Responses
* HTTP_200 - Succesful
* HTTP_400 - Bad request
    Fields required have not been filled


# Resend activation email
http://127.0.0.1:8000/professionals_app/users/resend_activation

### Method=POST

Required fields
* email

## Logout
http://127.0.0.1:8000/professionals_app/token/logout

#### Responses
* HTTP_204 - No content

### Method=GET

## Provides the list of all the users
http://127.0.0.1:8000/professionals_app/userlist/

#### Responses
* HTTP_200 - ok
* Empty array if none


### Method=GET

## Filters the users by email
http://127.0.0.1:8000/professionals_app/userlist/user's email


### Method=GET

#### Responses
* HTTP_200 - User found
* HTTP_404 - No user

## Filters users by service
http://127.0.0.1:8000/professionals_app/userlist/service/service_name

### Method=GET

#### Responses
* HTTP_200 - User found
* HTTP_404 - No user

## Provides a list of all categories.
http://127.0.0.1:8000/professionals_app/categories/

#### Responses
* HTTP_200 - ok
* Empty array if none

### Method=GET

## Filters category by name
http://127.0.0.1:8000/professionals_app/categories/category_name


### Method=GET

#### Responses
* HTTP_200 - Category found
* HTTP_404 - No user

## Provides a list of all services
http://127.0.0.1:8000/professionals_app/services

### Method=GET

#### Responses
* HTTP_200 - ok
* Empty array if none

## Filters service by category name
http://127.0.0.1:8000/professionals_app/services/category_name

#### Responses
* HTTP_200 - Service found
* HTTP_404 - No service

## Filters service by name
http://127.0.0.1:8000/professionals_app/services/service name

#### Responses
* HTTP_200 - Service found
* HTTP_404 - No service found

## Get most popular services
http://127.0.0.1:8000/professionals_app/popular

### Method=GET

#### Responses
* HTTP_200 - services found
* Empty array no services 



## Reviews API
http://127.0.0.1:8000/professionals_app/reviews/reviewees-id

### Metod=POST

#### Required
* review
* rating
* reviewee

#### Responses
* HTTP_201 - created
* HTTP_400 - Bad request

### Method=GET

#### Respnses
* HTTP_200 - ok
* Empty array no reviews



## Password reset
http://127.0.0.1:8000/professionals_app/users/reset_password/

### Method=POST

Required
* email

#### Responses
* HTTP_204 - No content
* HTTP_400 - Bad request email not available in the database


## Password set
http://127.0.0.1:8000/professionals_app/users/set_password

### Method=POST

 Required
* new_password
* re_new_password
* current_password

#### Responses

* HTTP_204 - No content
            succesful request. 
* HTTP_400 - Bad request
        Lack of required fields
        Password not same.
        Wrong password


You must also be authenticated to access all these APIs except the forgotten password and activation email links.
Authentication fields are Email and Password
