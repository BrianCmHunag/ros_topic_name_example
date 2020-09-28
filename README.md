# ros_topic_name_example
A example to check the topic names of different kind of node names.


## Conclusion: 
| namespace | node name | topic name  | --> | rostopic list  |
|---|---|---|---|---|
| X  | robot | pose | -->   | /pose  |
| X  | robot | .pose  | -->   | /robot/pose  |
| ns  | robot  |  pose | -->  |  /ns/pose  |
| ns  | robot  |  .pose | -->  |  /ns/robot/pose  |

ref: <br>
1. [[ROS in 5 mins] 046 – What is ROS Namespace](https://www.theconstructsim.com/ros-5-mins-046-ros-namespace/)
2. [Names - ROS Wiki](http://wiki.ros.org/Names)
