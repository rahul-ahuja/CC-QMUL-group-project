# QMUL Cloud Computing group project

git clone https://rahul-ahuja@github.com/rahul-ahuja/CC-QMUL-group-project




For the project specifications;

External REST service is IEX API. Here's the documentation https://iexcloud.io/docs/api/
<snapshot of the quote price and symbol>
  
CRUD operations: Our applications can perform the following CRUD operations; The status codes have been assigned according to the responses conforming to REST standards.

1. For GET method; i. Welcome Page ii. Display of the stocks bought by the users
2. For POST method; i. Users can buy the stocks ii. Users can register their accounts along with password iii. Users can login
3. For DELETE method; i. Users can return the stocks that they bought
4. For PUT method; i. Users can change their login password

### External Cloud database 
Postgres database application has been setup on AWS instance using Docker image. The postgres docker container has been created by the below command;

`docker run --name qmul_cloud -p 5432:5432 -e POSTGRES_DB=stocks -e POSTGRES_USER=dba -e POSTGRES_PASSWORD=dba_pswd -d postgres` 
 
Option 2 has been addressed. 

1. Implementing user accounts and access management.
2. Implementing hash-based authentication.
3. Securing the database with role-based policies.

![image](https://user-images.githubusercontent.com/21355015/113444079-155dd280-93eb-11eb-81b5-5531b427df38.png)

Some of the curl commands to be used on windows terminal;

curl -i -H "Content-Type:application/json" -X POST -d "{\"name\":\"danny\", \"pswd\":\"blah\"}" http://127.0.0.1:5000/register

curl -i -H "Content-Type:application/json" -X POST -d "{\"name\":\"danny\", \"pswd\":\"blah\"}" http://127.0.0.1:5000/login

curl -i -H "Content-Type:application/json" -X POST http://127.0.0.1:5000/buy/TWTR

docker run --name qmul_cloud -p 5432:5432 -e POSTGRES_DB=stocks -e POSTGRES_USER=dba -e POSTGRES_PASSWORD=dba_pswd -d postgres

curl -i -H "Content-Type:application/json" -X DELETE http://127.0.0.1:5000/return/3

curl -i -H "Content-Type:application/json" -X PUT -d "{\"name\":\"danny\", \"pswd\":\"blah\", \"new_pswd\":\"boo\"}" http://127.0.0.1:5000/reset_password


