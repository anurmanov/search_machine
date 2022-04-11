SEARCH MACHINE

Solution according to Technical task.pdf


-----DESCRIPTION-----

Hi there.

Let me introduce my version of the search machine.
It is consist of 2 parts: client and server.

We've got a rather thin client app. Client part is just a client.py script which depends on requests library (pip install requests)

The server part is much more complicated.
It is packed into docker-compose infrastructure and consists of worker and nginx intended for load balancing.

The worker contains all business logic of the search machine. It is based on fastapi app and can be scaled up through docker's flag --scale worker=n (you will see it inside a run script)

-----HOW TO RUN-----

You need Docker to run the app.
To run server just run script run_server.sh or run_server_with_5_workers.sh, but please DO NOT FORGET to give +x access rights for all shell scripts in working dir.
The script run_server_with_5_workers.sh lets us to run 5 workers, but it was done just for showing ability of app.

To stop server run script stop_server.sh

P.S. Despite of fact that the technical task looks like description of a simple console app. 
I tried to perform it in a production-ready style, e.g. switching from JSON storage to Postgres will take minimal expenses. Performance issues are not forgotten as well, I meant workload balancing through running several workers and balancing them via nginx.

    
