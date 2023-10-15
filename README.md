# HOW TO EXECUTE

- First, install the docker in your device.
- Now, let's go to the party:
	- run `sudo docker build -t <project-name> .`
		- This will create an image docker of your project with the name you choose.
	- run `sudo docker run -p 5000:5000 <project-name>`
		- This will run the created image with the API.
		- If you prefer, put the *-d* flag before *-p* for run the API in the background
