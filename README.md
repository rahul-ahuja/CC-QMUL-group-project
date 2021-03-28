# CC-QMUL-group-project
QMUL Cloud Computing group project


Some of the curl commands to be used on windows terminal;

curl -i -H "Content-Type:application/json" -X POST -d "{\"name\":\"danny\", \"pswd\":\"blah\"}" http://127.0.0.1:5000/register

curl -i -H "Content-Type:application/json" -X POST -d "{\"name\":\"danny\", \"pswd\":\"blah\"}" http://127.0.0.1:5000/login

curl -i -H "Content-Type:application/json" -X POST http://127.0.0.1:5000/buy/TWTR

docker run --name qmul_cloud -p 5432:5432 -e POSTGRES_DB=stocks -e POSTGRES_USER=dba -e POSTGRES_PASSWORD=dba_pswd -d postgres

curl -i -H "Content-Type:application/json" -X DELETE http://127.0.0.1:5000/return/3

curl -i -H "Content-Type:application/json" -X PUT -d "{\"name\":\"danny\", \"pswd\":\"blah\", \"new_pswd\":\"boo\"}" http://127.0.0.1:5000/reset_password


