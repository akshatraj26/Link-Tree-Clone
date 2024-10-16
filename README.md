# LinkTree - Your Personalized Link Hub

LinkTree is a customizable, user-friendly web application designed to help you organize and share all your important links on a single, sleek page. Similar to Linktree, LinkNest allows users to present their online presence in one convenient place, perfect for social media profiles, portfolios, and more.

## What is LinkTree?

**LinkTree** is your personalized hub for managing and sharing multiple links from one page. Whether you're a content creator, business professional, or just someone with a lot of online accounts, LinkNest provides an easy way to:

- Consolidate all your important links into one place.
- Share a single URL with your audience, which leads them to all your relevant profiles, blogs, videos, websites, and more.
- Make it easier for people to find and connect with you online.

With **LinkTree**, you can create a clean, mobile-responsive landing page where you control the layout and appearance of your links. Built with modern technologies like Django and Tailwind CSS, LinkNest ensures both ease of use and flexibility.

---

## Features

- User-friendly interface for adding and organizing links.
- Clean, modern design using Tailwind CSS.
- Built with Django and Class-Based Views (CBVs) for structured, reusable components.
- Secure user authentication and profile management.
- Mobile-responsive design.

## Technologies Used

- **Django**: A high-level Python web framework that enables rapid development of secure and maintainable websites.
- **Django Crispy forms**:  Used to add styling and human touch to django forms
- **Class-Based Views (CBVs)**: Django views organized into classes to provide reusable, modular code.
- **HTML5**: For structuring content on the web.
- **Tailwind CSS**: A utility-first CSS framework for designing responsive layouts.

  
## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv env
    source env/bin/activate  # For Windows: env\Scripts\activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the Django project:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser for accessing the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Open the application in your browser:

    ```
    http://127.0.0.1:8000/
    ```

## Usage

1. **Home Page**: Add and manage your links.
2. **User Profile**: Users can register, log in, and update their profiles.
3. **Link Management**: After logging in, users can create, edit, and delete links.
4. **Mobile-Responsive Design**: The app looks great on all devices.


## Tailwind CSS

This project uses **Tailwind CSS** for styling. If you want to make custom changes to the design, you can modify the `tailwind.config.js` or add custom CSS classes in `static/tailwind.css`.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

### Contact

For any inquiries, reach out via [akshatraj2607@gmail.com](mailto:akshatraj2607@gmail.com).


