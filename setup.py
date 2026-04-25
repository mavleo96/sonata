# Copyright (c) Meta Platforms, Inc. and affiliates.
#
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

from setuptools import setup, find_packages


setup(
    name="sonata",
    version="1.0",
    description="",
    author="Xiaoyang Wu",
    packages=find_packages(exclude=["demo*"]),
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=[
        "addict",
        "huggingface_hub",
        "numpy<=1.26.4",
        "packaging",
        "scipy",
        "timm",
        "torch",
        "psutil",
    ],
)
