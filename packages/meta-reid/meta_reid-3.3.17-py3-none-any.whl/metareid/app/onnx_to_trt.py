from ..model_zoo import onnx2trt


class Onnx2Trt:
    def __init__(self,
                 onnx_file="models/baseline_R50.onnx",
                 trt_file="models/baseline_R50.trt",
                 precision="fp16",
                 verbose=False,
                 workspace=8):
        self.onnx_file = onnx_file
        self.trt_file = trt_file
        self.precision = precision
        self.verbose = verbose
        self.workspace = workspace

    def convert(self):
        onnx2trt(self.onnx_file, self.trt_file, self.precision, max_workspace_size=self.workspace, int8_calibrator=None)
