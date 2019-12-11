# Paint_ball_API

A Paintball game is a competitive team shooting sport in which players eliminate 
opponents from play by hitting them with spherical dye-filled gelatin capsules 
("paintballs") that break upon impact.
Select your team and choose your gun to get it started!

## Used tecnologies:

* Python 3.7
* Django (https://www.djangoproject.com/download/)
* DjangoRestFramework (https://www.django-rest-framework.org/)

## How to run the project

1. Create a virtual environment to run and install the projects dependencies(https://virtualenv.pypa.io/en/latest/installation/)
2. Activate the virtual envioriment
3. Clone de project into the destined folder 
> git clone https://github.com/ElcyJ/Paint_ball_API.git
4. Inside the projects root folder "paint_ball" install the dependencies using:
> pip install -r requirements.txt
5. to run te project at http://localhost:8000 use:
> python manage.py runserver
6. Now the project is runing and you can make requests to it.
7. On the browser if you access http://localhost:8000 you will have access to a API interface provided by the DRF.

## How to consume this API

### Enpoints:

* **Players** - http://localhost:8000/players/
> * Register players with a team and a gun.
> * You cannot change it later, just your localization.
* **Maps** - http://localhost:8000/maps/
> * Visualize available maps.
> * Only a admin can create a map.
* **Guns** - http://localhost:8000/guns/
> * Visualize available guns.
> * Only a admin can create a gun.
* **Teams** - http://localhost:8000/teams/
> Visualize available teams or create yours.
* **Shots** - http://localhost:8000/shots/
> * Select a direction and give a shot to hit someone from another team.
> * If you hit a player, this will be removed from the game .
