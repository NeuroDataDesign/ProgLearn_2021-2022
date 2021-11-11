[Khetarpal paper](https://arxiv.org/pdf/1811.10732.pdf)

# Background
* Arcade Learning Environment(ALE)  
  * Atari 2600 games
  * dozens of problems ot train on
* OpenAI's Gym
  * broader variety of RL tasks 
* ALE originally was too deterministic, adding stochastisity with multiple game modes
* DeepMind Lab and VizDoom
  * more realistic settings
  * 3D first-person-view environments   
* Minecraft could be leveraged for lifelong learning
* Gazebo is good for robotics 
# Learning in embodied agents
* embodied cognition
  * cognition is grounded in perception and action
  * utilize a rich, multi-modal sensori-motor stream of data
* virtual embodiment can be used in place of physical embodiment
* virtual embodiment is closer to how humans learn through interaction with their environment via multiple sensors and effectors of different types
* curriculum learning
  * virtual environments are easy to modify and train agents in progressive fashion
* short-term and long-term goals
  * equivalent to skills and composition of skills
* mimic agents in real-world scenarios
  * encapsulate the real world dynamics in a simulated environment as faithfully as possible
  * more realistic domains
* cause and effect learning
  * rich data streams helps agents understand the causality relationships of various events         
# This is a good paper if we want to find more datasets for testing
* multiple datasets with indoor scenes and house layouts
* not a lot of discussion of how the data is read in
