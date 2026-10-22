# SellSync — easiest deployment (single service)

This version builds the React frontend and serves it from the FastAPI backend, so you only need to deploy one service.

## 1. Push to GitHub
1. Extract this ZIP.
2. Create a new GitHub repository, e.g. `sellsync-deploy`.
3. Upload/push the **contents** of this folder to the repository root. Confirm `Dockerfile`, `backend/`, and `frontend/` are at the root (not nested inside another `SellSync_Local/` folder).

## 2. Deploy on Railway
1. Open https://railway.com/ and sign in with GitHub.
2. Choose **New Project** → **Deploy from GitHub repo** and select the repository.
3. Railway should detect the root `Dockerfile` and build the app.
4. When the deployment is built, open the service's **Settings / Networking** section and choose **Generate Domain**.
5. Open the generated public URL. The frontend and `/api` endpoints use the same domain.

## 3. Keep database changes
The app is configured to store SQLite at `/data/sellsync.db` and not to reseed on every restart. To preserve changes, add a Railway Volume mounted at `/data` in the service's Volumes settings, then redeploy. Without the volume, data can be lost when the service is recreated or redeployed. Railway usage/pricing may apply; check your plan before deploying.

## 4. Test before presenting
- Open the public URL and wait for the first load.
- Check dashboard, products, orders, payments, and analytics.
- Create a test product/order and refresh to verify changes persist (requires the `/data` volume).
- Visit `<your-domain>/docs` to see the API documentation.

## Notes
- This is a demonstration app. Marketplace integrations and payment workflows are simulated; do not enter real customer or payment data.
- The app's demo reset function can reset sample data. Avoid using it during the presentation unless intended.
