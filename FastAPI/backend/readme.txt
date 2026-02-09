pip install fastapi uvicorn pymysql
uvicorn main:app --reload

http://127.0.0.1:8000

http://127.0.0.1:8000/docs

curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=apple' #додає елементи до списку
curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=orange' #додає елементи до списку
curl -X GET http://127.0.0.1:8000/items/1 #отримує інформацію про елемент 1

curl -X POST -H "Content-Type: application/json" -d '{"text":"apple"} 'http://127.0.0.1:8000/items' #передаємо інформацію
конкретний обєкт apple
