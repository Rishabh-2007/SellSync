# SellSync — Unified Commerce Cockpit for Indian Micro-Sellers

> **Tagline:** One simple cockpit. Every sales chat & channel. Zero stockouts.  
> Developed for the **MDMIE01 entrepreneurship project**.

SellSync is a unified commerce management platform engineered specifically for **Indian micro-sellers**: Instagram boutiques, home bakers, social commerce resellers, and handmade artisan shops who run their businesses via WhatsApp, Instagram DMs, and regional marketplaces.

---

## 1. Product Vision & Architecture

Indian micro-sellers are informal, solopreneur, or family-run businesses. They don't have dedicated IT staff or ERP training. They juggle WhatsApp chats, Instagram DMs, UPI notification SMS messages, and delivery apps—leading to frequent stockouts, double-booking, missed payments, and courier dispatch delays.

SellSync replaces that chaos with a streamlined, honest operating cockpit:
- **Central Single-Source-of-Truth Inventory**: All listings connect back to a single inventory record:
  $$\text{Available Stock} = \text{Stock on Hand} - \text{Reserved Stock}$$
  Frictionless 1-tap `+` / `-` stock adjustments right from your phone.
- **Micro-Seller Order Lifecycle**:
  $$\text{NEW} \rightarrow \text{AWAITING\_PAYMENT} \rightarrow \text{CONFIRMED} \rightarrow \text{PROCESSING} \rightarrow \text{READY\_TO\_DISPATCH} \rightarrow \text{DISPATCHED} \rightarrow \text{DELIVERED}$$
- **Deterministic WhatsApp / Chat-to-Order Parser**: Converts messy customer chat text into structured orders with Indian mobile validation (+91), 6-digit PIN code verification, city matching, and local catalog SKU lookup—no external cloud AI or data leakage.
- **UPI Payment Reconciliation Assistant**: Cross-checks bank SMS amounts and UTR references against pending orders, flags exact matches, shortfalls, and excess payments, and provides 1-click order confirmation.
- **Dynamic UPI QR & Deep Links**: Generates NPCI-compliant `upi://pay` QR codes and formatted WhatsApp payment request links with 1 click.
- **Dual Fulfillment Routing**:
  - *Physical Courier Parcels* (Delhivery / BlueDart / India Post / Porter) with 1-click clipboard address formatting and printable 4x6" shipping labels.
  - *Food Delivery / Fresh Kitchen Handover* (Swiggy / Zomato kitchen status & rider handover OTPs).
- **Day-End Close Summary**: 1-click financial day-end reconciliation calculating collected revenue, pending payments, dispatched parcels, and CSV ledger export.
- **Bilingual Interface**: Full toggleable English and Hindi (`[EN | हिंदी]`) localization for intuitive everyday use.

---

## 2. Four Realistic Micro-Seller Personas

SellSync includes 4 distinct pre-configured Indian micro-seller personas. Switch between them instantly using the **Persona Switcher** in the top navigation bar or under **Settings**:

| Persona | Business Name | Location | Category | Primary Channels | Fulfilment Type |
|---|---|---|---|---|---|
| **`boutique`** | Ananya Sarees & Kurtis | Kolkata / Jaipur | Handcrafted Ethnic Wear | Instagram Direct, WhatsApp Business, Meesho | Courier Parcel (Delhivery / BlueDart) |
| **`baker`** | SweetWhisk Studio | Bandra, Mumbai | Home Bakery & Desserts | WhatsApp Business, Swiggy, Zomato | Fresh Delivery / Rider OTP Handover |
| **`reseller`** | Pooja Closet Finds | Indore | Curated Thrift & Jewelry | Instagram Direct, WhatsApp Business, Meesho | Courier Parcel (India Post / Porter) |
| **`handmade`** | Mitti Magic Studio | Khurja / Delhi | Terracotta & Ceramic Pottery | Instagram Direct, WhatsApp Business, Amazon Handmade | Heavy / Fragile Courier Box |

> **Persona Channel Isolation**: In accordance with domain rules, food aggregators (*Swiggy* and *Zomato*) are strictly restricted to food businesses (`baker`) and never appear in fashion, craft, or reseller accounts.

---

## 3. Technology Stack

- **Frontend**:
  - React 18 with TypeScript & Vite tooling
  - Tailwind CSS with rich slate/navy theme tokens
  - Lucide React icons
  - Recharts for business analytics
  - Custom English/Hindi i18n Context (`frontend/src/i18n`)
  - Touch-friendly mobile bottom navigation bar (`< 768px`)
- **Backend**:
  - Python 3.12 with FastAPI
  - Pydantic v2 schemas and validation
  - SQLAlchemy 2.0 ORM with SQLite database
  - Uvicorn ASGI server
  - Pytest automated test suite (24 passing test suites)

---

## 4. Non-Negotiable Honesty & Transparency Rules

SellSync is designed with uncompromising academic and operational integrity:

1. **Simulated Marketplace Connectors (`DEMO MODE`)**:
   External channels (Amazon, Meesho, Swiggy, Zomato) are clearly badged as **"Demo connections (Sample Data)"** with realistic mock sync loops. No live credentials, external API keys, or simulated bank logins are required.
2. **Local Feature Distinction (`LOCAL FEATURE`)**:
   Manual direct orders, WhatsApp chat parsing, UPI QR generation, and stock steppers run 100% locally on the device with zero external dependencies.
3. **Zero Fabricated Customer Data**:
   The **Customer Validation Tracker (`/validation`)** contains **0 fake interviews, 0 fabricated quotes, and 0 phantom traction figures**. All metrics are strictly computed from real interviews logged by the founder. All business model assumptions begin as `"Untested"`.
4. **Hypothesis Labeling**:
   All pricing tiers (Free ₹0, Starter ₹299/mo, Growth ₹799/mo) are explicitly tagged as **"Hypothesis — to be tested"**.

---

## 5. Project Directory Structure

```
FIE/
├── backend/
│   ├── app/
│   │   ├── main.py                     # FastAPI application entrypoint & lifespan
│   │   ├── config/
│   │   │   ├── __init__.py             # App configuration settings
│   │   │   └── personas.py             # 4 micro-seller personas & channel rules
│   │   ├── db/
│   │   │   └── session.py              # SQLite engine & sessionmaker
│   │   ├── models/                     # SQLAlchemy models (Order, Product, Channel, Payment, etc.)
│   │   ├── schemas/                    # Pydantic schemas (Request/Response validation)
│   │   ├── services/
│   │   │   ├── chat_parser_service.py  # Rule-based Indian WhatsApp chat-to-order extractor
│   │   │   ├── payment_helper_service.py # UPI UTR and amount match assistant
│   │   │   ├── seed_service.py         # Persona-specific sample data seeding
│   │   │   ├── inventory_service.py    # Available stock calculation & reservations
│   │   │   ├── order_service.py        # Order transitions & activity logging
│   │   │   ├── payment_service.py      # Payment states & settlement reconciliations
│   │   │   ├── validation_service.py   # Customer interview & hypothesis tracker
│   │   │   └── analytics_service.py    # Revenue & channel breakdowns
│   │   └── api/                        # REST endpoints (orders, payments, products, demo, etc.)
│   ├── tests/
│   │   ├── test_business_logic.py          # Core inventory & payment unit tests
│   │   ├── test_startup_business_logic.py  # Customer validation tracker tests
│   │   ├── test_phase1_personas_and_rules.py # Persona channel segregation tests
│   │   └── test_micro_seller_workflows.py  # Chat parser, UPI helper & data wipe tests
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── api/client.ts               # Fully-typed API client
│   │   ├── types/index.ts              # TypeScript interfaces
│   │   ├── i18n/index.tsx              # Bilingual English/Hindi dictionary & context
│   │   ├── components/
│   │   │   ├── layout/                 # Sidebar, Topbar (with persona & lang switcher), MobileNav
│   │   │   ├── common/                 # StatusBadge, ChannelBadge, Modal, SearchModal
│   │   │   ├── payments/               # PaymentCheckHelper, UpiQrGenerator
│   │   │   └── modals/                 # ChatToOrderModal, DayEndSummaryModal, OnboardingModal, etc.
│   │   ├── pages/
│   │   │   ├── TodayPage.tsx           # Daily operating cockpit with 4 action cards
│   │   │   ├── OrdersPage.tsx          # Order inbox with "Paste Chat" & 1-click address copy
│   │   │   ├── ProductsPage.tsx        # Catalog with 1-tap + / - stock steppers
│   │   │   ├── PaymentsPage.tsx        # UPI checker, dynamic QR generator & settlements
│   │   │   ├── FulfilmentPage.tsx      # Courier shipping labels & rider handover OTPs
│   │   │   ├── ChannelsPage.tsx        # Channel hub with honest simulated connection cards
│   │   │   ├── CustomerValidationPage.tsx # Clean discovery log & assumption matrix
│   │   │   ├── BusinessModelPage.tsx   # Lean canvas & hypothesis-badged unit economics
│   │   │   ├── PresentationSummaryPage.tsx # 9-slide academic pitch deck
│   │   │   └── SettingsPage.tsx        # Persona switch, JSON export, and data wipe
│   │   ├── App.tsx                     # Main shell with route state & onboarding trigger
│   │   ├── main.tsx
│   │   └── index.css                   # Global styles & responsive utilities
│   ├── package.json
│   ├── vite.config.ts
│   └── tailwind.config.js
├── run.bat                             # One-click Windows starter
├── run.ps1                             # PowerShell starter script
├── run.sh                              # Bash script for Linux/macOS
└── README.md
```

---

## 6. How to Run Locally

### Prerequisites
- **Python 3.10+** (with `pip` and `venv`)
- **Node.js 18+** & `npm`

### Quick Start (One Command)
- **Windows (PowerShell)**: `.\run.ps1`
- **Windows (Command Prompt / Double-Click)**: `run.bat`
- **macOS / Linux**: `./run.sh`

### Manual Setup

#### 1. Backend Server
```bash
cd backend
python -m venv venv

# Windows:
.\venv\Scripts\activate
# macOS/Linux:
# source venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```
- API Base URL: `http://127.0.0.1:8000`
- Swagger Interactive Docs: `http://127.0.0.1:8000/docs`

#### 2. Frontend Development Server
```bash
cd frontend
npm install
npm run dev
```
- Web Application URL: `http://127.0.0.1:5173`

---

## 7. Running the Automated Test Suite

The backend includes 24 automated unit and integration tests covering business logic, inventory safety, payment reconciliation, persona isolation, and micro-seller parsing.

Run the test suite from the `backend/` folder:

```bash
cd backend

# Windows PowerShell:
.\venv\Scripts\python.exe -m pytest tests -v

# macOS / Linux:
./venv/bin/pytest tests -v
```

### Verified Test Capabilities:
1. `test_inventory_available_stock_formula`: Verifies $\text{Available} = \text{On Hand} - \text{Reserved}$.
2. `test_order_creation_reserves_stock`: Confirms stock is held upon order entry.
3. `test_payment_verification_confirms_order`: Verifies automatic state transition to `CONFIRMED`.
4. `test_payment_failure_does_not_confirm`: Prevents order confirmation if payment is rejected.
5. `test_payment_mismatch_creates_alert`: Alerts seller when customer pays incorrect amount.
6. `test_dispatch_order_commits_stock`: Verifies reserved stock is permanently deducted upon shipping.
7. `test_cancel_order_releases_stock`: Restores available inventory upon cancellation.
8. `test_stock_adjustment_safety`: Rejects negative inventory balances.
9. `test_customer_interview_crud_and_metrics`: Validates discovery log math and metrics.
10. `test_business_assumptions_register`: Validates assumption status tracking.
11. `test_validation_experiments_planner`: Tests hypothesis experiment logging.
12. `test_all_four_personas_exist`: Validates boutique, baker, reseller, and handmade configs.
13. `test_non_food_personas_do_not_have_swiggy_zomato`: Enforces channel segregation.
14. `test_baker_persona_has_food_channels`: Confirms baker receives Swiggy and Zomato.
15. `test_chat_parser_flow`: Validates Indian phone (+91), PIN code, city, and item extraction.
16. `test_payment_match_helper_flow`: Validates UPI UTR and amount matching logic.
17. `test_day_end_summary_endpoint`: Validates financial reconciliation calculations.
18. `test_data_export_and_clean_delete`: Tests JSON export and clean-slate data wipe.

---

## 8. Guided Walkthrough & Demo Flow

To experience SellSync like an Indian micro-seller:

1. **Start the App**: Open `http://127.0.0.1:5173/`.
2. **Onboarding Wizard**: If visiting for the first time, the 3-step setup modal asks:
   - What kind of micro-seller are you? (Boutique, Baker, Reseller, Handmade)
   - Where do you get orders? (WhatsApp, Instagram, Meesho, etc.)
   - How do you deliver? (Parcels vs Direct Handover)
3. **Today Cockpit (`/today`)**:
   - Inspect the 4 primary cards: **Payments to check**, **Orders to pack**, **Ready to ship**, and **Low stock**.
   - Check the quick actions bar: *Paste Chat*, *Create Direct Order*, *Check Payments*, *Day-End Summary*.
4. **Paste WhatsApp Chat to Order**:
   - Click **Paste Chat** on the Today Cockpit or Orders page.
   - Paste a sample message:
     ```
     Hi didi, please send 2 Linen Shirts to Ananya Roy, 42 Park Street, Flat 3B, Kolkata 700016. Phone 98301 12345. Will pay via GPay.
     ```
   - Click **Extract Details**. Notice the phone, PIN code, address, and matched catalog items are automatically extracted. Click **Create Order**.
5. **Check Payment & Generate Dynamic UPI QR**:
   - Head to **Payments (`/payments`)**.
   - Use the **Check Received UPI Payment** assistant: enter Amount ₹2,499 and UTR reference to find the matching pending order with 1-click confirmation.
   - Switch to the **Create Payment Link / UPI QR** tab: enter an amount and order reference to view an NPCI-compliant QR code and 1-click WhatsApp payment request link.
6. **1-Tap Stock Updates**:
   - Open **Products (`/products`)**. Use the inline `+` and `-` buttons next to any item to quickly update physical stock on hand.
7. **Copy Courier Address**:
   - On **Orders (`/orders`)** or **Fulfilment (`/fulfilment`)**, click **Copy Address** to copy a standardized address block formatted for Delhivery, Porter, or India Post.
8. **Day-End Close**:
   - Click **Day-End Summary** on the Today Cockpit to review today's collected money, pending cash, and shipped packages. Download the ledger as a CSV.
9. **Founder & Academic Startup Hub**:
   - Check **Customer Discovery (`/validation`)** to see the clean, un-fabricated discovery log ready for real user interviews.
   - Review **Business Model (`/business-model`)** with hypothesis-badged pricing and unit economics.
   - View the 9-slide **Presentation Deck (`/presentation-summary`)**.
10. **Data Ownership & Clean Slate**:
    - Under **Settings (`/settings`)**, click **Export My Data** to download a JSON archive, or click **Delete My Data (Clean Slate)** to wipe all demo orders and start with an empty book.

---

## 9. Academic Project Context

- **Course:** MDMIE01 Entrepreneurship Project
- **Market Focus:** Indian Informal & Micro-Retail Commerce (Instagram DMs, WhatsApp, Home Businesses)
- **Primary Design Principle:** Plain-language, low-cognitive-load operations without deceptive growth metrics or fake platform traction.

## One-click Windows launch

1. Extract the complete folder from the ZIP.
2. Install Python 3.10+ and Node.js 18+ if needed.
3. Double-click `run.bat`. The launcher starts the FastAPI backend and Vite frontend, then opens the browser at `http://127.0.0.1:5173`.
4. Keep both terminal windows open while using the app.

Opening `index.html` directly cannot start the backend server; use `run.bat` for the full application. See `START_HERE.txt`.
