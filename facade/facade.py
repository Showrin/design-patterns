class Image:
    name = None
    ext = None
    data = None
    size = None

    def __init__(self, name, ext, data, size) -> None:
        self.name = name
        self.ext = ext
        self.data = data
        self.size = size


class AwsImgUploadManager:
    _bucket_name = None
    _secret = None
    supported_types = ["png", "jpg"]
    size_limit = 10

    def __init__(self, bucket, secret) -> None:
        self._bucket_name = bucket
        self._secret = secret

    def __check_img_type(self, img: Image):
        if img.ext in self.supported_types:
            print("Proceed! Image type is supported.")
            return True

        print("Can't proceed! Image type is not supported.")
        return False

    def __check_img_size(self, img: Image):
        if img.size <= self.size_limit:
            print("Proceed! Image size is ok.")
            return True

        print("Can't proceed! Image size exceeded.")
        return False

    def upload(self, img: Image):
        can_upload = self.__check_img_type(img) and self.__check_img_size(img)

        if can_upload:
            print("Uploading the image!")
        else:
            print("Uploading failed!")


uploadManager = AwsImgUploadManager(
    bucket="Image_Bucket", secret="secret_code")

print("-------------------------------")
img_1 = Image(name="Test Image", ext="png", data="Image data", size=8)
uploadManager.upload(img_1)

print("-------------------------------")

img_2 = Image(name="Test Image 2", ext="png", data="Image data 2", size=13)
uploadManager.upload(img_2)
print("-------------------------------")

# Output
# -------------------------------
# Proceed! Image type is supported.
# Proceed! Image size is ok.
# Uploading the image!
# -------------------------------
# Proceed! Image type is supported.
# Can't proceed! Image size exceeded.
# Uploading failed!
# -------------------------------
