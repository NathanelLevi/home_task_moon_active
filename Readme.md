# Explanation
In microservices dir:
- We have a `main.py` file that contains the route that uses `API_URL` env var

In numbers_api dir:
- We have a `main.py` file that contains the route that implemets 2 different api paths for odd and even numbers

In the root dir:
- We have an `app.py` file that implements `ready`, `evennumber` and `oddnumber` routes
- I did it that way because I'm not so familiar with flask and I tried to finish the task As fast as I can.

### pre requisites:
1. create virtual env for python 3.9
2. run `pip install -r requirements.txt`

## To test task 3:
1. Navigate to numbers_api dir, run from terminal: `python main.py`
2. Go to browser: `http://127.0.0.1:5000/odd` --> you'll get a random odd number
3. Go to browser: `http://127.0.0.1:5000/even` --> you'll get a random even number

## To test task 4:
1. Run from terminal: `export API_URL=https://run.mocky.io/v3/08131f7e-216d-4387-bf7a-d234b9964551`
2. Navigate to microservices dir, run from terminal: `python main.py`
3. Go to browser: `http://127.0.0.1:5000/` --> you'll get a response according to the env var URL

## To test task 5:
I've used minikube, and it didn't work well, but it will work well with a managed K8S cluster 

1st, I need to build a docker image and push to registry, in my case it's my registry.
```
docker buildx build --platform linux/arm64/v8 -t freshkorabs/ma-app .
docker push freshkorabs/ma-app:latest
```

These are the commands for deploying the helm charts :
```
oddnumber:
    helm upgrade odd helm --set path=oddnumber --install
 
evennumber:
    helm upgrade odd helm --set path=evennumber --install
```
