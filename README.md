# QMUL Cloud Computing group project

git clone https://rahul-ahuja@github.com/rahul-ahuja/CC-QMUL-group-project

### Video Demo
https://drive.google.com/file/d/1genJKrDGx_dfyz8Hcf6h5asVc4hXrptt/view?usp=sharing


Description of the Application: This API can enable users to buy the stocks. We used the external rest api to fetch the information of the stocks like (stock symbol, company name and stock price).

For the project specifications;

External REST service is IEX API. Here's the documentation https://iexcloud.io/docs/api/
The endpoint to the External REST service is as follows;
<IPADDRESS>:5000/stocks/<company symbol>

Here's the Netflix stocks details collected from external rest API;

![image](https://user-images.githubusercontent.com/21355015/113519143-563c1f80-9582-11eb-991c-aca36a2f83f0.png)


Here's the Facebook stocks details collected from external rest API;
![image](https://user-images.githubusercontent.com/21355015/113519159-6f44d080-9582-11eb-9778-e074818cb750.png)

Here's the Amazon stocks details collected from external rest API;
![image](https://user-images.githubusercontent.com/21355015/113519184-8be10880-9582-11eb-8484-2562f55509d0.png)

  
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

### Here's the Welcome page of our application - GET method
![welcome](https://user-images.githubusercontent.com/21355015/113476421-5994b580-9473-11eb-865a-58b7003fdf42.PNG)

### Here's the call to the External Rest API service which displays the stock's name, symbol and price - GET method
![GOOGL](https://user-images.githubusercontent.com/21355015/113476432-6ca78580-9473-11eb-89c6-4c57317a81ed.PNG)

### Here's how the user can register with our platform - POST method
![register](https://user-images.githubusercontent.com/21355015/113476434-6f09df80-9473-11eb-970a-45d163757d96.PNG)

### After registration, the user can login by the below curl command; - POST method 
![login](https://user-images.githubusercontent.com/21355015/113476437-7204d000-9473-11eb-8620-0e299e418704.PNG)
![login2](https://user-images.githubusercontent.com/21355015/113476447-7df09200-9473-11eb-8ded-e81d2d200903.PNG)

### Hash-based Authentication 
![hashed](https://user-images.githubusercontent.com/21355015/113476440-76c98400-9473-11eb-937b-2fce04fb8916.PNG)

### Password reset curl command - PUT method
![reset](https://user-images.githubusercontent.com/21355015/113476445-7c26ce80-9473-11eb-9d41-ff52e2e7db0b.PNG)

### User buys the stock - POST method
![buy](https://user-images.githubusercontent.com/21355015/113476442-792bde00-9473-11eb-9521-7ae5f713f77e.PNG)

### Display of the records of the stocks the user is holding - GET method
![manny's records](https://user-images.githubusercontent.com/21355015/113476411-4a156c80-9473-11eb-9668-5761827a08f1.PNG)

### Curl command to return the stock - DELETE method
![return](https://user-images.githubusercontent.com/21355015/113476452-8052ec00-9473-11eb-9c57-0047500ee475.PNG)

Some of the curl commands that can be used on windows terminal;

curl -i -H "Content-Type:application/json" -X POST -d "{\"name\":\"danny\", \"pswd\":\"blah\"}" http://127.0.0.1:5000/register

curl -i -H "Content-Type:application/json" -X POST -d "{\"name\":\"danny\", \"pswd\":\"blah\"}" http://127.0.0.1:5000/login

curl -i -H "Content-Type:application/json" -X POST http://127.0.0.1:5000/buy/TWTR

docker run --name qmul_cloud -p 5432:5432 -e POSTGRES_DB=stocks -e POSTGRES_USER=dba -e POSTGRES_PASSWORD=dba_pswd -d postgres

curl -i -H "Content-Type:application/json" -X DELETE http://127.0.0.1:5000/return/3

curl -i -H "Content-Type:application/json" -X PUT -d "{\"name\":\"danny\", \"pswd\":\"blah\", \"new_pswd\":\"boo\"}" http://127.0.0.1:5000/reset_password
