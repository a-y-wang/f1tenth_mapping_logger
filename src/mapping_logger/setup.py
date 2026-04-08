from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'mapping_logger'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        # 1. Registers the package so 'ros2 run' can find it
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        
        # 2. Installs the package.xml (the dependency list)
        ('share/' + package_name, ['package.xml']),
        
        # 3. CRITICAL: Installs your launch files so 'ros2 launch' works
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Abbie Wang',
    maintainer_email='abbieywang@utexas.edu',
    description='VSLAM CSV Logger for F1TENTH Senior Design',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # format: 'alias_name = folder_name.file_name:main_function'
            'logger_node = mapping_logger.logger_node:main',
        ],
    },
)