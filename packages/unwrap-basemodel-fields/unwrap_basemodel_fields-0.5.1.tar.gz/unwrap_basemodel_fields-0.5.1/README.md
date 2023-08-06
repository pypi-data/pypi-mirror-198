# :recycle: Unwrapper pydantic optional fields :recycle:


Unwrapper stores a **Result** object to implement unpacking of values if they are not **None**. The **BaseModel** object is also a little extended to work with the **Result** object.


# :star: A simple example :star:
```python
from unwrapper import BaseModel, Result

class User(BaseModel):
    name: Result[str]
    age: int

data = {
    "age": 20
}
user = User(**data)
#> User(name=Result(None), age=20)
print("Hello", user.name.unwrap(error_msg="What's your name?"), "!")
#> ValueError: What's your name?
```

# :book: Documentation :book:
* In :ru: [**Russian**](https://github.com/luwqz1/unwrap_basemodel_fields/blob/main/docs/RU.md) :ru:
* In :us: [**English**](https://github.com/luwqz1/unwrap_basemodel_fields/blob/main/docs/EN.md) :us:
