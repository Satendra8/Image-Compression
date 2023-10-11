# # Lossless Image Compression

Python script that performs lossless image compression. The script traverse through a specified directory, locate all the images within it, and apply lossless compression to each image. It is crucial to maintain the image quality during compression.


### Prerequisites
**
-   AWS Access Key and Secret Key with sufficient permissions to access and modify the target S3 bucket.
-   Python 3.x installed on your system.
-   Required Python libraries (`boto3`, `PIL`) installed.
**

## Usage

##### To use the script, follow these steps:
1.  Clone this repository or download the script to your local machine.
    
2. Open the script in a text editor or IDE and set the following parameters in the `main` function:
    
    -   `aws_access_key`: Your AWS Access Key.
    -   `aws_secret_key`: Your AWS Secret Key.
    -   `bucket_name`: The name of the target AWS S3 bucket.
    -   `folder_prefix`: The prefix or folder within the bucket where the images are located.
    -   `region`: The AWS region where the S3 bucket is located.
3. Run the script using Python:
	`python image_compression.py`
4. The script will traverse through the specified S3 bucket, locate image files (JPEG and PNG), apply lossless compression to each image, and upload the compressed images back to the S3 bucket.
5. The original file structure within the S3 bucket will be retained, and image quality will not be compromised during compression.

##### Author
Satendra Kumar