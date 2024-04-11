# prefect-docker-compose

Local testing with docker compose.

```bash
# Start the services in the background
docker compose up -d

# Create and use a profile pointing to the services
prefect profile create compose
prefect profile use compose
prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api

# Open the UI in your default browser
open http://127.0.0.1:4200/

# Deploy the flows
python deploy.py
```
