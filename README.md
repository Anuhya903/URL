# 🔗 URL Shortener

A modern, responsive URL shortener web application built with Flask that allows you to create shortened links and track their performance.

## 🌐 Live Demo

**Live Application:** [https://url-shortener-x6lz.onrender.com](https://url-shortener-x6lz.onrender.com)

## ✨ Features

- **URL Shortening**: Convert long URLs into short, shareable links
- **Click Analytics**: Track how many times each shortened link has been clicked
- **Social Sharing**: One-click sharing to Twitter, Facebook, LinkedIn, WhatsApp, and Instagram
- **Copy to Clipboard**: Easy copying of shortened URLs
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **Modern UI**: Beautiful glassmorphism design with animated background
- **Recent URLs**: Local storage of your recently created short URLs
- **URL Validation**: Automatic validation of URL format

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Database**: SQLite
- **Deployment**: Render
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Poppins, Inter)

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/Aunhya893/URL.git
   cd URL
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Open your browser and go to `http://localhost:5000`

## 🚀 Usage

1. **Shorten a URL**:
   - Enter your long URL in the input field (must include http:// or https://)
   - Click "Shorten URL"
   - Copy your new shortened link

2. **Share Your Link**:
   - Use the social media buttons to share directly
   - Or copy the link and share manually

3. **View Statistics**:
   - See all shortened URLs in the statistics table
   - Track click counts and creation dates

## 🗂️ Project Structure

```
URL/
├── static/
│   └── style.css          # Custom CSS styles
├── templates/
│   └── index.html         # Main HTML template
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
└── .gitignore            # Git ignore rules
```

## 🔧 Configuration

The application uses SQLite database which is automatically created on first run. No additional configuration is required for basic usage.

## 🌟 Features in Detail

### URL Management
- Generates unique 6-character codes for each URL
- Validates URL format before shortening
- Stores original URL, short code, creation date, and click count

### User Interface
- Modern glassmorphism design
- Animated gradient background
- Responsive layout for all screen sizes
- Real-time URL validation with visual feedback

### Social Integration
- Direct sharing to multiple platforms
- Custom share messages
- Clipboard integration for easy copying

## 📊 API Endpoints

- `POST /shorten` - Create a new shortened URL
- `GET /<short_code>` - Redirect to original URL
- `GET /` - Main application interface

## 🚀 Deployment

This application is deployed on **Render** using:
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python app.py`

## 🔒 Privacy & Security

- No user data collection
- URLs are stored in a local SQLite database
- No tracking beyond basic click counts

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Developer

**Anuhya903**  
- GitHub: [@Anuhya903](https://github.com/Anuhya903)

## 🐛 Bug Reports

If you encounter any issues, please [open an issue](https://github.com/Aunhya893/URL/issues) on GitHub.

---

**⭐ Star this repository if you find it helpful!**
