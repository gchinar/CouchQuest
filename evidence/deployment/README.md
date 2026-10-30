# Part 3 deployment evidence

Executed on 30 October 2026. The service sources are maintained in separate repositories: [Catalog](https://github.com/gchinar/couchquest-catalog) and [Session](https://github.com/gchinar/couchquest-session). CouchQuest pins them as Git submodules, not duplicate maintained source trees. Each service has its own tests, dependencies, Dockerfile, CI and Kubernetes deployment files.

## Completed steps

| Requirement | Observed result | Evidence |
| --- | --- | --- |
| Separate Docker containers | Two API containers and two separate PostgreSQL containers running | docker-containers.txt |
| Docker application integration | 11 HTTP checks passed, final state COMPLETED | docker-http.json |
| Local Kubernetes deployment | Minikube 1.39.0, Kubernetes 1.35.0, Docker driver, 2 CPUs, 2800 MB | kubernetes-rollout.txt |
| Kubernetes application integration | 11 checks passed against PostgreSQL-backed APIs | kubernetes-http.json |
| Dashboard inspection | All four deployments healthy; Session 2/2 and others 1/1 | dashboard-deployments.png |
| Independent scaling | Session scaled to two ready pods; Catalog remained one | scaled-resources.txt |
| Persistence | Same completed session retrieved after rolling API restart | persistence-after-restart.json |
| CI/CD | Tests, image builds, cluster deployment, HTTP verification and artifact upload all succeeded | ci-run.json |

## Dashboard analysis

Catalog is 1/1 available, Session 2/2, and both databases 1/1. The Session API scales independently and both replicas use session-db; durable data does not reside in API memory. Four ClusterIP Services expose API port 8000 and database port 5432 only within the cluster. Each service owns a separate Bound 1 GiB PVC. The successful GET after Session restart verifies application data persistence across that API restart, not database disaster recovery.

The initial API pods each restarted twice while their databases initialized. The Catalog pod retained this count in the initial final-resources snapshot; replacement Session pods had zero restarts. Startup dependencies should use retry/backoff or a separate migration job for production. Dashboard CPU/memory graphs were still waiting for samples in the captured deployment view. The separate resource-usage.txt file contains actual metrics-server readings; it is a snapshot, not a load benchmark. HPA is optional and was not enabled; the two Session replicas were manually requested.

## CI/CD options and implementation

1. **GitHub-hosted Minikube (implemented):** each service has independent tests and Docker-build CI. The coordinating workflow checks out pinned service commits, repeats tests, builds both images, creates an isolated Minikube cluster, deploys APIs/databases, runs the full HTTP flow, saves evidence, and removes the temporary CI cluster. It needs no long-lived cloud credentials. This is a repeatable deployment test environment.
2. **Self-hosted runner on a local machine (considered):** could deploy to a persistent local cluster, but requires a maintained runner and careful isolation of untrusted pull requests. Not configured.
3. **Registry plus GitOps controller (considered):** publish immutable image digests and promote manifests through review to a persistent cluster. Appropriate for a future production environment; registry publication and GitOps are not configured here.

Successful run: https://github.com/gchinar/CouchQuest/actions/runs/40999250344
Workflow: ../../.github/workflows/deploy.yml

The CI deployment is temporary on GitHub's runner. The local couchquest Minikube deployment is separate. Main-branch changes to deployment inputs or pinned submodules trigger CI/CD; workflow_dispatch also permits manual execution. Updating a service requires promoting its tested commit in the coordinating repository. Deployment logs are uploaded as the minikube-deployment-evidence Actions artifact.

Postman desktop screenshots, personal details and a recorded video remain submission tasks. No recording or automatic scaling benchmark is claimed.

## Recovery verification

After resuming later on 30 October, Minikube required a restart and context endpoint refresh. All four deployments recovered, both PVCs remained Bound, and 11 HTTP checks passed again. The original completed session was also retrieved successfully. See recovered-resources.txt, recovered-http.json, recovered-metrics.txt, dashboard-recovered.png and persistence-after-cluster-restart.json. Restart counts in this later snapshot include cluster recovery and differ from the initial capture.
