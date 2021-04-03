# QMUL Cloud Computing group project

git clone https://rahul-ahuja@github.com/rahul-ahuja/CC-QMUL-group-project




For the project specifications;

External REST service is IEX API. Here's the documentation https://iexcloud.io/docs/api/
<snapshot of the quote price and symbol>
  
CRUD operations: Our applications can perform the following CRUD operations; The status codes have been assigned according to the responses conforming to REST standards.

1. For GET method;
 
i. Welcome Page implemented with function of hello()

ii. Display of the stocks bought by the users implemented with function of get_records(symbol)

2. For POST method; 

i. Users can buy the stocks implemented with function of buy(symbol)

ii. Users can register their accounts along with password implemented with function of register()   

iii. Users can login implemented with function of login()

3. For DELETE method; 

i. Users can return the stocks that they bought implemented with function of return_stocks(r_id)

4. For PUT method; 

i. Users can change their login password implemented with function of reset_password()

### External Cloud database 
Postgres database application has been setup on AWS instance using Docker image. The postgres docker container has been created by the below command;

 
Option 2 has been addressed. 

1. Implementing user accounts and access management.
2. Implementing hash-based authentication.
3. Securing the database with role-based policies.

![image](https://user-images.githubusercontent.com/21355015/113448602-0fb8ba80-93f4-11eb-93d4-d57919080f63.png)

To run the application, the following are the steps;

1. Install Docker to run the postgres or setup postgres on AWS by any configuration;
```
sudo apt update
sudo apt install docker.io
```

2. Install pip3 to install python dependencies

`sudo apt install python3-pip`

3. Install python dependencies

`pip3 install -r requirements`

To run the application within the directory

1. Setup Postgres Docker container with the name of qmul_cloud by;

`docker run --name qmul_cloud -p 5432:5432 -e POSTGRES_DB=stocks -e POSTGRES_USER=dba -e POSTGRES_PASSWORD=dba_pswd -d postgres` 

2. Setup the Database along with the tables created and the role created;

`python3 postgres_setup.py`

3. Run the Flask application;

`python3 app.py`

4. Run the application on the web browser with the below URL and follow the youtube video;

`aws_public_ip:5000`
