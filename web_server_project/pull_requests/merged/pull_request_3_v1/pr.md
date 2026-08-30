Issue Summary: 
Support for parsing query parameters in the URL path has been added to the server.

Approach: 
The approach involves modifying the server to extract query parameters from the URL path and store them in a dictionary, which is then passed to the handler. The modification includes parsing the query string and splitting it into key-value pairs. The resulting dictionary is then used to store the query parameters. This change enables the server to handle query parameters in the URL path and pass them to the handler for further processing. The updated diff file is attached for review.