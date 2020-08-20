# Django Database

## Django Models
For example: Suppose our application is blogging application, which needs a table **posts** in database to store our blog article. Create a file **posts.py** inside models folder of your apps.

```python
# File: front/models/posts.py
from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
After defining the defination of tables in above class, further it is required to make migrtions from above definations by running below commands as: 
```bash
python manage.py makemigrations
```

Executing the above command creates a migrations folders inside your application, which contains migration files. Migration file will responsible for creating as well as modifying database schemas. Run the below command to create posts table in our database.
```bash
python manage.py migrate
```