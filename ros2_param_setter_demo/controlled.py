# Copyright 2021 Viktor Kravchenko (viktor@vik.works)

# Licensed under the Apache License, Version 2.0 (the "License")
#  you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#      http: // www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import SetParametersResult


class ControlledNode(Node):
    def __init__(self):
        super().__init__("controlled")
        self.get_logger().info("node launched ok")
        self.mode = ""
        self.add_on_set_parameters_callback(self.handle_param_change)
        self.declare_parameter("mode", "INITAL MODE")

    def handle_param_change(self, params):
        for param in params:
            if param.name == "mode":
                self.mode = param.value
                self.get_logger().info(f"mode is {self.mode}")
                return SetParametersResult(successful=True)
        return SetParametersResult(successful=False)


def main(args=None):
    rclpy.init(args=args)
    remapper = ControlledNode()
    rclpy.spin(remapper)
    remapper.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
