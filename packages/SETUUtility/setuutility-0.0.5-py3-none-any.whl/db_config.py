from firebase_admin import firestore, initialize_app

# Initialize the Firebase app with the credentials
initialize_app()

# Create a Firestore client
db_client = firestore.client()
