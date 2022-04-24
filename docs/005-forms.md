# Django From

### Create a Django Thread Form 


### ModelForm
* Some form maps closely to Django Model
* It would be redundant to define the field types in the form as it's already defined in models.
* Django provides helper class, to create a form from Django Model.


```python
from django.forms import ModelForm

class LoginForm(ModelForm):

```
