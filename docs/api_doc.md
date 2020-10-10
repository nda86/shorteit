# Создать короткий url

Создать короткий url для оригинального url переход по которому будет редиректить на оригинальный url 

**URL** : `/api/v1/shorturls/`

**Method** : `POST`

**Auth required** : None

**Permissions required** : None

**Пример передаваемых данных в post запросе**

.

```json
{
    "original_url": "https://docs.djangoproject.com/en/3.1/ref/models/fields/",
    "user_id": "51e35381713b4268975af6d2b9766578",
    "short_url": "12345"
}
```


## Успешный ответ

```json
{
    "id": 23,
    "short_url": "http://localhost:8000/s/12345",
    "user_id": "51e35381-713b-4268-975a-f6d2b9766578",
    "original_url": "https://docs.djangoproject.com/en/3.1/ref/models/fields/",
    "created_at": "2020-10-10T18:02:51.122663Z",
    "count_click": 0
}
```


# Получить список коротких ссылок пользователя 

**URL** : `/api/v1/shorturls/?user_id=51e35381713b4268975af6d2b9766578`

**Method** : `GET`

**Auth required** : None

**Permissions required** : None


## Успешный ответ

```json
[
    {
        "id": 23,
        "short_url": "http://localhost:8000/s/12345",
        "user_id": "51e35381-713b-4268-975a-f6d2b9766578",
        "original_url": "https://docs.djangoproject.com/en/3.1/ref/models/fields/",
        "created_at": "2020-10-10T18:02:51.122663Z",
        "count_click": 0
    },
    {
        "id": 22,
        "short_url": "http://localhost:8000/s/07d3dfed37",
        "user_id": "51e35381-713b-4268-975a-f6d2b9766578",
        "original_url": "http://www.ya.ru/171086",
        "created_at": "2020-10-10T16:49:20.991557Z",
        "count_click": 0
    }
]
```

# Получить конкретную запись по id

**URL** : `/api/v1/shorturls/23/?user_id=51e35381713b4268975af6d2b9766578`

**Method** : `GET`

**Auth required** : None

**Permissions required** : None


## Успешный ответ

```json
{
    "id": 23,
    "short_url": "http://localhost:8000/s/12345",
    "user_id": "51e35381-713b-4268-975a-f6d2b9766578",
    "original_url": "https://docs.djangoproject.com/en/3.1/ref/models/fields/",
    "created_at": "2020-10-10T18:02:51.122663Z",
    "count_click": 0
}
```