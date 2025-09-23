# pgvector_sample
- PostgreSQL pgvector sample

# 项目依赖环境
```bash
conda create -n pgvector_sample python=3.10.6
conda activate pgvector_sample
pip install django
django-admin startproject pgvector_sample
pip install djangorestframework
pip install psycopg[binary]
pip install pgvector
```


```bash
pip install sentence-transformers
pip install hf_xet
pip install protobuf
```



# 配置
```bash
python manage.py startapp app

```


```

INSTALLED_APPS [
...省略...
'rest_framework',
'app',
]

```


```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vector_sample',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

```

# 生成表

```
python manage.py makemigrations
python manage.py migrate

```

# 访问
- http://127.0.0.1:8000/api/
# 参考
- https://github.com/pgvector/pgvector-python
- https://juejin.cn/post/7337579872746127369