# Basic Django API backend - React frontend boilerplate

- Run `pipenv install` in the root of the project.
- Execute `./manage.py migrate`
- Cd to frontend and run `npm i`.
- Start frontend server from `frontend` with `npm run dev`.
- Create `.env` file in the root folder and add `SECRET_KEY` and `DEBUG=True`.
- Start backend server from root with `./manage.py runserver`.
- Create api models in `api` app.
- Create react components in `frontend/src/components/`
- main.js auto generates on watch under `frontend/static/frontend/` and renders in index.html.
- App is live on localhost:8000.
- Api is live on localhost:8000/api (create models, views, serializers and urls in api app)
- A sample model, serializer, view and url path is provided. You may either ignore it and overwrite it or delete the contents of the following files and create your own:
  - ./api/models.py
  - ./api/serializers.py
  - ./api/urls.py
  - ./api/views.py
- Delete afterwards db.sqlite3 and `./api/migrations/0001_initial.py`
- Migrate again to generate a fresh database and write your own views, models, urls and serializers.
