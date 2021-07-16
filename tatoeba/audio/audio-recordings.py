#First, you have to download the sentence file and the audio file. The sentence file contains all sentences, the audio
#file contains Ids of the recorded sentences.
# extract lang sentences from src file and generate target file

lang="kab"
src_file="sentences.csv"
target_file="sentences_kab.csv"

def extract_lang(lang,src_file,target_file):
    f= open(src_file,encoding='utf-8')
    kab=open(target_file,"w+",encoding='utf-8')

    i=0
    line=""
    for line in f:
        line=line.replace("\ufeff","")
        values = line.split("\t")
        #extract only kabyle sentences to a file.
        if (values[1]==lang):
         kab.write(line)


    f.close()
    kab.close()
extract_lang(lang,src_file,target_file)
sentences_ids=[]
text_file="sentences_kab.csv"

#extract the senetnces ids from the sentences text file
def extract_sentences_ids(text_file,sentences_ids):

  f= open(text_file,encoding='utf-8')

  for line in f:
        line=line.replace("\ufeff","")
        values = line.split("\t")

        sentences_ids.append(int(values[0]))
  f.close()

  return sentences_ids

# create a text file for sentences wich have only recordings
sentences_ids= extract_sentences_ids(text_file,sentences_ids)
print (sentences_ids[:10])
target_audio_file= "sentences_kab_with_audio.csv"
audio_file="sentences_with_audio.csv"



def generate_lang_file_audio (target_audio_file,audio_file,sentences_ids,lang):

    kab_audio=open(target_audio_file,"w+",encoding='utf-8')
    f= open(audio_file,encoding='utf-8')

    for line in f:
            line=line.replace("\ufeff","")

            values = line.split("\t")

            if int(values[0]) in sentences_ids:
             #audiokab.append(values[1])
             kab_audio.write("https://audio.tatoeba.org/sentences/"+lang+"/"+values[0]+".mp3\n")
    kab_audio.close()
    f.close()

generate_lang_file_audio (target_audio_file,audio_file,sentences_ids,lang)

# download the audio regordings
import wget

target_audio_file="sentences_with_audio.csv"

def download (target_audio_file):
    f=open(target_audio_file,encoding='utf-8')
    for url in f:
        values = url.split("\t")
        try:
         wget.download(values[1])
        except:
         print ("file error", values[1])

    f.close()
download (target_audio_file)
