import io
import boto3
from PIL import Image


def compress_image_s3(bucket_name, s3_key, session):
    try:
        s3 = session.client('s3')
        response = s3.get_object(Bucket=bucket_name, Key=s3_key)
        image_data = response['Body'].read()
        extension = s3_key.split('.')[-1]
        # Set the content type based on the file extension
        if extension == '.jpg' or extension == '.jpeg':
            content_type = 'image/jpeg'
        elif extension == '.png':
            content_type = 'image/png'
        else:
            content_type = 'application/octet-stream'
        # Compress the image in memory
        with Image.open(io.BytesIO(image_data)) as img:
                        
            # Create a new in-memory buffer to save the compressed image
            image_bytes = io.BytesIO()
            img.save(image_bytes, format=img.format, quality=70, optimize=True)
            
            # Get the compressed image data from the buffer
            compressed_image_data = image_bytes.getvalue()

        # Upload the compressed image back to S3 with the same key and content type
        print("Compress Successfull !!!")
        s3.put_object(
            Bucket=bucket_name,
            Key=s3_key,
            Body=compressed_image_data,
            ContentType=content_type  # Set the content type
        )
        print(f"Compressed and updated on S3: {s3_key}")
    except Exception as e:
        print(f"Error in compressing {s3_key}: {str(e)}")


def main(aws_access_key, aws_secret_key, bucket_name, folder_prefix, region):
    # Initializing AWS session
    session = boto3.Session(
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=region
    )

    s3_client = session.client('s3')
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_prefix)
    if 'Contents' in response:
        for obj in response['Contents']:
            s3_key = obj['Key']
            # Only process objects with specified image extensions
            if s3_key.lower().endswith(('.jpg', '.jpeg', '.png')):
                print("Compressing file...", s3_key)
                compress_image_s3(bucket_name, s3_key, session)



# Main function
aws_access_key = "AWS_ACCESS_KEY"
aws_secret_key = "AWS_SECRET_KEY"
folder_prefix = "pictures/"
bucket_name = "satendra-bhatnagar22719"
region = "ap-south-1"
main(aws_access_key, aws_secret_key, bucket_name, folder_prefix, region)
