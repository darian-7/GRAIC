## Generalized RAcing Intelligence Competition (GRAIC)

GRAIC is a simulated vehicle race co-located with CPS-IOT Week 2023. GRAIC aims to bring together researchers in AI, planning, synthesis, and control to create a platform for comparing different algorithms for controlling vehicles in dynamic and uncertain environments. At runtime, the input to the controller will come from a perception oracle that will provide as input a local view of obstacles, lanes, and gates on the track near the vehicle. The tracks will have à priori unknown static and moving obstacles. The outputs from the controller (brake, throttle, and steering) will drive the vehicle. In some race categories, you will be provided a mathematical vehicle model, and in other categories you will be provided a black-box vehicle simulator. The perception and control interfaces will not change. 

(./docs/GRAIC.gif)


## Installation Setup Instructions

### Install the Carla 0.9.13 Simulator
* You can find the official installation guide [here](https://carla.readthedocs.io/en/latest/start_quickstart/#carla-installation).
  For a simpler installation walkthrough, follow these steps:

1. Download the Carla 0.9.13 simulator [here](https://carla-releases.s3.eu-west-3.amazonaws.com/Linux/CARLA_0.9.13.tar.gz).
2. Extract it to your preferred path (e.g., `/home/yanmiao2/ws/CARLA_0.9.13`):
   ```bash
   tar -xvzf CARLA_0.9.13.tar.gz -C /home/yanmiao2/ws/

Install required library:
'sudo apt install libomp5'

Add Carla API to your Python path by appending the following lines to your ~/.bashrc file and source the file:
'''
echo 'export PYTHONPATH=$PYTHONPATH:/home/yanmiao2/ws/CARLA_0.9.13/PythonAPI/carla/' >> ~/.bashrc
echo 'export PYTHONPATH=$PYTHONPATH:/home/yanmiao2/ws/CARLA_0.9.13/PythonAPI/carla/dist/carla-0.9.13-py3.7-linux-x86_64.egg' >> ~/.bashrc
source ~/.bashrc
'''

Install individual packages:
'''
python3 -m pip install --user pygame numpy
python3 -m pip install --upgrade networkx
'''

To launch the simulator:
'''
cd /home/yanmiao2/ws/CARLA_0.9.13/
./CarlaUE4.sh
'''

### Install GRAIC Customized Maps for Carla 0.9.13

	•	You can find the official installation guide [here](https://carla.readthedocs.io/en/0.9.13/tuto_M_add_map_package/).
For a simpler installation walkthrough, follow these steps:

1.	Download the 5 raw maps from the provided Google Drive link.
2.	Place the 5 .tar.gz files in your corresponding import path (e.g., /home/yanmiao2/ws/CARLA_0.9.13/Import).
3.	Import the maps:
'''
cd /home/yanmiao2/ws/CARLA_0.9.13
./ImportAssets.sh
'''

To switch to any of the 5 maps:

1.	Launch the simulator:
'''
cd /home/yanmiao2/ws/CARLA_0.9.13/
./CarlaUE4.sh
'''

2. Open a new terminal and list the maps:
'''
cd /home/yanmiao2/ws/CARLA_0.9.13/PythonAPI/util
python3 config.py --list
'''

3.	Switch to a new map:
'python3 config.py -m /Game/map_package/Maps/shanghai_intl_circuit/shanghai_intl_circuit'

Replace shanghai_intl_circuit with t1, t2, t3, or t4 to switch to different GRAIC maps.

### Install GRAIC Customized Scenario Runner

•	Use the customized Scenario Runner from the [GRAIC public repository](https://github.com/PoPGRI/scenario_runner).

1.	Download the customized 0.9.13 Scenario Runner from GRAIC public repo.
2.	Extract Scenario Runner to your workstation (e.g., /home/yanmiao2/ws/scenario_runner-0.9.13).
3.	Install Scenario Runner dependencies:
'''
cd /home/yanmiao2/ws/scenario_runner-0.9.13
python3 -m pip install -r requirements.txt
'''

4.	Add Scenario Runner API to your Python path by appending the following line to your ~/.bashrc file and source the file:
'''
echo 'export PYTHONPATH=$PYTHONPATH:/home/yanmiao2/ws/scenario_runner-0.9.13' >> ~/.bashrc
source ~/.bashrc
'''

To test the setup, run the following script (e.g., copy to test.py):
'''
from scenario_runner import ScenarioRunner
print("Success")

python3 test.py
'''

### Install GRAIC Customized Scripts

1.	Download GRAIC infrastructure scripts for 2022 from here.
2.	Place the folder into your workspace (e.g., /home/yanmiao2/ws/Race).
3.	Implement your controller in agent.py.

Launch the GRAIC

1.	Open Terminal 1 and launch the simulator:
'''
cd /home/yanmiao2/ws/CARLA_0.9.13/
./CarlaUE4.sh
'''

2.	Open Terminal 2 and run the wrapper script:
'''
cd /home/yanmiao2/ws/Race
python3 wrapper.py
'''

•	To change maps, modify line 6 in wrapper.py. Available maps: shanghai_intl_circuit, t1_triple, t2_triple, t3, t4.
•	To test the controller without scenarios, comment out line 10 in wrapper.py.
•	To stop a running Python script, use pkill -9 -f python3.

Notes

1.	Only modify agent.py. Other files will be overwritten during grading.
2.	Carla Python API: Refer to [Carla Python API](https://carla.readthedocs.io/en/0.9.13/python_api/).
3.	Model + Track: The code runs Tesla Model 3 on the Shanghai Track; different models and tracks may be used during testing.
4.	Scoring & Collision:
•	The score is based on the time to finish a lap.
•	Controllers are ranked by the number of collisions first, then by time.
•	Collisions might affect the car’s state and the controller’s performance.



## UIUC Academic Integrity

DO NOT COPY. Only for reference. I hereby state that I shall not be held responsible for any misuse of my work or any academic integrity violations.
