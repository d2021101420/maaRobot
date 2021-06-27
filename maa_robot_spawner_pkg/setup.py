import os # Operating system library
from glob import glob # Handles file path names
from setuptools import setup # Facilitates the building of packages

package_name = 'maa_robot_spawner_pkg'
# Path of the current directory
cur_directory_path = os.path.abspath(os.path.dirname(__file__))

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        # Path to the launch file      
        (os.path.join('share', package_name,'launch'), glob('launch/*.launch.py')),

        # Path to the world file
        (os.path.join('share', package_name,'worlds/'), glob('./worlds/*')),

        # Path to the warehouse sdf file
        (os.path.join('share', package_name,'models/maa_cenario2/'), glob('./models/maa_cenario2/*')),

        # Path to the mobile robot sdf file
        (os.path.join('share', package_name,'models/maa_robot/'), glob('./models/maa_robot/*')),
        
        # Path to the world file (i.e. warehouse + global environment)
        (os.path.join('share', package_name,'models/'), glob('./worlds/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Mauricio A Almeida',
    maintainer_email='d2021101420@unifei.edu.br',
    description='Trabalho de CCO0116 - Mauricio A.ALmeida 2021101420',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          'spawn_demo = maa_robot_spawner_pkg.spawn_demo:main'
        ],
    },
)
