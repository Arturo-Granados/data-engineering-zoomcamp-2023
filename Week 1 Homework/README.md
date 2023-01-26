# Week 1 Homework
<img src="images_week_1/portada.png" />

Homework 1 for the data engineering zoomcamp by: 

* [https://datatalks.club](https://datatalks.club)

## Question 1. Knowing docker tags

Run the command to get information on Docker 

```docker --help```

Now run the command to get help on the "docker build" command

Which tag has the following text? - *Write the image ID to the file* 

- `--imageid string`
- `--iidfile string`
- `--idimage string`
- `--idfile string`

## Solution 
Step 1. Install docker(comands for ubuntu):

- sudo apt update
- sudo apt install apt-transport-https ca-certificates curl software-properties-common
- curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
- echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
- sudo apt update
- apt-cache policy docker-ce
- sudo apt install docker-ce
- sudo systemctl status docker
- sudo systemctl enable docker
- sudo usermod -aG granados
- docker version 

Step 2. Run the comand docker build --help
output:
<img src="images_week_1/image1.png" />

Answer: -iidfile string





## Question 2. Understanding docker first run 

Run docker with the python:3.9 image in an interactive mode and the entrypoint of bash.
Now check the python modules that are installed ( use pip list). 
How many python packages/modules are installed?

- 1
- 6
- 3
- 7

## Solution 
Step 1. Create dockerfile

<img src="images_week_1/create_dockerfile.png" />

Step 2. Set dockerfile base on python 3.9

<img src="images_week_1/create_image.png" />

Step 3. Look if the image has been created

<img src="images_week_1/see_docker_images.png" />

Step 4. Run docker with the python:3.9 image in an interactive mode and the entrypoint of bash

<img src="images_week_1/build_image.png" />

step 5. Check how many python packages/modules are installed?

<img src="images_week_1/answer.png" />

Answer: 3


# Prepare Postgres

Run Postgres and load data as shown in the videos
We'll use the green taxi trips from January 2019:

```wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz```

You will also need the dataset with zones:

```wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv```

Download this data and put it into Postgres (with jupyter notebooks or with a pipeline)


## Question 3. Count records 

How many taxi trips were totally made on January 15?

Tip: started and finished on 2019-01-15. 

Remember that `lpep_pickup_datetime` and `lpep_dropoff_datetime` columns are in the format timestamp (date and hour+min+sec) and not in date.

- 20689
- 20530
- 17630
- 21090

## Solution
Run the following query:

Answer: 20530

## Question 4. Largest trip for each day

Which was the day with the largest trip distance
Use the pick up time for your calculations.

- 2019-01-18
- 2019-01-28
- 2019-01-15
- 2019-01-10

## Solution
Run the following query:

Answer: 2019-01-15

## Question 5. The number of passengers

In 2019-01-01 how many trips had 2 and 3 passengers?
 
- 2: 1282 ; 3: 266
- 2: 1532 ; 3: 126
- 2: 1282 ; 3: 254
- 2: 1282 ; 3: 274

## Solution
Run the following query:

Answer: 2: 1282 ; 3: 254

## Question 6. Largest tip

For the passengers picked up in the Astoria Zone which was the drop off zone that had the largest tip?
We want the name of the zone, not the id.

Note: it's not a typo, it's `tip` , not `trip`

- Central Park
- Jamaica
- South Ozone Park
- Long Island City/Queens Plaza

## Solution
Run the following query:

Answer:  Long Island City/Queens Plaza