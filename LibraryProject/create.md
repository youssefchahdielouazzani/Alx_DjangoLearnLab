# Commande pour créer un livre via l'API
curl -X POST http://localhost:8000/books/ \
-H "Content-Type: application/json" \
-d '{"title": "Dune", "author": "Frank Herbert", "published_date": "1965-08-01", "isbn": "9780441013593", "pages": 412, "language": "English"}'

