# CC-QMUL-group-project
QMUL Cloud Computing group project


For the project specifications;

External REST service is IEX API. Here's the documentation https://iexcloud.io/docs/api/
<snapshot of the quote price and symbol>
  
CRUD operations: Our applications can perform the following CRUD operations; The status codes have been assigned according to the responses conforming to REST standards.

For GET method; 1. Welcome Page 2. Display of the stocks bought by the users
For POST method; 1. Users can buy the stocks 2. Users can register their accounts along with password 3. Users can login 4. 
For DELETE method; 1. Users can return the stocks that they bought
For PUT method; 1. Users can change their login password

### External Cloud database 
Postgres database application has been setup on AWS instance using Docker image. The postgres docker container has been created by the below command;

`docker run --name qmul_cloud -p 5432:5432 -e POSTGRES_DB=stocks -e POSTGRES_USER=dba -e POSTGRES_PASSWORD=dba_pswd -d postgres` 
 
Option 2 has been addressed. 

1. Implementing user accounts and access management.
2. Implementing hash-based authentication.
3. Securing the database with role-based policies.



Some of the curl commands to be used on windows terminal;

curl -i -H "Content-Type:application/json" -X POST -d "{\"name\":\"danny\", \"pswd\":\"blah\"}" http://127.0.0.1:5000/register

curl -i -H "Content-Type:application/json" -X POST -d "{\"name\":\"danny\", \"pswd\":\"blah\"}" http://127.0.0.1:5000/login

curl -i -H "Content-Type:application/json" -X POST http://127.0.0.1:5000/buy/TWTR

docker run --name qmul_cloud -p 5432:5432 -e POSTGRES_DB=stocks -e POSTGRES_USER=dba -e POSTGRES_PASSWORD=dba_pswd -d postgres

curl -i -H "Content-Type:application/json" -X DELETE http://127.0.0.1:5000/return/3

curl -i -H "Content-Type:application/json" -X PUT -d "{\"name\":\"danny\", \"pswd\":\"blah\", \"new_pswd\":\"boo\"}" http://127.0.0.1:5000/reset_password


