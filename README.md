<div align="center">

# Recetario • Cloud-Native Vercel Serverless Edition
### *Serverless Python Architecture, Stateless WSGI Adapter & Edge Deployment Pipeline*

[![Vercel Deployment](https://img.shields.io/badge/Vercel-Serverless_Live-black?style=for-the-badge&logo=vercel)](https://vercel.com)
[![Python: 3.9+](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask: Serverless](https://img.shields.io/badge/Flask-WSGI_Serverless-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Bootstrap 5](https://img.shields.io/badge/UI-Bootstrap_5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<p align="center">
  The production cloud-ready edition of the Recetario culinary platform, optimized for zero-cold-start edge distribution and serverless container execution on Vercel infrastructure.
</p>

</div>

---

## ☁️ Cloud & Serverless Optimizations

- **Vercel Serverless Routing (`vercel.json`):** Directs incoming HTTP traffic into serverless WSGI Python invocations.
- **Stateless Database Integration:** Decoupled SQLite/PostgreSQL connection patterns accommodating serverless function lifecycles.
- **Pre-Compiled Static Asset Delivery:** High-speed edge CDN caching for static styles, scripts, and media files.
- **Automated Database Seeding:** Dedicated `init_db.py` routine for reproducible schema setup in distributed environments.

---

## 🚀 Local Execution & Vercel Deployment

```bash
# Clone the repository
git clone https://github.com/ExeDevCentral/RecetarioUpgradeParaVercel.git
cd RecetarioUpgradeParaVercel

# Install local dependencies
pip install -r requirements.txt

# Run locally
python3 app.py

# Or deploy to Vercel via Vercel CLI
npx vercel
```

---

## 👨‍💻 Author

**Exequiel Echevarria**
- GitHub: [@ExeDevCentral](https://github.com/ExeDevCentral)
