import time
import logging

from flask import Flask

# logging.basicConfig(filename='./Persistancy/Debug.log', level=logging.DEBUG)

app = Flask(__name__)
# Create a Flask server called app.
# logging.debug("Flask Server created")


def get_hit_count():
    # logging.debug("Hitcount function entered")
    # The number of attempts the client has to reach the server.
    NonVolatileHits = open("./Persistancy/HitRecord.txt", "r+")
    logging.info("Opened .txt file")
    # Open the file where the hit record will be updated.
    hits = int(NonVolatileHits.read())
    # logging.debug("Read .txt file")
    # Read the current number of hits saved by the server.
    hits += 1
    # logging.debug("Incremented hit value")
    # Increment the number of hits by 1.
    NonVolatileHits = open("./Persistancy/HitRecord.txt", "r+")
    # Open the file again to reset marker to overwrite previous data
    NonVolatileHits.write(str(hits))
    logging.info("Write the new number of Hits to text file")
    # Write the new number of hits to the file.
    NonVolatileHits.close()
    logging.info("Saving text file")
    # Close the file and save its new value.
    time.sleep(0.5)
    logging.info("Waiting 0.5 ms")
    # Wait so that server has time to catch up to client requests.
    return hits
    logging.info("Exiting hit count function")
    # Return the current number of hits to the server


@app.route('/')
def hello():
    logging.info("Server has been hit")
    # Run the hello function when the server is accessed by a client.
    count = get_hit_count()
    # logging.debug("Hit count function called")
    # Find the number of times the server has been hit.
    return 'Hello World! I have been seen {} times.\n'.format(count)
    logging.info("Outputting text to server")
    # Output a message with the number of times the server has been hit.


if __name__ == "__main__":
    NonVolatileHits = open("./Persistancy/HitRecord.txt", "r+")
    # Open file within directory where the hits would be stored with readwrite
    if NonVolatileHits.read() == '':
        # Check if the file has any data in it.
        FileHitCounter = 0
        # If not initialised the hit count as 0.
    else:
        FileHitCounter = NonVolatileHits.read()
        # Otherwise initialise it with whatever the value is in the .txt file.
    NonVolatileHits.close()
    # logging.debug("HitRecord file read")
    # Close and save changes to the file.
    app.run(host="0.0.0.0", debug=True)
    # logging.debug("Server initialised")
    # Run the server off of localhost and enable debugging.
