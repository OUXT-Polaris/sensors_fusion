from setuptools import setup
import os
from glob import glob

package_name = 'sensor_fusion'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        # launch ファイル群のインストール設定
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        # package.xml の配置
        (os.path.join('share', package_name), ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Fumiya Matsuzaki',
    maintainer_email='matsunoki1130@gmail.com',
    description='None',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
