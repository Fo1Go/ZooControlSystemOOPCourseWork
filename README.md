Course project at BSUIR(OOP)<br />
Subject of project: Zoo Control System<br />
<a href="#endpoints">Endpoints</a><br />
<a href="#Project tech-stack">Tech stack</a><br />
<a href="#How to set up project">How to set up<br />

## Endpoints
<p>
all endpoint starts with api/v1/<br />
animals/<br />
GET/POST animals/list <br />
GET/DELETE/PATCH animals/animal_id <br />
</p>

## Project tech-stack
<p>
python:3.11.7<br />
PostgreSQL 16.1<br />

docker for containers<br />
</p>

## How to set up project
<p>
1) Install docker<br />
2) git clone https://github.com/Fo1Go/ZooControlSystemOOPCourseWork.git [directory]<br />
3) docker-compose up -d<br />
4) go to 127.0.0.1:5252 for api view, 127.0.0.1:80 for pgadmin<br />
WARNING: Project does not consist database data, so you have to create superuser through docker CLI<br />
</p>
