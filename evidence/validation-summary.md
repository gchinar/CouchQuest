# Verified checks

- Catalog pytest suite: 4 passed.
- Session pytest suite: 8 passed.
- Live local HTTP workflow: 11 expected status checks passed; final session COMPLETED.
- Docker Compose config: parsed successfully.
- Kubernetes YAML: parsed; 11 resource documents and matching Deployment selectors checked.
- Postman collection: JSON parsed; 11 requests.

Tests used separate SQLite databases. Live API checks used two Uvicorn processes and real HTTP between them. A TestClient deprecation warning was emitted by the installed framework; it did not fail the tests.

Not executed: Docker builds/runtime, PostgreSQL runtime, Minikube deployment, Kubernetes server-side validation, HPA scaling, GitHub Actions, Postman application execution. These need the student's execution evidence.
