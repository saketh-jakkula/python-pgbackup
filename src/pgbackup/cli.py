from argparse import ArgumentParser,Action


class DriverAction(Action):
    def __call__(self,parser,namespace,values,option_string=None):
        driver = values[0]
        namespace.driver = driver.lower()
        namespace.destination = None

        if len(values) > 1:
            destination = values[1]
            namespace.destination = destination

def create_parser():

    parser = ArgumentParser("Backup the postgress to local or cloud")

    parser.add_argument("url",help = 'Place the link for the databse')

    parser.add_argument("--driver","-d",help = 'mention driver info and the destination path',metavar = ("DRIVER", "DESTINATION"),action=DriverAction,nargs = 2 )

    return parser

def main():
    import boto3
    from pgbackup import storage,pgdump
    import sys
    import time

    arg = create_parser().parse_args()

    timestamp = time.strftime("%Y-%d-%b",time.localtime())

    if not arg.destination:
        filename = pgdump.dump_file_name(arg.url,timestamp)
    else:
        filename = arg.destination

    try:
        dump = pgdump.pg_dump(arg.url)

        if arg.driver == 's3' :
            client = boto3.client('s3')
            storage.s3(client,dump.stdout,arg.destination,backup)
        else:
            outfile = open(filename,'wb')
            storage.local(dump.stdout,outfile)
            outfile.close()

    except OSError:
        print("it errored ")
        sys.exit(1)


