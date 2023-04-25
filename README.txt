# littlelemon_repo
Capstone Project

Mysql:
DATABASE:  littlelemon
USER:	root
PASSWORD:	root

API end points
Project level urls.py

django admin:	http://127.0.0.1:8000/admin/'
djoser urls:    http://127.0.0.1:8000/auth/<several of them>
api-token-auth to be tested with a POST request with username and password in INSOMNIA
		http://127.0.0.1:8000/restaurant/api-token-auth/

App level urls.py
http://127.0.0.1:8000/restaurant/menu
http://127.0.0.1:8000/restaurant/menu/<id>  (for single menuitem operations like put, patch, delete
http://127.0.0.1:8000/restaurant/booking/tables/ (for table booking)

TEST
----
In views.py file, In MenuItemView View, comment out 
permission_classes = [IsAuthenticated]
Otherwise test on view will fail.
This view requires token authentication.  I don't know how to provide token authentication in test.
