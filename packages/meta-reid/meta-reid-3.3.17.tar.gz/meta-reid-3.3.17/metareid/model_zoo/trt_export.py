import logging
import tensorrt as trt

logging.basicConfig(level=logging.INFO)
logging.getLogger("trt_export").setLevel(logging.INFO)
logger = logging.getLogger("trt_export")


def onnx2trt(
        onnx_file_path,
        save_path,
        mode,
        log_level='ERROR',
        max_workspace_size=1,
        strict_type_constraints=False,
        int8_calibrator=None,
):
    """build TensorRT model from onnx model.
    Args:
        onnx_file_path (string or io object): onnx model name
        save_path (string): tensortRT serialization save path
        mode (string): Whether or not FP16 or Int8 kernels are permitted during engine build.
        log_level (string, default is ERROR): tensorrt logger level, now
            INTERNAL_ERROR, ERROR, WARNING, INFO, VERBOSE are support.
        max_workspace_size (int, default is 1): The maximum GPU temporary memory which the ICudaEngine can use at
            execution time. default is 1GB.
        strict_type_constraints (bool, default is False): When strict type constraints is set, TensorRT will choose
            the type constraints that conforms to type constraints. If the flag is not enabled higher precision
            implementation may be chosen if it results in higher performance.
        int8_calibrator (volksdep.calibrators.base.BaseCalibrator, default is None): calibrator for int8 mode,
            if None, default calibrator will be used as calibration data.
    """
    mode = mode.lower()
    assert mode in ['fp32', 'fp16', 'int8'], "mode should be in ['fp32', 'fp16', 'int8'], " \
                                             "but got {}".format(mode)

    trt_logger = trt.Logger(getattr(trt.Logger, log_level))
    builder = trt.Builder(trt_logger)

    logger.info("Loading ONNX file from path {}...".format(onnx_file_path))
    EXPLICIT_BATCH = 1 << (int)(trt.NetworkDefinitionCreationFlag.EXPLICIT_BATCH)
    network = builder.create_network(EXPLICIT_BATCH)
    parser = trt.OnnxParser(network, trt_logger)
    if isinstance(onnx_file_path, str):
        with open(onnx_file_path, 'rb') as f:
            logger.info("Beginning ONNX file parsing")
            flag = parser.parse(f.read())
    else:
        flag = parser.parse(onnx_file_path.read())
    if not flag:
        for error in range(parser.num_errors):
            logger.info(parser.get_error(error))

    logger.info("Completed parsing of ONNX file.")
    # re-order output tensor
    output_tensors = [network.get_output(i) for i in range(network.num_outputs)]
    [network.unmark_output(tensor) for tensor in output_tensors]
    for tensor in output_tensors:
        identity_out_tensor = network.add_identity(tensor).get_output(0)
        identity_out_tensor.name = 'identity_{}'.format(tensor.name)
        network.mark_output(tensor=identity_out_tensor)

    config = builder.create_builder_config()
    config.max_workspace_size = max_workspace_size * (1 << 25)
    if mode == 'fp16':
        assert builder.platform_has_fast_fp16, "not support fp16"
        builder.fp16_mode = True
    if mode == 'int8':
        assert builder.platform_has_fast_int8, "not support int8"
        builder.int8_mode = True
        builder.int8_calibrator = int8_calibrator

    if strict_type_constraints:
        config.set_flag(trt.BuilderFlag.STRICT_TYPES)

    logger.info("Building an engine from file {}; this may take a while...".format(onnx_file_path))
    engine = builder.build_cuda_engine(network)
    logger.info("Create engine successfully!")

    logger.info("Saving TRT engine file to path {}".format(save_path))
    with open(save_path, 'wb') as f:
        f.write(engine.serialize())
    logger.info("Engine file has already saved to {}!".format(save_path))
