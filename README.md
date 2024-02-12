# IntegrateImagekit

## Overview

This project demonstrates how to upload files to ImageKit server and save the URLs in Django models.

## Prerequisites

- Python (>=3.6)
- Django (>=3.0)
- ImageKit SDK

Before getting started, you need to have ImageKit credentials ready:

1. **ImageKit Account**: Sign up for an [ImageKit](https://imagekit.io/) account if you haven't already.
2. **ImageKit API Credentials**: Obtain your ImageKit API credentials (public key, private key, and URL endpoint).

## Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/parthdadhaniya/EmailReader.git
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Django and Celery Settings**:You need to configure your ImageKit credentials in the Django settings file (settings.py). Add the following lines and replace the placeholders with your actual ImageKit credentials:

   ```bash
   IMAGEKIT = {
    'PUBLIC_KEY': 'your_public_key',
    'PRIVATE_KEY': 'your_private_key',
    'URL_ENDPOINT': 'https://your-endpoint-url.com',
    }
   ```

4. **Make Migrations**:

   ```bash
   python manage.py makemigrations
   ```

5. **Apply Migrate**:

   ```bash
   python manage.py migrate
   ```

6. **Start Django Development Server**:
   ```bash
   python manage.py runserver
   ```

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Credits

- [Django](https://www.djangoproject.com/)

## Authors

- [Parth Dadhaniya](https://github.com/parthdadhaniya)

## Contact

For any inquiries or feedback, feel free to contact [parthdadhaniya079@gmail.com](mailto:parthdadhaniya079@gmail.com).
