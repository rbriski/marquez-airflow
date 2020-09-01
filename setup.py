# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

NAME = "marquez-airflow"
VERSION = "0.2.0"

setuptools.setup(
    name=NAME,
    version=VERSION,
    author="Marquez Team",
    author_email="",
    description="Marquez integration with Airflow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MarquezProject/marquez-airflow",
    packages=setuptools.find_packages(),
    install_requires=[
        "marquez-python==0.7.0",
        "sqlparse==0.3.1"
    ],
)
