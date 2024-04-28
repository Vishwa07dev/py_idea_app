from flask import Flask


app = Flask(__name__)

#Create the idea repository. This where ideas will be stored
ideas  = {
    1 : {
        "id" : 1,
        "idea_name" : "ONDC",
        "idea_description" : "Details about ONDC",
        "idea_author" : "Adeeb"
    },
    2 : {
        "id" : 2,
        "idea_name" : "Save Soil",
        "idea_description" : "Details about Saving Soil",
        "idea_author" : "Ankit Sharma"
    }

}

'''
Creat an RESTful endpoint for fetching all the ideas
'''
@app.get("/ideaapp/api/v1/ideas")
def get_all_ideas():
    #Logic to fetch all the ideas
    return ideas




if __name__ == '__main__':
    app.run(port=8080)