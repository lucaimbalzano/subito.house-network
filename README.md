# subito.house-network <img src="https://user-images.githubusercontent.com/45575898/184987964-64477382-1df1-4512-9b77-9d6ec0eef470.jpg" width="60" height="60" />

webscraper-engine module for real-estate on subito.it

clone repository and move in:
```
$ git clone https://github.com/lucaimbalzano/subito.house-network.git
$ cd subito.house-network
```

create virtual environment

```
$ python3 -m venv env

windows:
$ .\env\Scripts\activate 
linux:
$source .\env\bin\activate

```
or 
```
(if you haven't pipenv)
$ pipenv --python 3.10 install --dev
then:
$ pipenv shell
```


install all dependencies:
```
$ pip install -r requirements.txt

Linux add this dep called 'tkinter' to use Mouseinfo:
sudo apt-get install python3-tk python3-dev
```

Docker
```
docker build -t subito_docker .
docker run --net=host subito_docker
```

``` Dreams without Goals are just Dreams ```


ᵈᵉᵛᵉˡᵒᵖᵉᵈ ᵇʸ 𝙡𝙪𝙘𝙖𝙞𝙢𝙗𝙖𝙡𝙯𝙖𝙣𝙤@𝙜𝙢𝙖𝙞𝙡.𝙘𝙤𝙢