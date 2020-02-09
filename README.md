# test-prj-user_orders

## Descriptions

Application provides infornation about users and their orders

## Tools

* Python
* Flask
* SQLAlchemy
* Jinja2

## Requirements

To install requirements run:  
```$ pip install -r requirements.txt```

## How to run

If you already have database, specify it in ```user_project/config.py```

If you want to run application with test database, create it  
```$ python init_data.py```

Then run application:  
```$ python main.py```

## Tests

You need pytest to be istalled:  
```$ pip install pytest```

To run tests use:  
```$ python -m  pytest```
