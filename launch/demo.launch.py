from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="ros2_param_setter_demo",
                executable="controlled_node",
                name="controlled_node",
            ),
            Node(
                package="ros2_param_setter_demo",
                executable="modifier",
                name="modifier",
            ),
        ]
    )
