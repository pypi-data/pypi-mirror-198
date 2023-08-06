from paddleocr import PaddleOCR
def model():
        ocr = PaddleOCR(use_angle_cls=True,use_gpu=True,rec_model_dir="paddleocr/rec/",drop_score=0.5,det=True,show_log = False)
        return ocr
