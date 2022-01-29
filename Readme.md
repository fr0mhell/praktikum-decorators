# Материалы к вебинару "Декораторы в Python"

## Установка

1. Создаем и активируем виртуальное окружение
2. Устанавливаем зависимости `pip install -r requirements.txt`
3. Регистрируемся на сайте [The Cat API](https://thecatapi.com/)
4. Создаем в корневой папке файл `constants.py` и добавляем туда:
    ```python
    API_KEY = '%API ключ, пришедший после регистрации%'
    ```

## Скачиваем котиков!

Запускай `python main.py` и смотри, 
с какой скоростью скачиваются картинки с котиками в зависимости от количества потоков!

Полную API документацию ищи [здесь](https://docs.thecatapi.com/api-reference/images/images-search)

## Запускаем в docker!

Собираем образ

```shell
docker build . -t catloader
```

Запускаем образ в новом контейнере

```shell
docker run catloader
```

Создаем именованный контейнер для многократного запуска

```shell
docker create --name catloader catloader
```

Проваливаемся внутри контейнера

```shell
docker start catloader
docker exec -it catloader /bin/bash
```
Запускаем контейнер с папкой проекта в качестве volume

```shell
docker run -v "$(pwd)":/catloader  --rm catloader
```
