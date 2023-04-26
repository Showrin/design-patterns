# Facade Pattern

Facade is a structural design pattern that provides a simplified interface to a library, framework or any other complex set of classes.

## Real Life use cases

1. pydash.get() or lodash.get()
2. setState() in react
3. AWS image upload

## Implementation

### Facade pattern in Python

```
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

```

#### Output

```
-------------------------------
Proceed! Image type is supported.
Proceed! Image size is ok.
Uploading the image!
-------------------------------
Proceed! Image type is supported.
Can't proceed! Image size exceeded.
Uploading failed!
-------------------------------

```

### Facade pattern in JS

```
class Image {
	name = null;
	ext = null;
	data = null;
	size = null;

	constructor(name, ext, data, size) {
		this.name = name;
		this.ext = ext;
		this.data = data;
		this.size = size;
	}
}

class AwsImgUploadManager {
	bucket_name = null;
	secret = null;
	supported_types = ["png", "jpg"];
	size_limit = 10;

	constructor(bucket, secret) {
		this._bucket_name = bucket;
		this._secret = secret;
	}

	check_img_type(img) {
		if (this.supported_types.includes(img.ext)) {
			console.log("Proceed! Image type is supported.");
			return true;
		}

		console.log("Can't proceed! Image type is not supported.");
		return false;
	}

	check_img_size(img) {
		if (img.size <= this.size_limit) {
			console.log("Proceed! Image size is ok.");
			return true;
		}

		console.log("Can't proceed! Image size exceeded.");
		return false;
	}

	upload(img) {
		const canUpload = this.check_img_type(img) && this.check_img_size(img);

		if (canUpload) {
			console.log("Uploading the image!");
		} else {
			console.log("Uploading failed!");
		}
	}
}

const uploadManager = new AwsImgUploadManager("Image_Bucket", "secret_code");
console.log("-------------------------------");
const img1 = new Image("Test Image", "png", "Image data", 8);
uploadManager.upload(img1);

console.log("-------------------------------");

const img2 = new Image("Test Image 2", "png", "Image data 2", 13);
uploadManager.upload(img2);
console.log("-------------------------------");

```

### Output

```
-------------------------------
Proceed! Image type is supported.
Proceed! Image size is ok.
Uploading the image!
-------------------------------
Proceed! Image type is supported.
Can't proceed! Image size exceeded.
Uploading failed!
-------------------------------

```
