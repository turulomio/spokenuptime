#!/usr/bin/python3
import argparse
import datetime
import math
import os
import gettext

# I had a lot of problems with UTF-8. LANG must be es_ES.UTF-8 to work
gettext.textdomain('spoken-uptime')
_=gettext.gettext

def pretty(segundos):
    segundos=int(segundos)
    stri=""
    if args.pretty:
        dias=int(segundos/(24*60*60))
        if dias!=0:
            stri=stri+_("{} days").format(dias)
        segundosquedan=math.fmod(segundos,24*60*60)
        horas=int(segundosquedan/(60*60))
        if horas!=0:
            stri=stri + " "+ _("{} hours").format(horas)
        segundosquedan=math.fmod(segundosquedan,60*60)
        minutos=int(segundosquedan/60)
        if minutos!=0:
            stri=stri + " "+ _("{} minutes").format(minutos)
        segundosquedan=math.fmod(segundosquedan,60)
        segundos=int(segundosquedan)
        if segundos!=0:
            stri=stri + " "+ _("{} seconds").format(segundos)
        return stri
    else:
        return _("{} seconds").format(segundos)
        
        
def average():
    f=open(logfile)
    a=[]
    for l in f.readlines():
        try:
            a.append(float(l[:-1].split('#')[1]))
        except:
            print ("error reading returning 0")
            return 0
    return int(sum(a)/len(a))


# os.getenv is equivalent, and can also give a default value instead of `None`
voice=os.getenv('LC_ALL', 'en')[:2]
if voice not in ('es', 'en'):
    voice='en'

logfile="/var/log/spoken-uptime"
    
parser=argparse.ArgumentParser(prog='spoken-uptime', description=_('It logs and speaks system uptime'),  epilog=_("Developed by Mariano Muñoz 2015 ©"))
parser.add_argument('--version', action='version', version="0.1.0")
parser.add_argument('-l', '--log', help=_('Logs the result'), action='store_true')
parser.add_argument('-s', '--speak', help=_('Speaks the result'), action='store_true')
parser.add_argument('-t', '--statistics',  help=_('Show result with statistics'), action='store_true')
parser.add_argument('-p', '--pretty',  help=_('Show days, hours, minutes and seconds instead of seconds'), action='store_true')
args=parser.parse_args()

f=open('/proc/uptime', 'r')
upseconds= float(f.readline().split()[0])
f.close()

speak=_("System started {} ago").format(pretty(upseconds))
print(speak)

if args.log==True:
    f=open(logfile, "a")
    f.write("{}#{}\n".format(datetime.datetime.now(), upseconds))
    f.close()
            
if args.statistics==True:
    speak_statistics=_("Uptime average is {}").format(average())
    print (speak_statistics)
else:
    speak_statistics=""
    
if args.speak==True:
    os.system("espeak -v {} '{}. {}'".format(voice, speak, speak_statistics))
