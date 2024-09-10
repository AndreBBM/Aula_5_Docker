### Run the application

```bash
docker build -t my_test_server .
docker run -p 8080:8080 -v ${PWD}/src:/app/src my_test_server
```

access the application at http://localhost:8080