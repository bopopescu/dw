import mysql.connector

db = mysql.connector.connect(
        host="localhost",
        user="suyash",
        passwd="suyash@123",
        database="dw_test"
        )

cursor = db.cursor()

api_key = "USxqIbXJDOdaYZLpMgR94cw4Z"
api_secret = "geXskTyq5qqx9CnnuFpFko62HAHW9Cqm38k4W6mSAlVR8h3IyS"
access_token = "2915086652-77XHTRHThgRPfKaQENZ8oAxZmv1vpatfx5FFyG3"
access_token_secret = "sKJkzaHYT6F2OdKTJwGQkG29xrd7Kd8RT4Bta61vqDGEl"


import pdb
