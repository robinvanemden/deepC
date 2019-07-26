
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# pylint: disable=invalid-name, unused-argument
#
# This file is part of DNN compiler maintained at 
# https://github.com/ai-techsystems/dnnCompiler
#
# Author:
# Date:

import torch.onnx
import torch.nn as nn
import numpy as np
import onnx

onnx_filename = "./testcases/threshold/threshold.onnx"
text_filename = "./testcases/threshold/threshold.txt"

model = nn.Threshold(0, 0)
test_input = torch.randn(2)
torch.onnx.export(model, test_input, onnx_filename)
with open(text_filename, 'w') as f:
	model = onnx.load(onnx_filename)
	f.write(str(model.graph))