# Chia-Plot-Transfer
This is a python script to transfer chia plots from your temp drive to your farming drive(s)<br>
This script will get a list of your plot files on your temp drive and copy the files to your farming drives.<br>
It will check your drives and make sure you have enough space available before it copies. After it copies, it will delete the plot file from your temp drive. If your mining drive does not have the available space for the plot file, it will skip to the next farming drive. Edit the InputDrive and outputDrives to your drives. Keep the same syntax as shown in the template python file.<br>
<br>
<br>
Version 2 now has an infinate loop. it does not end and continues to rescan after going through the initial plot files. <br>
Also added was a scan delay feature. On line 10, there is a scanDelay setting that you set to how many minutes you want to delay between scans <br>
<br>
<br>
