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

        navigation_launch = ExecuteProcess(
                cmd=['ros2', 'launch', 'turtlebot3_navigation2', 'navigation2.launch.py', 'use_sim_time:=True', 'map:=c2-papel.yaml'],
                output='screen'
                )


        return LaunchDescription([
            ##gazebo_launch_file,
            Node(
            package='navigation',
            executable='nav',
            name='nav',
            prefix='gnome-terminal --',
            output='screen'
            ),
            navigation_launch
        ])