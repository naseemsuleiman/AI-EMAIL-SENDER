# AI Email Sender

AI Email Sender is a full-stack application that generates professional emails using AI and sends them to specified recipients. The project consists of a React frontend and a Python backend.

## ✨ Features

- Generate email content using AI based on user prompts
- Send emails to multiple recipients
- Modern React frontend (Vite, React 19)
- Python backend with email sending and AI integration
- Environment variable support via .env files

## 📁 Project Structure

```
├── backend/
│   ├── .env
│   ├── ai_generator.py
│   ├── email_sender.py
│   ├── main.py
│   └── ...
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### 🔧 Backend

1. **Install dependencies**

Navigate to the backend directory and set up a virtual environment:

```bash
cd backend
python -m venv env
env\Scripts\activate  # On Windows
# or
source env/bin/activate  # On macOS/Linux
pip install -r requirements.txt
```

2. **Configure environment variables**

Create a `.env` file in the `backend` directory with your email credentials and any required API keys.

3. **Run the backend server**

```bash
python main.py
```

### 💻 Frontend

1. **Install dependencies**

Navigate to the frontend directory:

```bash
cd frontend
npm install
```

2. **Start the development server**

```bash
npm run dev
```

3. **Open the app**

Visit [http://localhost:5173](http://localhost:5173) in your browser.

## 📌 Usage

- Enter recipient email addresses (comma-separated)
- Enter a prompt describing the email you want to generate
- Click **"Generate Email"** to let the AI create the email content
- Review and edit the subject/content if needed
- Click **"Send Email"** to send it to the recipients

## 🔐 Environment Variables

The backend uses a `.env` file for sensitive configuration (not tracked in version control).

Example `.env`:

```
EMAIL_ADDRESS=your-email@example.com
EMAIL_PASSWORD=your-password
GROQ_API_KEY=your-groq-api-key
```

---

© 2025 AI Email Sender Project
