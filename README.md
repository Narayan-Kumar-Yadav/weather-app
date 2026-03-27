<div align="center">

# 🌤️ WeatherNow

### Real-Time Weather Dashboard for 200,000+ Cities Worldwide

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![OpenWeatherMap](https://img.shields.io/badge/OpenWeatherMap-API-orange?style=flat&logo=openweathermap&logoColor=white)](https://openweathermap.org/api)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)](https://www.w3.org/Style/CSS/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)
[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=flat&logo=vercel)](https://your-demo-link.vercel.app)

<br/>

> **Live weather data. Clean UI. Zero friction.**  
> A production-ready weather dashboard built with Python Flask — delivering accurate, real-time weather for any city on Earth.

<br/>

![WeatherNow Screenshot](./assets/screenshot.png)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [API Reference](#api-reference)
- [Screenshots](#screenshots)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Author](#author)

---

## 🌍 Overview

**WeatherNow** is a full-stack weather application that integrates the **OpenWeatherMap API** with a **Python Flask** backend to deliver real-time weather data in a clean, responsive UI.

Built to demonstrate real-world API integration, backend development with Flask, and production-ready frontend design — this is not a tutorial clone, it's a fully functional weather platform.

```
User → Search City → Flask Backend → OpenWeatherMap API → Real-Time Data → Clean UI
```

---

## ✨ Features

### 🌡️ Weather Data
- 🌍 Real-time weather for **200,000+ cities** worldwide
- 🌡️ Temperature (Celsius / Fahrenheit toggle)
- 💧 Humidity, wind speed, pressure & visibility
- ☁️ Weather condition with dynamic icons
- 🌅 Sunrise & sunset times

### 🎨 UI/UX
- 📱 Fully **responsive design** — works on all screen sizes
- 🌙 **Dark mode** support
- ⚡ Fast load times with minimal dependencies
- 🎯 Clean Google-inspired search interface
- 🖼️ Dynamic weather condition backgrounds

### 🔧 Technical
- 🐍 **Python Flask** RESTful backend
- 🔑 Secure API key management via environment variables
- ⚠️ Comprehensive error handling (invalid city, API errors, network issues)
- 🔄 Loading states for better UX
- 🌐 CORS-enabled API endpoints

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Backend | Python 3.x | Core language |
| Framework | Flask | Web server & routing |
| HTTP Client | Requests | API calls to OpenWeatherMap |
| API | OpenWeatherMap | Weather data source |
| Frontend | HTML5, CSS3 | UI structure & styling |
| JavaScript | Vanilla JS | Dynamic interactions |
| Deployment | Vercel / Render | Hosting |

---

## 📁 Project Structure

```
weather-app/
├── app.py                  # Flask application entry point
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not committed)
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore rules
├── static/
│   ├── css/
│   │   └── style.css       # Main stylesheet
│   ├── js/
│   │   └── main.js         # Frontend JavaScript
│   └── assets/
│       └── icons/          # Weather condition icons
├── templates/
│   └── index.html          # Main HTML template
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have these installed:
- Python 3.8+
- pip
- A free [OpenWeatherMap API key](https://openweathermap.org/api)

### 1. Clone the Repository

```bash
git clone https://github.com/Narayan-Kumar-Yadav/weather-app
cd weather-app
```

### 2. Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

```bash
# Copy the example env file
cp .env.example .env

# Open .env and add your API key
OPENWEATHER_API_KEY=your_api_key_here
```

### 5. Run the App

```bash
python app.py
```

Open your browser and visit: **`http://localhost:5000`** 🎉

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
OPENWEATHER_API_KEY=your_openweathermap_api_key
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your_secret_key_here
```

> **Get your free API key** at [openweathermap.org/api](https://openweathermap.org/api) — free tier supports 1,000 calls/day.

---

## 🔌 API Reference

### Get Weather by City

```
GET /api/weather?city={city_name}
```

**Example:**
```bash
curl http://localhost:5000/api/weather?city=London
```

**Response:**
```json
{
  "city": "London",
  "country": "GB",
  "temperature": 18.5,
  "feels_like": 17.2,
  "humidity": 72,
  "wind_speed": 5.1,
  "description": "Partly cloudy",
  "icon": "02d",
  "sunrise": "06:12",
  "sunset": "20:34"
}
```

---

## 📸 Screenshots

| Home Page | Search Results | Dark Mode |
|-----------|---------------|-----------|
| ![Home](./assets/home.png) | ![Results](./assets/results.png) | ![Dark](./assets/dark.png) |

> **Note:** Add your actual screenshots to the `assets/` folder and update the paths above.

---

## 🔮 Roadmap

- [x] Real-time weather by city name
- [x] Temperature unit toggle (°C / °F)
- [x] Responsive mobile design
- [x] Error handling for invalid cities
- [ ] 7-day weather forecast view
- [ ] Auto-detect location (Geolocation API)
- [ ] Weather alerts & severe condition warnings
- [ ] Data visualization charts (Chart.js)
- [ ] PWA support for offline use
- [ ] Multiple city comparison
- [ ] Weather history graphs

---

## 🤝 Contributing

Contributions are welcome! Here's how:

```bash
# 1. Fork the repo
# 2. Create your feature branch
git checkout -b feature/amazing-feature

# 3. Commit your changes
git commit -m "Add amazing feature"

# 4. Push to the branch
git push origin feature/amazing-feature

# 5. Open a Pull Request
```

Please make sure to:
- Follow existing code style
- Add comments for complex logic
- Update README if needed
- Test your changes before submitting

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Narayan Kumar Yadav**

[![GitHub](https://img.shields.io/badge/GitHub-Narayan--Kumar--Yadav-181717?style=flat&logo=github)](https://github.com/Narayan-Kumar-Yadav)
[![Portfolio](https://img.shields.io/badge/Portfolio-narayankumaryadav.link-000000?style=flat&logo=vercel)](https://narayankumaryadav.link)
[![Email](https://img.shields.io/badge/Email-narayankumaryadav2007%40gmail.com-EA4335?style=flat&logo=gmail)](mailto:narayankumaryadav2007@gmail.com)

---

<div align="center">

⭐ **Star this repo if it helped you — it helps others discover it!** ⭐

*Built with ❤️ and ☕ by Narayan Kumar Yadav*

</div>
