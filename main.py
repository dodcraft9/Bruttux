import requests
from threading import Thread
import sys
import optparse

class Request_performer(Thread):
    def __init__(self,word,url):
        Thread.__init__(self)
        try:
            self.word = word.split("\n")[0]
            self.fuzz = url.replace('FUZZ',self.word)
            self.url = self.fuzz
        except Exception as e:
            print(e)
    
    def run(self):
        try:
            r = requests.get(self.url)
            print(self.url + " - " + str(r.status_code))
            word[0]=word[0]-1
        except Exception as e:
            print(e)


def banner():
    print("\n************************************")
    print("*********** Bruttux 1.0 **")
    print("*********** Author: dodccraft **")
    print("****************************************\n")
    print("Example: bruttux.py -u http://www.example.com/FUZZ -t 3 -f common.txt\n")

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest="url", help="url (http://example.com/FUZZ)")
    parser.add_option("-t", "--threads", dest="threads", help="threads")
    parser.add_option("-f", "--file", dest="file", help="dictionary file")
    (options, arguments) = parser.parse_args()
    if not options.url:
        parser.error('[-] Please specify an url, use --help more info.')
    if not options.threads:
        parser.error('[-] Please specify a number of threads, use --help more info.')
    if not options.file:
        parser.error('[-] Please specify a file, use --help more info.')
    return options

def read_dictionary_file(dictionary):
    try:
        f = open(dictionary, "r")
        words = f.readlines()
    except:
        print("Failed opening file: " + dictionary + "\n")
        sys.exit()
    
    return words

def launch_threads(words,threads,url):
    global word
    word = []
    result_list = []
    word.append(0)
    while len(words):
        try:
            if word[0]<int(threads):
                n = words.pop(0)
                word[0]=word[0]+1
                thread=Request_performer(n,url)
                thread.start()

        except KeyboardInterrupt:
            print("The program was interrupted by the user")
            sys.exit()
        thread.join()
    return


def start():
    banner()
    options = get_arguments()
    words = read_dictionary_file(options.file)
    launch_threads(words,options.threads,options.url)


if __name__ == "__main__":
    start()
