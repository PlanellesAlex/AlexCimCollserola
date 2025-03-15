import DATA
import pkg_resources
import subprocess
import sys

def install_dependencies():
  for package in DATA.required_packages:
    try:
      dist = pkg_resources.get_distribution(package);
      print("{} ({}) està instal·lat".format(dist.key, dist.version));
    except pkg_resources.DistributionNotFound:
      print("{} NO està instal·lat\n...Instal·lant".format(package));
      subprocess.check_call([sys.executable, '-m', 'pip', 'install', "{}".format(package)]);

install_dependencies();