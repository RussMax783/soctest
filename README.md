Please do not spend more than 3 hours on this.
# SOC Test
## Instructions
1. Fork this repo
2. Write a small app that accepts a csv file as an upload. The csv file is a contact list. The contents of the list need to be inserted into a database. There needs to be a way to view and delete after the upload.
4. Either demonstrate in code or provide an explanation in this README on how you would handle very large files.
5. Either demonstrate in code or provide an explanation in this README on how you would handle different encodings.
6. Submit this as a pull request.


## Explination

I chose to just implement as a REST API. I didn't create templates or anything because the most likely case is your going to interact with the server through Angular or React. So I just used the Django Rest Framework templates and serializers to make it very easy to upload contacts, view, and destroy. If we wanted to list all of them at the same time and paginate them DRF makes that very easy.


If the file was very large, we could stream the file. Or we could even put restrictions on file size. but beacuase we wouldn't want to store the actual file, streaming it through would probably be the best option.


If my understanding is correct, the python csv module handles different types of encodings so we would really need to worry about that. If the file is encoded in a way that csv couldn't read the file, then we proably wouldn't want to read that file in the first place and have the user change it.
