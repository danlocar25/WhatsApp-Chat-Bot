# run.py - Refactored for Netlify functions

from app import create_app

# Create the Flask app
app = create_app()

# The app.run() is not needed for Netlify functions, so it's commented out
# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=5000)
