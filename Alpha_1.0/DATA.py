preinstalled_packages = {"subsystem", "sys", "os", "subprocess", "pkg_resources", 'time'}
required_packages = {'pandas', 'tk', 'unidecode', 'selenium'}

filetypes = [("CSV", "*.csv"), ("Excel", "*.xlsx"), ("Text", ".txt"), ("Tots els fitxers (No recomanat)", "*.*")]


# ---------------- OBJECTS -------------------------------

class Attributes_:
  TOTAL_attributes = []
  def __init__(self, name:str):
    self.name = name;
    self.elements = [];
    Attributes_.TOTAL_attributes.append(self);

class Noms_(Attributes_):
  pass;

class Menjador_(Attributes_):
  pass;

class Pati_(Attributes_):
  pass;

class RelacioAdult_(Attributes_):
  pass;

class RelacioComapnys_(Attributes_):
  pass;


# ---------------- MISSATGES ------------------------------------
class Message_:
  def __init__(self):
    pass;

  def print(self):
    pass;

WelcomeMsg: str = "\n\n\n" + "-"*50 + "\nPrograma Creat Per: ALEX PLANELLES ALONSO\n\n\tNo sigueu xoriços.\n\nPer qualsevol problema contacteu amb mi a traves de: alexplanelles@gmail.com\nO bé accediu directament al github del programa a través del link:\nhttps://github.com/PlanellesAlex/AlexCimCollserola.git \n\n" + "-"*50;


ErrMsg1: str = "";


#  ...

