import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    nebula_ros_share_dir = get_package_share_directory('nebula_ros')
    velodyne_launch_file = os.path.join(nebula_ros_share_dir, 'launch', 'velodyne_launch_all_hw.xml')
    
    velodyne_launch = IncludeLaunchDescription(
        XMLLaunchDescriptionSource(velodyne_launch_file),
        launch_arguments={'sensor_model': 'VLP16'}.items()
    )
    
    v4l2_camera_node = Node(
        package='v4l2_camera',
        executable='v4l2_camera_node',
        output='screen'
    )
    
    return LaunchDescription([
        velodyne_launch,
        v4l2_camera_node
    ])
