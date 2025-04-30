from app import create_app, db
from flask_migrate import Migrate

app = create_app()

# Initialize Migrate
migrate = Migrate(app, db)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
