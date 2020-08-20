# Testing

## Django Testing a CRUD operation
Suppose a blog has a feature that a login user can post a Thread. We are going to perform follwing tests:
1. User can create a Thread. (Thread is stored in the database.)
2. Thread owner can edit the thread. (No other user or guest cab edit)
3. Thread owner can delete the thread.
4. All the threads are listed in the home page.
5. Thread can read by anyone. 

### Test user can access a thread post form
Suppose, we have created a thread post form in the url ```/threads/create```. We are only testing that 200 status for this form. For details form data and user behaviour test, we should perform selenium based browser test. For now we are assuming that asseting 200 response on that url means there is no any errors.

```python
# File: tests/test_thread.py
from django.test import TestCase
from django.test import Client


class ThreadTest(TestCase):

    def test_user_can_access_thread_post_form(self):
        response = self.client.get('/thread/create')
        self.assertEqual(response.status_code, 200)
```
