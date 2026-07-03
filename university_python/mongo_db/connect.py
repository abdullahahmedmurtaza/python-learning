from pymongo import MongoClient
# connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
# create database
db = client["college_db"]
# create collection
collection = db["courses"]
print("Connected to MongoDB successfully")

#Create Courses
course1 = {
"course_id": 101,
"course_name": "Digital Logic Design",
"available_seats": 4,
"credits" : 2,
"instructor": "Shehzad Shaikh"
}
collection.insert_one(course1)
course2 = {
"course_id": 102,
"course_name": "Communication Skills",
"available_seats": 3,
"credits" : 3,
"instructor": "Ali Khan"
}
collection.insert_one(course2)
course3 = {
"course_id": 103,
"course_name": "Pakistan Studies",
"available_seats": 2,
"credits" : 2,
"instructor": "Muhammad Rafique"
}
collection.insert_one(course3)
course4 = {
"course_id": 104,
"course_name": "Economics I",
"available_seats": 4,
"credits" : 3,
"instructor": "Raza Ali"
}
collection.insert_one(course4)
course5 = {
"course_id": 105,
"course_name": "Data Structures",
"available_seats": 1,
"credits" : 3,
"instructor": "Ahmed Ali"
}
collection.insert_one(course5)
print("Courses inserted successfully")


#Read
courses = collection.find()
for c in courses:
	print(c)
	

#Update
collection.update_one(
{"course_id":103},
{"$set":{"credits":3}}
)

#Delete
collection.delete_one({"course_id":104})
print("Document deleted successfully")