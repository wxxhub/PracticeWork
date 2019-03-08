from aip import AipFace

""" 你的 APPID AK SK """
APP_ID = '15704263'
API_KEY = '8Pxfzs2uK4QE8k8g9v0F8o3v'
SECRET_KEY = 'Wi9nWmiqoqb8sN4YULl1BPygDSXwyZGI'
import base64;

client = AipFace(APP_ID, API_KEY, SECRET_KEY);
# ==========================================================
""" 读取图片 """

filepath = "hb.jpg"
with open(filepath, "rb") as fp:
    base64_data = base64.b64encode(fp.read())
image = str(base64_data, 'utf-8')
imageType = "BASE64"
""" 调用人脸检测 """
rb =  client.detect(image,imageType);
print(rb)


""" 如果有可选参数 """
options = {}
options["max_face_num"] = 2
options["face_fields"] = "age"

""" 带参数调用人脸检测 """
rb = client.detect(image,imageType, options)
print(rb)
# =====================================================
