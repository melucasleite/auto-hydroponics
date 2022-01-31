start_frontend:
	cd frontend && npm start

start_backend:
	cd backend && python3 manage.py runserver

make start:
	make start_frontend & make start_backend