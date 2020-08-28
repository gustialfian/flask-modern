# flask-modern

## Install
```
sudo apt install python3-pip
sudo apt install libpq-dev

python3 -m pip install --upgrade --user virtualenv
python3 -m virtualenv -p python3 venv
venv/bin/pip install -r requirements.txt
```

## RUN
```bash
venv/bin/python app.py
```

## dependency 
run this command after add new dependency
```bash
venv/bin/pip freeze > requirements.txt
```