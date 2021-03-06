import time

import redis
from flask import Flask


app = Flask(__name__)
# Create a Flask server called app.
cache = redis.Redis(host='redis', port=6379)
# Create a redis cache called cache bound to port 6379.


def get_hit_count():
    # When someone accesses the server, log a hit to the cache.
    retries = 5
    # The number of attempts the client has to reach the server.
    while True:
        # Loop until exited.
        try:
            return cache.incr('hits')
            # Return the current number of hits to the server
        except redis.exceptions.ConnectionError as exc:
            # If the client does not reach the server.
            if retries == 0:
                # If the client has tried a number of time equal to retries:
                raise exc
                # Raise the connection error exception.
            retries -= 1
            # If the client has not retried a number of times equal to retries,
            # Decrement retries and try again.
            time.sleep(0.5)
            # Wait so that server has time to catch up to client requests.


@app.route('/')
def hello():
    # Run the hello function when the server is accessed by a client.
    count = get_hit_count()
    # Find the number of times the server has been hit.
    return 'Hello World! I have been seen {} times.\n'.format(count)
    # Output a message with the number of times the server has been hit.


if __name__ == "__main__":
    # Run the server off of localhost and enable debugging.
    app.run(host="0.0.0.0", debug=True)
