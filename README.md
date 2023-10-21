# Aqlabs PyCD File Relayer

## Overview
The Aqlabs PyCD File Relayer is a tool designed to transfer files between nodes via http.

## Problem Statement
The way my application is set up goes as follows. There are 3 nodes all running docker and clustered using docker swarm. <br>
I have a Jenkins CI/CD pipeline running on the 3rd node, and it's using an IP from my network not the docker network. <br>
Oddly since Jenkins is running in a docker environment and on the deployment node I cannot send files from the docker container <br>
to the host node via SSH now I tried to mount a volume and have the output from the pipeline save there but that did not work.

## Solution

Oddly when I access the jenkins container's terminal I can ssh to other nodes i.e(node 1, node 2) on my network just not the host which is node 3.<br>
So I decided to create a relayer where Jenkins will send the output JAR file to [ node 2 ] via HTTP and [ node 2 ] will send it back to [ node 3 ] 
and [ node 3 ] will deploy the JAR file. 


## Key Components

The application comprises two primary components:
- <b>Relayer MODE</b>: Which runs the tool as a relayer. It will accept a file and send it to another external node.
- <b>Receiver MODE</b>: Which runs the tool as a receiver making it listen for a request and execute the file. 


## Version 1.0 Features

The initial release (v1.0) of the Aqlabs PyFile Relayer focuses on providing essential features:
- **Relayer**: Relays file from pipeline to deployment node. With ability to input Destination IP
- **Receiver**: Receives file from relayer.
