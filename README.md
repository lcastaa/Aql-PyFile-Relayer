# Aqlabs PyFile Relayer

## Overview

The Aqlabs PyFile Relayer is a versatile utility meticulously crafted to streamline the process of transferring files and facilitating communication across Docker containers within various network environments. This tool was originally conceived to address a set of intricate challenges I encountered during the development of software within a clustered Raspberry Pi ecosystem, leveraging Docker Swarm and a Jenkins CI/CD Pipeline container. In this setup, the Jenkins CI/CD Pipeline container is tethered to my home network, acquiring a stable and unique IP address through the MACVLAN network driver.
## Problem Statement

In this multi-node setup, Jenkins CI/CD relies on a MACVLAN network driver to obtain an IP address on the actual network, rather than within the Docker network. However, this configuration introduced an issue: when attempting to transfer files via SFTP from Jenkins to other physical nodes, strict RSA key checks prevented successful transfers. Although SSH access was possible, SFTP file transfers were not due to key discrepancies. To bridge this gap, a solution was needed.

## Solution

The Aqlabs PyFile Relayer was developed to overcome these challenges. It offers a straightforward yet effective approach to file transfer and communication, with the potential for future expansion.

## Key Components

The application comprises two primary components:

1. **Receiver Node**: This component is built using Flask and allows you to configure the listening port. It is responsible for receiving files and handling incoming requests.

2. **Sender / Command Node**: Another Flask-based application, this component facilitates file transfer via HTTP. It actively monitors the health of both the sender and receiver nodes and listens for receiver confirmation.

## Version 1.0 Features

The initial release (v1.0) of the Aqlabs PyFile Relayer focuses on providing essential features:

- **File Send and Receive**: Users can easily send and receive files between nodes, overcoming the strict key checks that impeded traditional SFTP transfers.

- **Customizable Ports**: The application is flexible, allowing users to specify the ports on which it should listen, ensuring compatibility with their network setup.

- **Confirmation Mechanism**: The sender node includes a confirmation mechanism, which helps ensure that the receiver has successfully received the file.

This application serves as a foundational tool for addressing file transfer challenges in network configurations similar to the one described. Future versions may introduce additional capabilities and enhancements to further improve its functionality.
