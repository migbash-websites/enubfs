# ENU - Napier Fintech Society

Our website: www.napierfintech.com (depreciated) | https://enubfs.herokuapp.com/ (placeholder)

This repository currently contains:

- Society website

Currently on our website you will find:

- Our social media links,
- How to join our society,
- Our E-mail subscription - so you would not miss a thing! :)

We are aiming to expand our society to the fullest and get as many people as we can into our society.

Keep visiting our website, as we will be including more features in the upcoming future that will make it the go-to place for Fintech & Blockchain Upcoming Events / Discussions & Special Offers in Scotland!

This website is being hosted through ~~PythonAnywhere.com~~ | Heroku.com

## Attention!

This society has migrated & re-branded, please find us __[here](https://github.com/migbash/enuets)__ - or -  __https://enuets.com__.

---

This website has been built using:

- Flask_Mail
- Flask_PyMongo
- Flask

Website dependencies can be found with further instructions in the *__requirements.txt__* file.

This website was built for society purposes. Its aim is to inform the public & members of the societies existence & promote itself.

We do not collect emails for spam purposes, its only use is to inform the members of upcoming events & interesting nearby events.

---

## Website Deployment [Heroku]

First of all you need a Heroku account to do this, if you do not yet have an account, create one.

1. Download the Heroku CLI for your respective OS [here](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

2. Run ```heroku login``` in you command line & follow the steps to login to your heroku account.

3. Now we need gunicorn , a WSGI server: ```pip install gunicorn``` or ```pipenv install gunicorn```

4. Add a ```Procfile``` (no extension) file to this repository folder (or any other folder ready for deployment). Addthe following to the file ```web: gunicorn app:app```, where ```:app``` is the name of your main flask app file. Use mine for reference.

5. Now, make sure that the website dependencies are all up to date and located within your requirements.txt file. You can do so by running the command - ```pip freeze > requirements.txt```. Again, mine is already included.

6. Finally, run the command ```heroku create <your-project-name>```
7. Now, once that's done, run the command ```heroku open``` this should open your heroku live website.

8. If you are not seeing your website: then you must push your code to the heroku platform first - ```git add .``` - ```git commit -m "message"``` - ```git push heroku master```

Fantastic! Whoo-hoo! You are now live on Heroku!
