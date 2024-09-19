# Product Affordability Predictor

This Product Affordability Predictor is a Django web application designed to track cash flow, predict product affordability, and display predictions based on user inputs. It utilizes PostgreSQL for data storage and provides OAuth-based integration with external APIs for fetching product prices.

## Features

- Track monthly income and expenses through a cash flow interface.
- Add products to track prices and predict when you can afford them.
- Display affordability predictions based on cash flow and product prices.
- Pagination support for cash flow records, products, and predictions.
- OAuth2 integration for fetching product prices from external APIs.
- Admin interface to manage cash flow, products, and affordability predictions.

## Requirements

- Python 3.9+
- Django 3.2+
- PostgreSQL
- Docker (optional)
- Gunicorn (for production)
- OAuth credentials (for product price API integration)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/josuejero/product-affordability-predictor.git
cd product-affordability-predictor
```

### 2. Install Dependencies

You can either use a virtual environment or Docker to set up the project.

#### Virtual Environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Docker:

```bash
docker build -t django-app .
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory with the following environment variables:

```bash
SECRET_KEY=your-secret-key
DEBUG=False
DB_NAME=your-db-name
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=5432
CLIENT_ID=your-client-id
CLIENT_SECRET=your-client-secret
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 4. Database Setup

Run the following commands to set up your PostgreSQL database and create the necessary tables:

```bash
python manage.py migrate
```

If using Docker:

```bash
docker-compose up
```

### 5. Create a Superuser

You’ll need a superuser to access the Django admin interface.

```bash
python manage.py createsuperuser
```

### 6. Running the Application

#### For Development:

```bash
python manage.py runserver
```

#### For Production (using Gunicorn):

```bash
gunicorn --bind 0.0.0.0:8000 pap.wsgi:application
```

### 7. Running Tests

You can run the tests using Django's built-in test runner:

```bash
python manage.py test
```

## Project Structure

```
├── Dockerfile
├── Jenkinsfile
├── README.md
├── docker-compose.yml
├── pap/
│   ├── manage.py
│   ├── myapp/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   └── pap/
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
└── src/
    ├── data_loader.py
    ├── feature_engineering.py
    ├── main.py
    ├── model.py
    └── analysis.py
```

## Features and Usage

### 1. Cashflow Tracking

- Navigate to `/cashflow/` to add, view, or edit cash flow records.
- Cash flow records include `date`, `income`, and `expenses`.

### 2. Product Management

- Navigate to `/products/` to add, view, or edit products and their prices.
- Products include `name` and `price`, which can be fetched from external APIs using OAuth.

### 3. Affordability Predictions

- Navigate to `/predictions/` to view when specific products can be afforded based on cash flow.

### 4. Admin Panel

- You can access the Django admin panel at `/admin/` to manage records directly.

## OAuth Integration

To fetch product prices, you’ll need to set up OAuth credentials. Ensure you have the following environment variables set:

```bash
CLIENT_ID=your-client-id
CLIENT_SECRET=your-client-secret
```

## Deployment

This project can be deployed using Docker and Kubernetes. The `Dockerfile` and `deployment.yaml` files are provided for containerization and deployment to Kubernetes clusters.

### Docker Deployment:

```bash
docker build -t my-django-app .
docker run -p 8000:8000 my-django-app
```

### Kubernetes Deployment:

You can deploy the application to a Kubernetes cluster by applying the deployment and service manifests:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

## Contributing

Feel free to submit pull requests to contribute to this project. Ensure that all tests pass before submitting your PR:

```bash
python manage.py test
```

## License

This project is licensed under the MIT License.