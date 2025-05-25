# Number Publisher-Subscriber ROS 2 Package

## Overview

This ROS 2 package demonstrates a simple example of communication between two nodes using a publisher and a subscriber.  
- The **NumberPublisher** node publishes incrementing integers to the `number` topic once every second.  
- The **NumberSubscriber** node subscribes to the `number` topic and logs the received numbers.

This package is a beginner level package demonstrating the functionality of a subscriber and a publisher.

---

## Installation

Make sure you have a ROS 2 workspace set up. Then clone this repository into the `src` directory:

```bash
cd ~/ros2_ws/src
git clone https://github.com/yourusername/your_repo_name.git

