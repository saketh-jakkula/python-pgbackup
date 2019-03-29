from argparse import ArgumentParser,Action


class DriverAction(Action):
    def __call__(self,parser,namespace,values,option_string=None):
        driver,destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():

    parser = ArgumentParser("Backup the postgress to local or cloud")

    parser.add_argument("url",help = 'Place the link for the databse')

    parser.add_argument("--driver",help = 'mention driver info and the destination path',action=DriverAction,nargs = 2 )

    return parser
