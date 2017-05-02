from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import boto3, boto
from login_and_registration import *
from browse import *

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Create your views here.
def index(request):
    # Print out bucket names
    for bucket in s3.buckets.all():
        print '*'*50
        print(bucket.name)
    return render(request, 'company/index.html')

def add_video(request):
    # Create an S3 client
    # s3 = boto3.client('s3')
    conn = boto.connect_s3()
    k = Key(b)
    k.key = 'test'
    k.set_contents_from_filename(request.FILES['episode_file'])

    # Upload a new file

    # print request.FILES['episode_file']
    # fs = FileSystemStorage()
    # filename = fs.save(request.POST['episode_name'] + '.jpg', request.FILES['episode_file'])
    # img_file = Image.open(request.POST['episode_name'] + '.jpg')
    # print img_file.size
    # data = open(request.FILES, 'rb')
    # s3.Bucket('wrestle-coast-bucket').put_object(Key='episode_file', Body=data)

    # filename = request.POST['episode_name']
    # bucket_name = 'wrestle-coast-bucket'

    # Uploads the given file using a managed uploader, which will split up large
    # files automatically and upload parts in parallel.
    # s3.upload_file(
    # request.POST['episode_name'],
    # 'wrestle-coast-bucket',
    # request.POST['episode_name']
    # )
    return redirect('/company')

def logout(request):
    request.session.clear()
    return redirect('/')
