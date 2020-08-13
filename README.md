## Application Setup

### virtual environment
```
$ python -m venv venv

$ source venv/bin/activate
```

### dependencies
```
$ pip install -r requirements.txt
```

### Populate databse with data file
```bash
$ mongoimport --type csv -d pubnative -c case_study --fields _id,price,expiration_date data/data.csv
```

### Run the application
```
$ python app.py
```

### Check running application
> http://localhost:8080

## Example API calls from shell

```bash
$ curl http://0.0.0.0:8000/promotions/e2649ca5-7e05-4d53-a8ff-919917a4922e
{
  "expiration_date": "2018-08-22 18:34:11", 
  "id": "e2649ca5-7e05-4d53-a8ff-919917a4922e", 
  "price": 66.64
}

$ curl http://0.0.0.0:8000/promotions/e2649ca5-7e05-4d53-a8ff-919917a4922ee
{
  "Error": "Not found"
}
```
