# IMDB_API_Clone
IMDB API Clone With DRF

1. Admin Access

Admin Section: http://127.0.0.1:8000/dashboard/

2. Accounts

Registration: http://127.0.0.1:8000/api/account/register/

Login: http://127.0.0.1:8000/api/account/login/

Logout: http://127.0.0.1:8000/api/account/logout/

3. Platforms

Create Element & Access List: http://127.0.0.1:8000/api/watchlist/platform/

Access, Update & Destroy Individual Element: http://127.0.0.1:8000/api/watchlist/platform/<str:name>/

4. Watch List

Create & Access List: http://127.0.0.1:8000/api/watchlist/list/

Access, Update & Destroy Individual Element: http://127.0.0.1:8000/api/watchlist/list/<int:pk>/

5. Reviews

Create Review For Specific Movie: http://127.0.0.1:8000/api/watchlist/<int:pk>/reviews/create/

List Of All Reviews For  Movie: http://127.0.0.1:8000/api/watchlist/reviews/

Access, Update & Destroy Individual Review: http://127.0.0.1:8000/api/watchlist/<int:pk>/reviews/
