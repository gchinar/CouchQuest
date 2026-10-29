# Submission completion checklist

- [ ] Add actual name, student ID, group number and all group member details to SOLUTION.docx.
- [ ] Read, understand and adapt the implementation to your group's work and course rules.
- [x] Publish catalog-service and session-service as two separate GitHub repositories.
- [x] Replace the repository placeholders in the report with real links.
- [ ] Run each repository's tests independently.
- [ ] Run Docker Compose and verify the four containers and complete API workflow.
- [ ] Run the Minikube deployment; verify PostgreSQL-backed API responses.
- [ ] Import and run the Postman collection; capture real API request/response screenshots.
- [ ] Capture dashboard Deployments, Pods, Services and persistent volume evidence.
- [ ] Demonstrate scaling Session to two pods and retrieval after an API restart.
- [ ] Insert your screenshots and observations into the report's evidence section.
- [ ] Record a demonstration video; include it in the final ZIP or use an instructor-approved link.
- [ ] Rename the report and final ZIP with your actual student ID; final ZIP pattern: STUDENT_ID_CouchQuest.zip.
- [ ] Remove placeholder text and confirm every link/file works before LMS upload.

## Suggested six minute video sequence

0:00–0:45 — Introduce CouchQuest, local split-screen use case and architecture.
0:45–1:15 — Show two repositories and independent Dockerfiles and tests.
1:15–2:00 — Show Minikube context, deployments, pods, services and PVCs.
2:00–3:45 — Create game, create session, join Bob, reject a third player, set readiness, start and finish.
3:45–4:30 — Open Kubernetes dashboard and explain each workload and the separate databases.
4:30–5:15 — Scale Session to two replicas and show Ready pods.
5:15–6:00 — Restart Session API, retrieve the saved session and explain remaining production work.

This is a recording script, not a supplied demonstration video. Capture your actual run.
