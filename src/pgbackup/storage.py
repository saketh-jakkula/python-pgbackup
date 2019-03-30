def local(infile,outfile):
    outfile.write(infile.read())

def s3(client,infile,bucket,outfile):
    client.upload_fileobj(infile,bucket,outfile)

