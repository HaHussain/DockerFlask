import time

from flask import Flask


app = Flask(__name__)
# Create a Flask server called app.


def get_hit_count():
    # The number of attempts the client has to reach the server.
    NonVolatileHits = open("./Persistancy/HitRecord.txt", "r+")
    # Open the file where the hit record will be updated.
    hits = NonVolatileHits.read()
    # Read the current number of hits saved by the server.
    hits += 1
    # Increment the number of hits by 1.
    time.sleep(0.5)
    # Wait so that server has time to catch up to client requests.
    return hits
    # Return the current number of hits to the server


@app.route('/')
def hello():
    # Run the hello function when the server is accessed by a client.
    count = get_hit_count()
    # Find the number of times the server has been hit.
    return 'Hello World! I have been seen {} times.\n'.format(count)
    # Output a message with the number of times the server has been hit.
    NonVolatileHits.write(count)
    # Write the new number of hits to the file.
    NonVolatileHits.close()
    # Close the file and save its new value.


if __name__ == "__main__":
    NonVolatileHits = open("./Persistancy/HitRecord.txt", "r+")
    # Open file within directory where the hits would be stored with readwrite
    if NonVolatileHits.read() == '':
        # Check if the file has any data in it.
        FileHitCounter = 0
        # If not initialise the hit count as 0.
    else:
        FileHitCounter = NonVolatileHits.read()
        # Otherwise initialise it with whatever the value is in the .txt file.
    NonVolatileHits.close()
    # Close and save changes to the file.
    app.run(host="0.0.0.0", debug=True)
    # Run the server off of localhost and enable debugging.
