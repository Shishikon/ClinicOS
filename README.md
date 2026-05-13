# 🏥 ClinicOS

> A clean and modern clinic management platform — patients book appointments with doctors and walk away with a QR code as their confirmation ticket.

![ClinicOS](https://github.com/user-attachments/assets/ef6fc42d-adc6-4939-9746-bdd44114f908)

🌐 **Live Demo:** [clinicosapp.up.railway.app](https://clinicosapp.up.railway.app)

---

## ✨ Features

- 👨‍⚕️ **Doctor Listings** — Browse available doctors and their specialties
- 📅 **Appointment Booking** — Patients fill out a form to book an appointment with their chosen doctor
- 🔑 **QR Code Generation** — Every confirmed appointment generates a unique QR code instantly
- 📲 **Scan or Download** — Patients can scan or download their QR code as proof of appointment
- 🗄️ **Database Storage** — All appointments are stored and fully manageable via the admin panel
- 🔐 **Admin Panel** — Full control over doctors, appointments, and clinic settings

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Frontend | Bootstrap, HTML, CSS |
| Database | SQLite |
| QR Codes | qrcode (Python library) |
| Web Scraping | BeautifulSoup4 |
| Static Files | WhiteNoise |
| Hosting | Railway |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/Shishikon/ClinicOS.git
cd ClinicOS

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

Then open [http://localhost:8000](http://localhost:8000) in your browser.

---

## ⚙️ Environment Variables

Set these in your hosting dashboard or a `.env` file:

```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=yourpassword
DJANGO_SUPERUSER_EMAIL=admin@example.com
```

---

## 📁 Project Structure

```
ClinicOS/
├── project/          # Django project settings
├── clinicos/         # Main app (models, views, templates)
│   ├── static/       # CSS, JS, images
│   └── templates/    # HTML templates
├── requirements.txt
├── build.sh          # Railway build script
├── Procfile
└── manage.py
```

---

## 🖼️ How Appointments Work

1. Patient browses available doctors
2. Patient fills out the appointment booking form
3. System saves the appointment to the database
4. A unique QR code is generated for that appointment
5. Patient can **scan** or **download** the QR code as confirmation
6. Staff verifies the appointment by scanning the QR code on arrival

---

## 👨‍💻 Author

**Shishikon** — Trilingual Python Developer
- GitHub: [@Shishikon](https://github.com/Shishikon)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
