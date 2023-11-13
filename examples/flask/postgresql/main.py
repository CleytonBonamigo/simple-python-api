from flask import Flask, request, jsonify, abort
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Configure the database connection
conn = psycopg2.connect(
    dbname="mydatabase",
    user="yourusername",
    password="yourpassword",
    host="localhost"
)