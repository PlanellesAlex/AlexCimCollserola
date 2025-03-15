import DATA
import ChromeInteraction
import subprocess
import sys
import os
import pkg_resources

# -------------------------
from tkinter import filedialog
from unidecode import unidecode
import pandas as pd

# ------------------------------


def file_dialog():
  FilePath = filedialog.askopenfilename(title = "Troba el fitxer SEM", initialdir = "../" , filetypes = DATA.filetypes, multiple = False);
  return FilePath;


def check_File_extension(FilePath):
  if FilePath.endswith('.csv'):
    llegir_csv(FilePath);
  # elif FilePath.endswith('.xls'):  
  #   llegir_excel(FilePath);
  # elif FilePath.endswith('.txt'):
  #   llegir_txt(FilePath);
  else:
    print("Fromat del fitxer no suportat.\n Aquesta versió només accepta fitxers *.csv");
    quit(1);


  
def llegir_csv(FilePath):
  try:
    df = pd.read_csv(FilePath);
    (rows, columns) = df.shape
    # Els noms comencen a la posicio [9,2]
    for j in range(2, columns):
      contador = 0;
      for i in range(rows):
        if str(df.iat[i,2]) == "nan":
          continue;
        else:
          if contador == 0:
            DATA.Noms_(str(df.iat[i, j]));
            contador +=1;
          else:
            DATA.Attributes_.TOTAL_attributes[j-2].elements.append(df.iat[i,j])

  except Exception as e:
    print(e);
    quit(1);



def main():
  print(DATA.WelcomeMsg);
  email = ChromeInteraction.Pregunta_mail();
  FilePath = file_dialog();
  check_File_extension(FilePath=FilePath);
  ChromeInteraction.FundacioLink(email = email)
  input("Programa Finalitzat. Clica ENTER per Tancar la Finestra");
  

if __name__ == "__main__":
  main();



