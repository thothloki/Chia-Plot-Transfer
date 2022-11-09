import shutil, os, sys, time, threading

# DRIVE THAT YOUR FILES ARE LOCATED AT THAT YOU WANT TO TRANSFER SEPARATE EACH DRIVE WITH A COMMA. 
# MAKE SURE YOU HAVE AN r TO INDICATE A RAW FILE LOCATION
sourceDrives = [r'C:', r'D:']

# DRIVE(S) THAT YOU ARE TRANSFERRING TO FOR MINING. SEPARATE EACH DRIVE WITH A COMMA. 
# MAKE SURE YOU HAVE AN r TO INDICATE A RAW FILE LOCATION
farmDrives = [r'E:', r'F:'] 

#SELECT FILE FORMAT YOU ARE LOOKING TO TRANSFER
fileFormat = '.plot'

#Time delay between scans (in minutes)
scanDelay = 0





######## COLORS ######
progressCOLOR = '\033[38;5;33;48;5;236m' #\033[38;5;33;48;5;236m# copy inside '' for colored progressbar| orange:#\033[38;5;208;48;5;235m
finalCOLOR =  '\033[38;5;33;48;5;33m' #\033[38;5;33;48;5;33m# copy inside '' for colored progressbar| orange:#\033[38;5;208;48;5;208m
########

BOLD    = '\033[1m'
UNDERLINE = '\033[4m'
CEND    = '\033[0m'

def getPERCECENTprogress(source_path, destination_path):
    time.sleep(.24)
    if os.path.exists(destination_path):
        while os.path.getsize(source_path) != os.path.getsize(destination_path):
            sys.stdout.write('\r')
            percentagem = int((float(os.path.getsize(destination_path))/float(os.path.getsize(source_path))) * 100)
            steps = int(percentagem/5)
            copiado = int(os.path.getsize(destination_path)/1000000)# Should be 1024000 but this get's equal to Thunar file manager report (Linux - Xfce)
            sizzz = int(os.path.getsize(source_path)/1000000)
            sys.stdout.write(("         {:d} / {:d} Mb   ".format(copiado, sizzz)) +  (BOLD + progressCOLOR + "{:20s}".format('|'*steps) + CEND) + ("   {:d}% ".format(percentagem))) # BG progress
            sys.stdout.flush()
            time.sleep(.01)

def CPprogress(SOURCE, DESTINATION):
    if os.path.isdir(DESTINATION):
        dst_file = os.path.join(DESTINATION, os.path.basename(SOURCE))
    else: dst_file = DESTINATION
    print ((BOLD + UNDERLINE + "FROM:" + CEND + "   "), SOURCE, "     ", (BOLD + UNDERLINE + "TO:" + CEND + "     "), dst_file)
    #print ((BOLD + UNDERLINE + "TO:" + CEND + "     "), dst_file)
    threading.Thread(name='progresso', target=getPERCECENTprogress, args=(SOURCE, dst_file)).start()
    shutil.copy2(SOURCE, DESTINATION)
    time.sleep(.02)
    sys.stdout.write('\r')
    sys.stdout.write(("         {:d} / {:d} Mb   ".format((int(os.path.getsize(dst_file)/1000000)), (int(os.path.getsize(SOURCE)/1000000)))) +  (BOLD + finalCOLOR + "{:20s}".format('|'*20) + CEND) + ("   {:d}% ".format(100))) # BG progress 100%
    sys.stdout.flush()
    print (" ")
    print (" ")

def main():
    while True:
        #GET LIST OF PLOTS

        for srcDrive in sourceDrives:
            plots = [each for each in os.listdir(srcDrive) if each.endswith(fileFormat)]
            for drive in farmDrives:
                for plot in plots:
                    _, _, free = shutil.disk_usage(drive)
                    if free > os.path.getsize(os.path.join(srcDrive, plot)):
                        print(free)
                        print(os.path.getsize(os.path.join(srcDrive, plot)))
                        plotdir = os.path.join(srcDrive, plot)
                        outdir = os.path.join(drive, plot)
                        CPprogress(plotdir, outdir)
                        print('Plot %s copied to %s, deleting %s' % (plot, drive, plot))
                        plots.remove(plot)
                        os.remove(plotdir)
                    else:
                        print('Plot too large for %s drive, skipping' % (drive))
            time.sleep(scanDelay*60)
 
main()