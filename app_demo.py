from  flask import  Flask, jsonify, request

#step 1: Create the Flask app instance
app = Flask(__name__)

#step 2: Dummy data for photographers  (simulating database)
photographers  =  [
     {"id": "p1", "name": "Amit Lensman", "skills": ["Wedding", "Portrait"]},
     {"id": "p2", "name": "Sana Clickz",  "skills": ["Fashion", "Event"]}
]

# step 3: Dummy availability data maped by photographer ID
availability_data = {
    "p1": ["2025-06-20", "2025-06-23"],
    "p2": ["2025-06-19", "2025-06-22"]
}
# -------------------------
# Route 1: GET /photographers
# Returns  list of all photographers
@app.route('/photographers', methods=['GET'])
def  get_photographers():
    return jsonify(photographers)

# step 4: start the Flask server
if __name__ == '__main__':
    app.run(debug=True)


    # --------------------
    # Route 2: GET /availability/<photographer_id>
    # Returns  available dates  for the given photographer
    @app.route('/availability/<photographer_id>',methods=['GET'])
    def check_availability(photographer_id):
        return jsonify({
            "photographer_id": photographer_id,
            "availability_dates": availability_data.get(photographer_id,[])
        })

        #------------------
        # Route 3: POST /book
        # Accept a booking request and returns confirmation
        @app.route('/book',methods=['POST'])
        def book_photographer():
            booking = request.get_json()
            print("Received booking request:",booking)
            return jsonify({
                "message": "Booking confirmed!",
                "booking_details": booking
            }),201

            # Step4: Start the Flask server
            if __name_ =='_main_':
               app.run(debug=True)