#!/bin/sh

# Start server
echo "Starting server"
#!/bin/sh

sleep 3
exec "$@"

exec python ./src/manage.py runserver 0.0.0.0:8000 
