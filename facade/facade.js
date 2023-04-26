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

// Output
// -------------------------------
// Proceed! Image type is supported.
// Proceed! Image size is ok.
// Uploading the image!
// -------------------------------
// Proceed! Image type is supported.
// Can't proceed! Image size exceeded.
// Uploading failed!
// -------------------------------
