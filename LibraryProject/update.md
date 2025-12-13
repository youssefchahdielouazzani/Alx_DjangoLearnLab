# Commande pour mettre à jour un livre existant (ex: id=1)
curl -X PUT http://localhost:8000/books/1/ \
-H "Content-Type: application/json" \
-d '{"title": "Dune Messiah", "author": "Frank Herbert", "published_date": "1969-10-15", "isbn": "9780441172696", "pages": 256, "language": "English"}'

