Viktoriia Varodi 100429843
Natalia Carrasco 100429915


Additional functionalities:

manager.py: @manager_only. To avoid normal customer unauthorized access to paths as /edit /add

manager.py: process_ajax(): Create a json for ajax call with data for each projection and its available seats. 

static/js/main.js: 
    interactiveForm: ajax call and used when onclick BuyTicket to show the corresponding available seats as a filter per projection
    Price: onclick when user chooses the number of seats to show total price
    when document.ready(): it updates the information for available seats using the json in the projection/reservation tables



Scripts provided:
virtual.sh: Create the virtual environment
run.sh: Run on development mode our application
insert.sql: The insertions we have introduced  