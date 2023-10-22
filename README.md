# road-quality-gen-collabathon-23
Team 'the green amateurs' project for the Collabathon '23 challenge in Smart Cities

# Collabothon23

Team Members:
- Ravi Kumar
- Doruk Altinkaya
- Fatma Shalaby
- Amitav Chris Mostafa

## General

Our vision with this project is to create an intuitive application that leverages both the power of user intelligence and modern ML techniques to generate datasets and insights to drive efficient city planning.

For example, a road that you frequent is in disrepair. However, the authorities are too slow to pick up on this because most of their working process are still based on surveys and census, heavily impeded by bereaucracy. 

With our solution, you would be able to take a photo of the damages. This will feed through a ML Model that extracts information from your photo. This will be used to update a comprehensive historical dataset on the entirety of Frankfurt or anywhere in Germany. Authorities in planning can now use this to more efficiently drive their repair work.

The motivation for this project developed as we saw the potential for user and AI driven Big Data niche for this area. Currently, there exists no public 
Bundes API that fulfills this, even though most major countries already have it publicly accessible and lots of work are being done on this.

Our codebase can be broadly divided into 3 parts

- The Extraction of Metadat from Photos, done by @fatmashalabi
- The Object Detection Model, done by @semibroiled
- The App API and Frontend, done by @Ravikumar

The main backbone of the endevaour is the backend, with the goal of 
generating a time series data that can be queried for Data Science purposes by anyone. While there are a lot of limitations and scope of improvement, the crucial aspects themselves can be show to be wokring.

## Proof of Concept

For our prototype to take its stage, we could not do so without extraction of metadata from phones or other cameras. This serves as the main basis for our Time Series modelling database records. The most important columns that can be used for data quality checks are included from the metadata, and they are exported/saved as json and csv files.

The Object Detection Dataset itself is derived from a previous IEEE project based in Japan. As members of IEEE and Vorstand from its Student Branch in TU Darmstadt, we have done the due diligence to ensure that it is all open source, with licenses and credits included. Their dated script is then brought up to date with the latest package and minor optimizations to generate a serialized model for our purposes.

While all of these aspects themselves work individually, due to time and team constraints, we have had no way to combine them as a servicable API as of yet.

## Architecture

## Open Source Technologies being leveraged in this Project

- Python 
- Docker
- Tensorflow
- IEEE Big Data Dataset
- Github 

## Working Principles for Metadata Extraction

### Running on a container

The prequisites are, that Docker needs to be installed on local computer and should be running

1) Run `docker-compose up road_quality_app`

2) Run `docker build -t road_quality_app . --no-cache`

3) Run `docker run road_quality_app`

### Runnin locally in a Virtual Environment

First, make you virtual environemnt with 

- `python3 m venv .venv`

Install all the required packages to your virutal environment


All packages and relevant frameworks are downloaded in the `.venv` virtual environment directory. 

You can activate this with `source .venv/bin/activate`

## Tag_Names for metadata
 "36867": "Date Taken",
 "36868": "Time Taken",
 "271": "Camera Make",
 "272": "Camera Model",
 "305": "Software"
#### Packages used for metadata
from PIL import Image
import exifread




## Special Thanks 
IEEE Student Services

Ravi Kumar and Fatma Shalaby @fatmashalabi for their incredible commitmend in seeing our team through the end despite many losses in team members and motivation

maedahi@iis.u-tokyo.ac.jp and @sekilabs incredible curation of Tutorial and Dataset on Github
