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
