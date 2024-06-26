
from download import *
from globals import *
from indices import *
from preproc import *
from replicate.replicate import *

download(dataDir)
dfTrain, dfTest = preproc(dataDir)
replicate_all(dfTrain, dfTest)
