PROJECT TITLE:
   NETWORK BASED PATTERN SEARCHING.

To run the project follow the below steps:-
   1 => in search.py run it
   2 => in server run the the server
   3 => After the starting of server open external terminal for running the client.py
        and run it.
        it will ask for the file name:-
        Give "data.txt" as file name(as data.txt is in the same directory )
        ==> if you enter the worng file name as it is not in the directory then it will print "File not Found"
        then it it will ask for word to search:-
        Give word to search in the given line

        Then it will display all the lines which consists of given word




=====Client=====

Connects to the server and sends a JSON request containing:

Filename

Word to search


Parses the server response and displays:

Matching lines with their line numbers

Error messages if any



=====Server=====

Listens for client connections on a specified port.

Processes incoming requests using the Search class.

Sends the search result back in JSON format.


=====Search Class=====

Reads file content and stores it in a list.

Cleans lines by removing special characters.

Searches for the given word in each line and returns matching lines with their line numbers.
