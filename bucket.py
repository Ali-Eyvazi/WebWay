import boto3
from WebWay import settings


class Bucket:    
    """
    CDN Bucket MAnager
    
    init method creates connection

    Note :
        none of this methodes are async.use public interface in tasks.py modules instead.

    """
    def __init__(self):
        session=boto3.session.Session()
        self.conn=session.client(
            service_name=settings.AWS_SERVICE_NAME,
            aws_access_key_id=settings.AWS_S3_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL

        )

    def get_objects(self):
        result=self.conn.list_objects_v2(bucket=settings.AWS_STORAGE_BUCKET_NAME)
        if result['KeyCount']:
            return result['Contents']
        else:
            return None

    def delete_object(self,key):
        self.conn.delete_object(bucket=settings.AWS_STORAGE_BUCKET_NAME,key=key)
        return True



    def download_object(self,key):
        with open(settings.AWS_LOCAL_STORAGE + key, 'wb') as f:
            self.conn.download_fileobj(settings.AWS_STORAGE_BUCKET_NAME, key, f)

    def upload_object(self,key):
        with open(key, "rb") as f:
            self.conn.upload_fileobj(f, settings.AWS_STORAGE_BUCKET_NAME, key)


    

bucket=Bucket()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
