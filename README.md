# ClientSphere — CRM assessment implementation (partial)

An original educational monorepo based on the ClientSphere Project 06 PDF. **Not a complete or production-ready implementation of all 15 assessments.**

## Run
1. Copy `.env.example` to `.env` and replace `JWT_SECRET` with a random 32+ character secret.
2. Run `docker compose up --build`.
3. Open http://localhost:3000. Create an organization and then sign in.
4. API http://localhost:4000/health; FastAPI documentation http://localhost:8000/docs.

## Implemented
- PostgreSQL CRM entities, including many-to-many contact/company and opportunity/member relationships.
- Basic JWT login, admin bootstrap, organization-scoped CRUD endpoints for seven entities, simple admin/manager delete permission.
- Contact/company linking, opportunity/team linking, basic weighted forecast.
- Simple Next.js dashboard for CRUD creation/listing, Python lead scoring and forecast, Docker Compose and basic CI tests.

## Not implemented / limitations
- Full team/owner record visibility, secure multi-tenant isolation for every relational path, field-level permissions, and audit writes.
- Complete Kanban, import wizard, CSV deduplication, workflow automation workers, integration providers, event retry and deduplication.
- Complete OpenAPI/Postman docs, coverage, real integration and browser tests, production deployment/HTTPS/backup/restore, incident evidence.
- Bootstrap endpoint is unrestricted: disable/protect it before any public deployment. Login email is not globally unique across organizations; extend login with organization identity for production.
- No live GitHub repository, deployed URL, or verified end-to-end test evidence is included.

## API examples
`POST /auth/bootstrap` with `{ "organization":"Demo", "email":"admin@example.com", "password":"a-long-demo-password" }`.
`POST /auth/login` with `{ "email":"admin@example.com", "password":"a-long-demo-password" }`.
Use `Authorization: Bearer <token>` for `/api/leads`, `/api/contacts`, `/api/companies`, `/api/opportunities`, `/api/pipelines`, `/api/activities`, `/api/automation_rules`.

## Tests
`cd api && npm install && npm test`; `cd intelligence && pip install -r requirements.txt && pytest -q`.

## GitHub publishing
Install/authenticate GitHub CLI, then `git init && git add . && git commit -m "Initial ClientSphere implementation" && gh repo create clientsphere --private --source=. --remote=origin --push`.
