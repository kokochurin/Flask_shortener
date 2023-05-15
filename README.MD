# Укорачиватель ссылок

Сервис, на котором все желающие могут сделать короткую ссылку вместо длинной

## Технологии

* Python
* Flask
* WTForm
* SQLAlchemy

## Как запустить

1. клонировать репозиторий

```commandline
git clone [link]
```

2. установить виртуальное окружение и запустить его

```commandline
python -m venv venv
Windows: venv\Scripts\activate
Linux: source venv/bin/activate
GitBash: source venv/Scripts/activate
```

3. установить зависимости
```commandline
pip install -r requirements.txt
```
4. создать файл .env и добавить конфигурацию
```text
nano .env
SECRET_KEY=YOUR_SECRET_KEY
DATABASE_URI=sqlite:///db.sqlite3
```
5. запуск приложения
```commandline
flask --debug run
```
