from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python import get_package_share_directory

def generate_launch_description():

    gazebo_dir = get_package_share_directory('turtlebot3_gazebo')
    gazebo_launch_file = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gazebo_dir + '/launch/turtlebot3_world.launch.py')
    )

    nav2_dir = get_package_share_directory('turtlebot3_cartographer')
    nav2_launch_file = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(nav2_dir + '/launch/cartographer.launch.py')
    )

    return LaunchDescription([
        gazebo_launch_file,
        Node(
            package='turtlebot3_teleop',
            executable='teleop_keyboard',
            name='teleop',
            prefix='gnome-terminal --',
            output='screen'
        ),
        nav2_launch_file
    ])