# Ihouz price estimate demo

## Development setup
### Python version
3.9

### Create virtual environment
```
python -m venv .venv
```

### Activate virtual environment
Windows:
```
.venv\Scripts\activate
```

Linux:
```
source .venv/bin/activate
```

### Install libraries
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Migrate DB
```
python manage.py migrate
```

### Run development server
```
python manage.py runserver
```

Now your website is served at [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/)

### To update price estimation logic, edit code in:
`price_estimate/views.py -> PriceEstimateView`
