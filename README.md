# School Schedule API - Pure.app assignment

## Setup

This Django application provides an API for managing school schedules. It uses **DRF** for the API and **PostgreSQL** as the DB. The project is containerized using **Docker** and **Docker Compose** for easy setup and deployment.

### Setup Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/enjoycod1ng/school_schedule.git
   cd school_schedule
   ```

2. Build and start the containers:
   ```bash
   docker-compose up --build
   ```

3. Run database migrations:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. Start the Django development server:
   ```bash
   docker-compose exec web python manage.py runserver 0.0.0.0:8000
   ```

5. Access the API at: `http://localhost:8000/schedule/`

### API Endpoints

- `GET /schedule/` - Returns all schedules.
- `GET /schedule/?for_today=true&class_name=<class_name>` - Returns the schedule for today for a specific class.

## Improvements (If I Had More Time)

- **Database Optimization**: 
   
- **Query Optimization**:

- **Caching**:
   - I would implement **Redis caching** to store frequently accessed schedule data.

- **Scaling and Load Balancing**:
   - For handling high traffic (5000+ RPS), I would implement **horizontal scaling** by using multiple Django instances behind a **load balancer**.

- **Test Automation**
