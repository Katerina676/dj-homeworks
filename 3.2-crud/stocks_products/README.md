Типовые команды для запуска контейнера c backend-сервером:

1) Создание контейнера из Dockerfile
```
docker build --tag=crud .
```
2) Запуск контейнера
```
docker run -p 8000:8000 -d --name my_stocks_products crud
```