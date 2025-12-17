# LinkTree – Your Personalized Link Hub

LinkTree is a customizable, user-friendly web application designed to help you organize and share all your important links on a single, sleek page. Similar to Linktree, **LinkTree** allows users to present their online presence in one convenient place, perfect for social media profiles, portfolios, and more.

This project is **Dockerized** and runs on **port 7000**.

---

## What is LinkTree?

**LinkTree** is your personalized hub for managing and sharing multiple links from one page. Whether you're a content creator, business professional, or someone with multiple online accounts, LinkTree helps you:

* Consolidate all important links into one place
* Share a single URL that points to all your profiles, blogs, and websites
* Maintain a clean, mobile-responsive landing page

Built with **Django** and **Tailwind CSS**, the application focuses on simplicity, scalability, and modern UI practices.

---

## Features

* User authentication and profile management
* Create, edit, delete, and reorder links
* Clean and modern UI using Tailwind CSS
* Class-Based Views (CBVs) for maintainable Django code
* Fully mobile-responsive design
* Docker-based setup for easy deployment
* CI/CD automation using Jenkins

---

## Technologies Used

* **Django** – Backend framework
* **Django Crispy Forms** – Improved form rendering
* **Class-Based Views (CBVs)** – Reusable and structured views
* **HTML5** – Markup
* **Tailwind CSS** – Utility-first styling
* **Docker & Docker Compose** – Containerized deployment
* **Jenkins** – CI/CD automation

---

## Prerequisites

Make sure you have the following installed:

* Docker
* Docker Compose (v2 recommended)
* Jenkins (for CI/CD pipeline)

---

## Installation & Running with Docker (Port 7000)

### 1. Clone the repository

```bash
git clone https://github.com/akshatraj26/Link-Tree-Clone.git
cd Link-Tree-Clone
```

### 2. Environment Variables

Create a `.env` file in the project root (example):

```env
DJANGO_SECRET_KEY=your-secret-key
DEBUG=0
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=linktree
DB_USER=admin
DB_PASS=Admin123
DB_HOST=db
DB_PORT=3306
```

### 3. Build and start containers

```bash
docker compose up --build
```

### 4. Database Migrations

Database migrations are **automatically handled during container startup**, so no manual migration commands are required.

### 5. Create superuser (optional)

```bash
docker compose exec app python manage.py createsuperuser
```

---

## Access the Application

Open your browser and visit:

```
http://localhost:7000/
```

---

## Jenkins CI/CD Integration

This project supports **Jenkins-based CI/CD** to automate build, test, and deployment workflows.

### Jenkins Pipeline Overview

The Jenkins pipeline typically performs the following steps:

1. Pull source code from GitHub
2. Build Docker images
3. Run containers using Docker Compose
4. Apply database migrations automatically
5. Restart services on successful build

### Sample Jenkinsfile

```groovy

pipeline {
    agent any 
    
    stages {
        stage("Pull code from git hub") {
            steps{
                git url: "https://github.com/akshatraj26/Link-Tree-Clone.git", branch: "main"
            }
        }
        stage("Build & Test your application"){
            steps{
                sh "docker build -t link-tree ."
            }
        }
        stage("Deploy you application on jenkins"){
            steps{
                sh "docker compose up -d"
            }
        }
    }
}

```

### Jenkins Requirements

* Jenkins installed on the host machine
* Docker and Docker Compose installed on the Jenkins server
* Jenkins user added to the Docker group

```bash
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
```

---

## Usage

* **Home Page** – Displays your public link page
* **Dashboard** – Manage and organize links after login
* **Profile Management** – Update user details
* **Responsive Design** – Optimized for desktop and mobile

---

## Tailwind CSS

Tailwind CSS is used for styling. You can customize the UI by editing:

* `tailwind.config.js`
* Static Tailwind files inside the `static/` directory

---

## Docker Notes

* The Django app is exposed on **port 7000**
* MySQL runs inside a separate container
* Static files are managed via Docker volumes

---

## Contributing

Contributions are welcome:

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-branch
```

3. Commit changes

```bash
git commit -m "Add new feature"
```

4. Push and open a Pull Request

---

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## Contact

For any queries or collaboration:

📧 **[akshatraj2607@gmail.com](mailto:akshatraj2607@gmail.com)**
